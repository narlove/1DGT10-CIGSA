// CIGSA in JS
// 01/01/2023
// Nathan | Dimqnd

const prompt = require('prompt-sync')({ sigint: true });
const express = require('express');

const api = require('./src/CIGSA-api');
const calculatePrivileges = api.calculatePrivileges;

let studentList = {};

class Student {
    constructor(studentId, firstName, surname, balance) {
        this._studentId = studentId;
        this._firstName = firstName;
        this._surname = surname;
        this._balance = balance;
        this._privileges = calculatePrivileges(this._balance);
    }

    get balance() {
        return this._balance;
    }

    set balance(change) {
        change > 0 ? console.log(`Changing ${this._firstName}'s balance by +${change}`) : 
            console.log(`Changing ${this._balance}'s balance by ${change}`);
        this._balance += change;
        this._privileges = calculatePrivileges(this._balance);
        console.log(`${this._firstName}'s balance is now ${this._balance}. ${this._firstName} has access to ${this._privileges.join(', ')}`);
    }

    logBalance() {
        console.log(`${this._firstName} has a balance of ${this._balance}, which allows them access to ${this._privileges.join(', ')}`);
    }

    get firstName() {
        return this._firstName;
    }

    set firstName(newName) {
        this._firstName = newName;
    }

    get surname() {
        return this._surname;
    }

    set surname(newName) {
        this._surname = newName;
    }

    get studentId() {
        return this._studentId;
    }

    set studentId(newId) {
        this._studentId = newId; 
    }

    get privileges() {
        return this._privileges;
    }
}

const app = express();
const PORT = 5000;

app.use(express.json());
app.use('/api', api);

app.listen(PORT, () => {
    console.log(`Listening on https://localhost:${PORT}`);
})