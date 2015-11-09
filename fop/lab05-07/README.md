#  LIBRARY
**Author: Cosmin Rusu**
**November 2015**

## Problem statement
Write an application for a book library. The application will store:  
* Books: id, title, description, author  
* Create an application which allows the user to:  
* Manage the list of books and clients.  
* Add, remove, update and list books and clients.  
* Search for a book; search for a client.  
* Rent/return book.  
* Reporting. The reporting part of the application will allow generating a list of clients or books (maybe of certain type) ordered based on the user preference. Examples: most rented book,
most active clients, clients with rented books ordered alphabetically, by number of rents, by
year of publishing, etc.   
* Unlimited undo/redo functionality. Each step will undo/redo the previous operation that modified the data structure.    

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

|Step   |User                     |Program                                                                                                                                                            |Description                                                                                        |
|-------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|1      |                                           |Type a command. Press 'help' for the available commands:                                                                                  |                                                                                                   |
|2      |`help`                                     |                                                                                                                                                                   |The user asks for help                                                                             |
|3      |                                           |Here are the commands:<br>`addBook|Title of the book|Description of the book|Author of the book`<br>`addClient|CNP|Name of the client`<br>`removeBook|Id` - removes the specific book<br>`removeClient|CNP` - removes the client with the given CNP<br>`updateCnp|ACTUAL_CNP|NEW_CNP` - update the cnp of a person<br>`updateName|CNP|NEW_NAME` - update the name of a person<br>`updateTitle|ID_BOOK|NEW_TITLE` - update the title of a specific book<br>`updateDescription|ID_BOOK|NEW_DESC` - update the description of a specific book<br>`updateAuthor|ID_BOOK|NEW_AUTH` - update the author of a specific book<br>`listBooks` - print all books<br>`listClients` - print all clients<br>`undo` - undo the last operation<br>`redo` - reverse of undo<br>`save` - save current library state<br>`exit` - save and exit                                                                                            |The programs shows the available commands                                                          |
|4      |`addBook|Introduction to Algorithms|The Bible for every computer scientist|Thomas H Cormen`                  |                                                                                                                                                                   |The user adds a new Book with the specified properties |Title|Description|Author                      |
|5      |`addBook|Learning Python - 3rd Edition|A very nice book for learning Python from scratch|Mark Lutz`   |                                                                                                                                                                   |Same as above       |
|6      |`addClient|1960715060015|Rusu Cosmin`                                     |                                                                                                                                                                   |The user inserts a new Client                                       |
|7      |`addClient|2960715060015|Rusu Raluca`                                     |                                                                                                                                                                   |The user inserts a new Client                                       |
|8      |`list`                                     |                                                                                                                                                                   |The app shows the user all the transaction he asked for                                            |
|9      |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca<br>CNP: 2960715060015                                                   |The app shows the user all the books and the clients                            |
|10     |`updateName|1960715060015|Rusu Cosmin-Ionut`                  |                                                                                                                                                                   |Update the Name of a Client|
|11     |`updateCnt|2960715060015|2020715060015`                                     |                                                                                                                                                                   |Update the CNP of a client|
|12     |`list`                                     |                                                                                                                                                                   |The app shows the user all the transaction he asked for                                            |
|13     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca<br>CNP: 2020715060015                               |The app shows the user all the books and the clients                                 |
|15     |`list`                                     |                                                                                                                                                                   |                                            |
|14     |`removeClient|2020715060015`                                |                                                                                                                                                                   |The user removes a client with a specific CNP                           |
|16     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br>                                                         |The app shows the user all the books and the clients                             |
|17     |`removeBook|1`                             |                               |The user remove the book with the Id = 1                                           |
|18     |`list`                                     |                                                                                                                                                                   |  |
|19     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br>                                                         |The app shows the user all the books and the clients|
|20     |`updateDescription|0|The best book on algorithms and data structures`             |                                                                                                                                                                   |The user updates the description of a specific Book|
|21     |`list`                                     |                                                                                                                                                                   |                                           |
|22     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The best book on algorithms and data structures<br>Author: Thomas H Cormen<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015 |The app shows the user all the books and the clients|
|23     |`undo`                                     |                                                                                                                                                                   |Undo the last performed operation        |
|24     |`undo`                                     |                                                                                                                                                                   |Undo the last performed operation|
|25     |`list`                                     |                                                                                                                                                                   |List                                               |
|26     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015                                                         |The app shows the user all the book and the clients|
|27     |`redo`                                     |                                                                                                                                                                   |Redo           |
|28     |`list`                                     |                                                                                                                                                                   |List                                        |
|29     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015                                                    |The program gives the user the requested information                                               |
|30     |`exit`                                     |                                                                                                                                                                   |The user wants to exit the application                                                             |
|31     |                                           |Exiting...                                                                                                                                                         |                                                                                                   |



