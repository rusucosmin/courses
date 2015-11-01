#  LIBRARY
**Author: Cosmin Rusu**
**November 2015**

## Problem statement
Write an application for a book library. The application will store:
*Books: <id>, <title>, <description>, <author>.
*Clients: <clientId>, <name>, <CNP>.
Create an application which allows the user to:
*Manage the list of books and clients.
*Add, remove, update and list books and clients.
*Search for a book; search for a client.
*Rent/return book.
*Reporting. The reporting part of the application will allow generating a list of clients or books (maybe of certain type) ordered based on the user preference. Examples: most rented book,
most active clients, clients with rented books ordered alphabetically, by number of rents, by
year of publishing, etc.
*Unlimited undo/redo functionality. Each step will undo/redo the previous operation that modified the data structure.

## Feature list
|Feature no.    | Description                                           | Commands                                                                                                                              |
|---------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
|1              |*Add, remove, update and list books and clients.       |<ul><li>`addBook`</li><li>`addClient`</li><li>`removeBook`</li><li>`removeClient`</li><li>`updateCnp`</li><li>`updateName`</li><li>`updateTitle`</li><li>`updateDescription`</li><li>`updateAuthor`</li><li>`listBooks`</li><li>`listClients`</li></ul>                                                        |
|2              |*Search for a book; search for a client.               |<ul><li>`searchBook`</li><li>`searchClient`</li></ul>      |
|3              |*Rent/return book.                                     |<ul><li>`rent`</li><li>`return`</li></ul>                             |
|4              |*Reporting.                                            |<ul><li>`report`</li></ul>                                  |
|5              |*Unlimited undo/redo functionality                     |<ul><li>`undo`</li><li>`redo`</li></ul>                                                                            |
|6              |*Save the current state of the libary in a txt file    |<ul><li>'save'</li></ul> 

## Iteration plan
Iteration no. | Planned features
:------------:|:----------------
1             | 1, 2, 5, 6
2             | 3
3             | 4

## Work items/tasks
|Options |Description                                               |
|--------|----------------------------------------------------------|
|   T1   |Implement user interface                                  |
|   T2   |Display menu                                              |
|   T3   |Display books                                             |
|   T4   |Display clients                                           |
|   T5   |Add books                                                 |
|   T6   |Add clients                                               |
|   T7   |Update clients - name and cnp                             |
|   T8   |Update books - title, description and author              |
|   T9   |Search client - by cnp, by name                           |
|   T10  |Search book - by id, by title, by description, by author  |
|   T11  |Rent a book                                               |
|   T12  |Return a book                                             |
|   T13  |Undo the last operation                                   |
|   T14  |Redo                                                      |
|   T15  |Save the current state                                    |
|   T16  |Reporting                                                 |

## Running scenarios

### Iteration 1

|Step   |User                                       |Program                                                                                                                                                            |Description                                                                                        |
|-------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|1      |                                           |Starting application.<br>Hello. Please insert a command. Type 'help' to show menu                                                                                  |                                                                                                   |
|2      |`help`                                     |                                                                                                                                                                   |The user asks for help                                                                             |
|3      |                                           |Shows the list of the whole available commands (shown in the ui module)                                                                                            |The programs shows the available commands                                                          |
|4      |`add 100,out,Bought Milk`                  |                                                                                                                                                                   |The user inserts a 100 RON out transaction with the 'Bought Milk' description                      |
|5      |`add 10000,out,Money for the University`   |                                                                                                                                                                   |The user inserts a 10000 RON out transaction with the 'Money for the University' description       |
|6      |`list`                                     |                                                                                                                                                                   |The user wants to have the whole transaction list printed                                          |
|7      |                                           |These are the stored transactions:<br>1. 20, 100, in, Bought Milk<br>2. 20, 10000, out, Money for the University                                                   |The app shows the user all the transaction stored right now in the list                            |
|8      |`insert 15,200,in,Salary`                  |                                                                                                                                                                   |The user insert a 200RON-out transaction on day 15 with the description 'Salary'                   |
|9      |`list`                                     |                                                                                                                                                                   |The app shows the user all the transaction he asked for                                            |
|10     |                                           |These are the transactions:<br>1. 20, 100, out, Bought Milk<br>2. 20, 10000, out, Money for the University<br>3. 15, 200, in, Salary                               |The app shows the user all the transaction he asked for                                            |
|11     |`remove 15`                                |                                                                                                                                                                   |The user wants to remove all the transaction for the day 15 of the month                           |
|12     |`list`                                     |                                                                                                                                                                   |The app shows the user all the transaction he asked for                                            |
|13     |                                           |These are the transactions:<br>1. 20, 100, out, Bought Milk<br>2. 20, 10000, out, Money for the University                                                         |The app shows the user all the transaction he asked for                                            |
|14     |                                           |These are the transactions:<br>1. 20, 100, out, bought milk<br>2. 15, 200, in, groceries                                                                           |The app shows the user all the transaction he asked for                                            |
|15     |`insert 15,350,in,Scholarship`             |                                                                                                                                                                   |The user inserts an in transaction with 350RON which is the monthly university scholarship         |
|16     |`insert 16,1000,in,Teaching classes`       |                                                                                                                                                                   |The users insert a in transaction with 1000RON.                                                    |
|17     |`list`                                     |                                                                                                                                                                   |The user wants to know which are the stored transactions                                           |
|18     |                                           |1. 26, 100, out, Bought Milk<br>2. 26, 10000, out, Money for the University<br>3. 15, 350, in, Scholarship<br>4. 16, 1000, in, Teaching classes                    |The program gives the user the requested information                                               |
|19     |`remove from 15 to 16`                     |                                                                                                                                                                   |The user ask the program to remove all the transactions from day 15 to day 16 of the month         |
|20     |`list`                                     |                                                                                                                                                                   |The program gives the user the requested information                                               |
|21     |                                           |These are the transactions:<br>1. 26, 100, out, Bought Milk<br>2. 26, 10000, out, Money for the University                                                         |The program gives the user the requested information                                               |
|22     |`all out`                                  |                                                                                                                                                                   |The user ask the program to print all the out transactions                                         |
|23     |                                           |Here is the result of the query:<br>1. 26, 250, out, Bought Milk<br>2. 26, 10000, out, Money for the University                                                    |The program gives the user the requested information                                               |
|24     |                                           |These are the transactions:<br>1. 26, 250, out, Bought Milk<br>2. 26, 10000, out, Money for the University                                                         |The program gives the user the requested information                                               |
|25     |`exit`                                     |                                                                                                                                                                   |The user wants to exit the application                                                             |
|26     |                                           |Exiting...                                                                                                                                                         |                                                                                                   |
