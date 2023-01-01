import csv
from os.path import exists

# all students are added to this student list, with the key being the student id
studentList = {}

# depending on the entered balance, privileges are appended to a list and returned
def privileges(balance: int):
    privilegesList = []
    if balance < 3:
        return ['None']
    if balance >= 3:
        privilegesList.append('Excursions')
    if balance >= 5:
        privilegesList.append('Book burrowing')
    if balance >= 7:
        privilegesList.append('School camp')
    if balance >= 10:
        privilegesList.append('Mobile phone access')
    return privilegesList

# Define the base student class that each student instance builds off
class Student:
    def __init__(self, studentId: str, firstName: str, surname:str, initialBalance: int):
        self._studentId = studentId
        self._firstName = firstName
        self._surname = surname
        self._balance = initialBalance
        self._privileges = privileges(self._balance)

    def __str__(self): # will run when the instance (not a property of the instance) is called, rather than python returning a weird code
        return f"{self._firstName} {self._surname}, {self._studentId}, {self._balance}, {self._privileges}"

    def changeBalance(self, change: int):
        print(f'Changing {self._firstName}\'s balance by +{change}') if change > 0 else print(f'Changing {self._firstName}\'s balance by {change}')
        self._balance += change
        self._privileges = privileges(self._balance)
        print(f'{self._firstName}\'s current balance is now {self._balance}. {self._firstName} has access to {self._privileges}')

    def printBalance(self):
        print(f'{self._firstName}\'s current balance is: {self._balance}')

    def get_balance(self):
        return self._balance
    
    def get_firstName(self):
        return self._firstName

    def get_surname(self):
        return self._surname
    
    def set_firstName(self, newName: str):
        self._firstName = newName

    def set_surname(self, newName: str):
        self._surname = newName

    def get_studentId(self):
        return self._studentId

    def set_studentId(self, newId: str):
        self._studentId = newId

    def get_privileges(self):
        return self._privileges

    # Creates properties using the above defined getters and setters for each object 
    # (or occasionally just the setter, if no getter is present/works elsewhere)
    firstName = property(get_firstName, set_firstName)
    surname = property(get_surname, set_surname)
    studentId = property(get_studentId, set_studentId)
    balance = property(get_balance)
    privileges = property(get_privileges)