### Iteration 2

#  LIBRARY
**Author: Cosmin Rusu**
**November 2015**

## Problem statement
Write an application for a book library. The application will store:  
* Books: id, title, description, author  
* Create an application which allows the user to:  
* Manage the list of books and clients.  
* Add, remove, update and list books and clients.  
* Search for a book; search for a client.  
* Rent/return book.  
* Reporting. The reporting part of the application will allow generating a list of clients or books (maybe of certain type) ordered based on the user preference. Examples: most rented book,
most active clients, clients with rented books ordered alphabetically, by number of rents, by
year of publishing, etc.   
* Unlimited undo/redo functionality. Each step will undo/redo the previous operation that modified the data structure.    

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

|Step   |User                     |Program                                                                                                                                                            |Description                                                                                        |
|-------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|1      |                                           |Type a command. Press 'help' for the available commands:                                                                                  |                                                                                                   |
|2      |`help`                                     |                                                                                                                                                                   |The user asks for help                                                                             |
|3      |                                           |Here are the commands:<br>`addBook|Title of the book|Description of the book|Author of the book`<br>`addClient|CNP|Name of the client`<br>`removeBook|Id` - removes the specific book<br>`removeClient|CNP` - removes the client with the given CNP<br>`updateCnp|ACTUAL_CNP|NEW_CNP` - update the cnp of a person<br>`updateName|CNP|NEW_NAME` - update the name of a person<br>`updateTitle|ID_BOOK|NEW_TITLE` - update the title of a specific book<br>`updateDescription|ID_BOOK|NEW_DESC` - update the description of a specific book<br>`updateAuthor|ID_BOOK|NEW_AUTH` - update the author of a specific book<br>`listBooks` - print all books<br>`listClients` - print all clients<br>`undo` - undo the last operation<br>`redo` - reverse of undo<br>`save` - save current library state<br>`exit` - save and exit                                                                                            |The programs shows the available commands                                                          |
|4      |`addBook|Introduction to Algorithms|The Bible for every computer scientist|Thomas H Cormen`                  |                                                                                                                                                                   |The user adds a new Book with the specified properties |Title|Description|Author                      |
|5      |`addBook|Learning Python - 3rd Edition|A very nice book for learning Python from scratch|Mark Lutz`   |                                                                                                                                                                   |Same as above       |
|6      |`addClient|1960715060015|Rusu Cosmin`                                     |                                                                                                                                                                   |The user inserts a new Client                                       |
|7      |`addClient|2960715060015|Rusu Raluca`                                     |                                                                                                                                                                   |The user inserts a new Client                                       |
|8      |`list`                                     |                                                                                                                                                                   |The app shows the user all the transaction he asked for                                            |
|9      |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca<br>CNP: 2960715060015                                                   |The app shows the user all the books and the clients                            |
|10     |`updateName|1960715060015|Rusu Cosmin-Ionut`                  |                                                                                                                                                                   |Update the Name of a Client|
|11     |`updateCnp|2960715060015|2020715060015`                                     |                                                                                                                                                                   |Update the CNP of a client|
|12     |`list`                                     |                                                                                                                                                                   |The app shows the user all the transaction he asked for                                            |
|13     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca<br>CNP: 2020715060015                               |The app shows the user all the books and the clients                                 |
|15     |`list`                                     |                                                                                                                                                                   |                                            |
|14     |`removeClient|2020715060015`                                |                                                                                                                                                                   |The user removes a client with a specific CNP                           |
|16     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br>                                                         |The app shows the user all the books and the clients                             |
|17     |`removeBook|1`                             |                               |The user remove the book with the Id = 1                                           |
|18     |`list`                                     |                                                                                                                                                                   |  |
|19     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br>                                                         |The app shows the user all the books and the clients|
|20     |`updateDescription|0|The best book on algorithms and data structures`             |                                                                                                                                                                   |The user updates the description of a specific Book|
|21     |`list`                                     |                                                                                                                                                                   |                                           |
|22     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The best book on algorithms and data structures<br>Author: Thomas H Cormen<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015 |The app shows the user all the books and the clients|
|23     |`undo`                                     |                                                                                                                                                                   |Undo the last performed operation        |
|24     |`undo`                                     |                                                                                                                                                                   |Undo the last performed operation|
|25     |`list`                                     |                                                                                                                                                                   |List                                               |
|26     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Learning Python - 3rd Edition<br>Description: A very nice book for learning Python from scratch<br>Author: Mark Lutz<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015                                                         |The app shows the user all the book and the clients|
|27     |`redo`                                     |                                                                                                                                                                   |Redo           |
|28     |`list`                                     |                                                                                                                                                                   |List                                        |
|29     |                                           |Book #0:<br>Title: Introduction to algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015                                                    |The program gives the user the requested information                                               |
|30     |`addClient|2960715060015|Rusu Raluca-Rusu` |  |The user adds another client.|
|31     |`addBook|Dorian Gray's Portret|Modern novel|Oscar Wilde`| | The user adds another book.|
|32     |`addBook|The basis of Math|A nice book on Math for students|Dorin Andrica`| |THe user adds another book.|
|33     |`list` | | The user wants to see how the library looks like.|
|34     |   |Book #0:<br>Title: Introduction to Algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Dorian Gray's Portret<br>Description: Modern novel<br>Author: Oscar Wilde<br><br><br>Book #2:<br>Title: The basis of Math<br>Description: A nice book on Math for students<br>Author: Dorin Andrica<br><br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca-Rusu<br>CNP: 2960715060015   |   |
|35     |
|36     |`rentBook|1960715060015|0` |      |Renting Introduction to Algorithms to Rusu Cosmin|
|37     |`rentBook|2960715060015|1` |      |Renting Oscars Wildes's novel to Rusu Raluca|
|38     |`list`|    |List library|
|39     |       | <br>Book #0:<br>Title: Introduction to Algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Dorian Gray's Portret<br>Description: Modern novel<br>Author: Oscar Wilde<br><br><br>Book #2:<br>Title: The basis of Math<br>Description: A nice book on Math for students<br>Author: Dorin Andrica<br><br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca-Rusu<br>CNP: 2960715060015<br><br>Client Rusu Cosmin-Ionut has the book #0 with the Title: Introduction to Algorithms<br><br>Client Rusu Raluca-Rusu has the book #1 with the Title: Dorian Gray's Portret | |
|40     |`returnBook|2960715060015|1` |     |A user return a book|
|41     |`list`|    |List library|
|42     |       | <br>Book #0:<br>Title: Introduction to Algorithms<br>Description: The Bible for every computer scientist<br>Author: Thomas H Cormen<br><br><br>Book #1:<br>Title: Dorian Gray's Portret<br>Description: Modern novel<br>Author: Oscar Wilde<br><br><br>Book #2:<br>Title: The basis of Math<br>Description: A nice book on Math for students<br>Author: Dorin Andrica<br><br><br>Client Name: Rusu Cosmin-Ionut<br>CNP: 1960715060015<br><br>Client Name: Rusu Raluca-Rusu<br>CNP: 2960715060015<br><br>Client Rusu Cosmin-Ionut has the book #0 with the Title: Introduction to Algorithms| |
|43     |`exit`                                     |                                                                                                                                                                   |The user wants to exit the application                                                             |
|44     |                                           |Exiting...                                                                                                                                                         |                                                                                                   |