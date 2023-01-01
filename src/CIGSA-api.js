const router = require('express').Router();
const { students } = require('./CIGSA-students.json');
const fs = require('fs');

/**
 * Returns an array of all of the privileges a student should have if they are sitting a specific balance
 * @param {int} balance - The balance to calculate the privileges for
 * @returns An array of privileges
 */
function calculatePrivileges(balance) {
    let privilegesArray = [];

    const privileges = {
        3: 'Excursions',
        5: 'Book burrowing',
        7: 'School camp',
        10: 'Mobile phone access',
    }

    if (balance < 3) {
        return ['None'];
    }

    for (let i = 0; i <= balance; i++) {
        if (privileges[i]) {
            privilegesArray.push(privileges[i]);
        }
    }

    return privilegesArray;
}

/**
 * When ran, will update the localhost file with information similar to the cloud, to avoid a reset of all data upon restarting
 */
function updateFileArray() {
    const cloudArrayCopy = {
        'students': students
    };
    fs.writeFileSync('./src/CIGSA-students.json', JSON.stringify(cloudArrayCopy));
}

router.get('/students', (req, res) => {
    res.status(200).send(students);
})

router.get('/students/idlookup/:id', (req, res) => {
    const { id } = req.params;

    const foundStudent = students.find(student => {
        return student.studentId === id;
    })

    if (!foundStudent) return res.status(404).send({ message: 'Student could not be found.' });
    res.status(200).send(foundStudent);
})

router.get('/students/namelookup/:name', (req, res) => {
    let { name } = req.params;
    name = name.toLowerCase();

    const foundStudents = students.filter(student => {
        return (student.firstName + ' ' + student.surname).toLowerCase().includes(name);
    })

    if (!foundStudents || foundStudents.length === 0) return res.status(404).send({ message: 'Student could not be found.' });
    res.status(200).send(foundStudents);
})

router.post('/students', (req, res) => {
    const {
        firstName,
        surname,
        studentId,
        balance
    } = req.body;

    if (!firstName || !surname || !studentId || !balance) return res.status(404).send({ message: 'Invalid arguments.' })

    const existingStudent = students.find(student => {
        return student.studentId === studentId;
    });

    if (existingStudent) return res.status(400).send({ message: 'This student already exists in the database.' })

    students.push({
        firstName,
        surname,
        studentId,
        balance,
        privileges: calculatePrivileges(balance)
    });

    updateFileArray();

    res.status(200).send({ message: 'A student has been added to the database.' });
})

const updateValue = (updated, prev) => !updated ? prev : updated;

router.put('/students/idlookup/:id', (req, res) => {
    const { id } = req.params;

    const existingStudentIndex = students.findIndex(student => {
        return student.studentId === id;
    })

    const existingStudent = students[existingStudentIndex];

    if (!existingStudent) return res.status(404).send({ message: 'The student couldn\'t be found' });

    const {
        firstName,
        surname,
        studentId,
        balance
    } = req.body;

    const replacementStudent = {
        firstName: updateValue(firstName, existingStudent.firstName),
        surname: updateValue(surname, existingStudent.surname),
        studentId: updateValue(studentId, existingStudent.studentId),
        balance: updateValue(balance, existingStudent.balance),
        privileges: calculatePrivileges(balance)
    };

    students.splice(existingStudentIndex, 1, replacementStudent);

    updateFileArray();

    res.status(200).send({ message: 'The student was updated correctly' });
})

router.delete('/students/idlookup/:id', (req, res) => {
    const { id } = req.params;

    const existingStudentIndex = students.findIndex(student => {
        return student.studentId === id;
    })

    const existingStudent = students[existingStudentIndex];

    if (!existingStudent) return res.status(404).send({ message: 'The student couldn\'t be found' });

    students.splice(existingStudentIndex, 1);

    updateFileArray();

    res.status(200).send({ message: 'The student was successfully deleted. '});
}) 

module.exports = router;