while True:
    function = str(input('What would you like to do (enter a number)?\n1. Create a new student\n2. Access or edit student details\n3. Print student list\n4. Save the current data to a file\n5. Load data from the file\n6. Quit\n'))
    # Create a new student
    if function == '1':
        try:
            firstName = str(input('What do you want this students first name to be? ')).title()
            if not firstName: # check that the user entered any value at all (if no value is present, firstName will equate to 'falsy')
                raise ValueError() 
            surname = str(input('What do you want this students surname to be? ')).title()
            if not surname:
                raise ValueError()
            studentId = str(input('What do you want this students id to be? ')).upper()
            if not studentId:
                raise ValueError()
            if studentId in studentList.keys(): # check for duplicate ids
                raise TypeError("Duplicate ID")
            initialBalance = int(input('What do you want this students initial balance to be? '))
            if not initialBalance:
                raise ValueError()

            studentList[studentId] = Student(studentId, firstName, surname, initialBalance)
            print(f'{studentList[studentId].firstName} {studentList[studentId].surname} has been created with an initial balance of {studentList[studentId].balance} and id of {studentList[studentId].studentId}')
            print('')
        # any errors, either user defined, or the general exception to catch anything else and keep it running
        except TypeError as e:
            print(f"Uh oh, that ID already exists. You have been returned to the main menu.")
        except ValueError as e:
            print(f"Uh oh, a response was invalid. You have been returned to the main menu.")
        except Exception as e:
            print(f"Uh oh, something went wrong. You have been returned to the main menu. (Error: \"{e}\")")
    # Access student details
    elif function == '2':
        try:
            index = str(input('What student ID would you like to access (enter an existing ID): ')).upper()
            print(f"Name: {studentList[index].firstName} {studentList[index].surname}")
            print(f"Student ID: {studentList[index].studentId}")
            print(f"Balance: {studentList[index].balance}")
            print(f"Privileges: {studentList[index].privileges}")

            option = str(input('What would you like to change (enter a number)?\n1. Student name\n2. Student Id\n3. Change student balance\n4. Delete the current student\n5. Return to the home screen\n')).lower()
            # Change student name
            if option == '1':
                newFirst = str(input('Enter the new student first name: '))
                if not newFirst:
                    raise ValueError()
                newSur = str(input('Enter the new student surname: '))
                if not newSur:
                    raise ValueError()
                studentList[index].firstName = newFirst
                studentList[index].surname = newSur
                print(f'The students new name is: {studentList[index].firstName} {studentList[index].surname}')
            # Change student id
            elif option == '2':
                newId = str(input('Enter the new student ID (do not enter an existing ID): ')).upper()
                if newId in studentList.keys(): # confirm w/ user override if duplicate exists
                    confirmation = str(input(f'You are about to override student "{studentList[newId].firstName} {studentList[newId].surname}". Are you sure you want to do this? (y for yes/n for no) ')).lower()
                    if confirmation in ['y', 'yes', 'ye']:
                        pass
                    else:
                        print('You have been returned to the main menu, with no changes saved.')
                        continue
                elif newId == index:
                    print('You cannot change the student ID to their preexisting ID')
                    continue
                # Swap the position in the dictionary as well as the ID in the instance
                studentList[newId] = studentList[index]
                studentList[newId].studentId = newId
                studentList.pop(index)
                print(f'The students new ID is: {studentList[newId].studentId}')
            # Change student balance
            elif option == '3':
                change = int(input('Enter a number to change the balance by (enter a positive number to increase, or negative to decrease): '))
                if change == 0:
                    print('Nothing has been altered.')
                    continue
                studentList[index].changeBalance(change)
            # Delete student
            elif option == '4':
                print(f'{studentList[index].firstName} has been deleted')
                del studentList[index]
            # Exit
            elif option == '5':
                print("Returning to the home screen")
                continue
        except ValueError as e:
            print(f"Uh oh, that response was invalid. You have been returned to the main menu.")
        except KeyError as e:
            print(f"Uh oh, that ID doesn't currently exist. You have been returned to the main menu.")
        except TypeError as e:
            print(f"Uh oh, the value you entered is out of range. You have been returned to the main menu.")
        except Exception as e:
            print(f"Uh oh, something went wrong. You have been returned to the main menu. (Error: \"{e}\")")
    # Print all students    
    elif function == '3':
        count = 0
        if not studentList:
            print('There are no students in the student list.')
            continue
        for student in studentList:
            count += 1
            print(f"STUDENT {str(count)}\nStudent ID: {studentList[student].studentId}\nName: {studentList[student].firstName} {studentList[student].surname}\nBalance: {studentList[student].balance}\nPrivileges: {studentList[student].privileges}\n")
    # Save the data to a file 
    elif function == '4':
        try:
            saveDir = str(input('Please enter a directory to save the file to: '))
            saveDir = saveDir + '\\saveFile.csv' # need to append \saveFile on the end to create the file
            if exists(saveDir):
                confirmation = str(input('That file already exists. Are you sure you want to override it? (press enter if true, otherwise press any key and enter)'))
                    # cofnrim that overriing a file was the initial intention
                if not confirmation:
                    print('Overriding save file data...')
                if confirmation:
                    print('You have been returned to the main menu. Please try saving again, this time inputting a different directory.')
                    continue
            with open(saveDir, 'w', encoding='UTF8', newline='') as f: # open a file with the csv module, but only hold it open for the time this block is in action
                for student in studentList:
                    # append all student details to a list and then write it to the csv file
                    details = []
                    details.append(studentList[student].firstName + ' ' + studentList[student].surname)
                    details.append(studentList[student].studentId)
                    details.append(studentList[student]._balance)
                    details.append(studentList[student]._privileges)
                    
                    writer = csv.writer(f)
                    writer.writerow(details)
        except ValueError as e:
            print(f"Uh oh, that response is invalid. You have been returned to the main menu.")
        except PermissionError as e:
            print(f"Uh oh, it looks like we don't have permission for that. You have been returned to the main menu.")
        except FileNotFoundError as e:
            print(f"Uh oh, we can't find that file. You have been returned to the main menu.")
        except Exception as e:
            print(f"Uh oh, something went wrong. You have been returned to the main menu. (Error: \"{e}\")")
    # Load the data from a file
    elif function == '5':
        confirmation = str(input("You are sure you want to load a new file? This will delete any progess not currently saved. (press enter if true, otherwise press any key and enter) "))
            # confirm that shutting down without saving is intentional
        if not confirmation:
            print('Overriding data with save file...')
        if confirmation:
            print('You have been returned to the main menu. Please save your data before attempting to load.')
            continue
        try:
            loadDir = str(input('Please enter a directory to load the file from: '))
            loadDir = loadDir + '\\saveFile.csv'
            with open(loadDir, 'r', encoding='UTF8', newline='') as f: # same as saveDir
                reader = list(csv.reader(f)) # create a list using the information in the document
                count = 0
                for row in reader: # for each 'row' (nested list) in the reader list
                    # create a new student in the list with information from the sale file
                    names = reader[count][0].split()
                    print(names)
                    studentList[str(reader[count][1])] = Student(str(reader[count][1]), names[0], names[1], int(reader[count][2]))
                    count += 1
        except ValueError as e:
            print(f"Uh oh, that response is invalid. You have been returned to the main menu.")
        except PermissionError as e:
            print(f"Uh oh, it looks like we don't have permission for that. You have been returned to the main menu.")
        except FileNotFoundError as e:
            print(f"Uh oh, we can't find that file. You have been returned to the main menu.")
        except Exception as e:
            print(f"Uh oh, something went wrong. You have been returned to the main menu. (Error: \"{e}\")")
    elif function == '6':
        confirmation = str(input('Uh oh, saving is not automatic. Have you already saved your program? (press enter if true, otherwise press any key and enter) ')) 
            # confirm that shutting down without saving is intentional
        if not confirmation:
            print('Thank you for using CIGSA. Shutting down...')
            break
        else:
            print('You are being returned to the main menu. Please save your progress and then quit.')
            continue