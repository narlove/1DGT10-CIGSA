# CIGSA
DATE: 07/04/2022 (original Python project) || 01/01/2023 (updated Node.js project)
## Description
This project was created under the context of a commission from a school who needed a good standing system. This is reflected in the name, 
which is an abbreviated version of Cactus Island (the school name) Good Standing Application. 
Because the project was originally written in Python, as a challenge for myself I attempted to update it with my increased programming knowledge and understanding of JavaScript and Node.js. Hence, the following sections will be split into two parts, one for the outdated Python and for the newer JavaScript. Both languages versions can be accessed in the repository, however, Python is in './python-version/' while the Node.js files litter the source directory.
## Functions (Python)
The program is able to perform the following functions:
 - Create a student profile and save information to it, such as their name and student ID, their good standing points or the rewards they have unlocked at their
current standing.
 - Read a student profile and return the data associated with it
 - Edit a student profile
 - Print a brief overview of each student entered into the system
 - Save the data to a excel file so that information can remain between program restarts
 - Load the data from the excel spreadsheet to be able to be edited in the program
## Functions (Node.js)
The program was instead written into an API. The API can only be accessed by making a call to a route on the localhost. The API can perform the following functions:
 - Automatically calculate the required privileges a student should have, based on their balance
 - Return a list of all of the students upon a GET request to '/api/students'
 - Return a specific student profile through an ID lookup, upon a GET request to '/api/students/idlookup/:id'
 - Return a specific student profile through a name lookup, upon a GET request to '/api/students/namelookup/:name'
 - Add a new student's data upon a POST request to '/api/students'.
 - Update student data upon a PUT request to '/api/students/idlookup/:id'. This function is only avaliable for the ID lookup
 - Delete a student's data upon a DELETE request to 'api/students/idlookup/:id'. This function is only avaliable for the ID lookup
 - Automatically save the cloud data to the localhost's JSON file upon any POST, PUT or DELETE request
 - Automatically load data from the localhost's JSON file when the server is started
## Quick overview
 - This project was originally created as an assignment for my digital technologies class. It was later updated as a personal project
 - The original was written in Python, while the updated was written in JavaScript
 - The python module cvs is used to save the data to an excel document for saving and loading purposes. The JavaScript version writes to a JSON file instead, utilising the fs (file system) module
 - The program has remained entirely text based and without a UI even after the update
 - Error handling is specifically built into the Python project, with less of a focus in the JavaScript project.
 - Unlike the Python project, the JavaScript project 
