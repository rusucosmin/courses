#  BANK ACCOUNT MANAGEMENT
Author: Cosmin Rusu
Date: 13 October 2015

## Problem statement
John wants to **manage his bank account**. In order to complete this task, John needs an application to
store, for a certain month, all the banking transactions which were performed on his account. Each
transaction will be stored in the application through the following elements: day (of the month in
which the transaction was made), amount of money transferred into/from the account, the type of the
transaction (into the account – in or from the account - out), and description of the transaction. Please
help John to create an application in order to repeatedly execute the following functionalities (each
functionality is exemplified):

## Feature list

Feature no.   | Description                                             | Commands
:------------:|:-------------------------------------------------------:|:----------------------------------------------------------------------
1             | Add a new transaction into the list.				    | <ul><li>add X,Y,description</li><li>insert X,Y,in/out,description</li></ul>
2             | Modify transactions from the list                       | <ul><li>remove X</li><li>remove from X to Y</li><li>remove in/out</li><li>replace X, in/out, description with Y</li></ul>
3             | Write the transactions having different properties.     | <ul><li>greater than X</li><li>less than X before Y</li><li>all in/out</li><li>balance X</li></ul>
4             | Obtain different characteristics of transactions        | <ul><li>sum in/out</li><li>max in/out X</li><li>asc sort day</li><li>desc sort type</li></ul>
5             | Filter transactions.                                    | <ul><li>filter in/out</li><li>filter in/out X</li></ul>
6             | Undo the last operation.                                | <ul><li>undo</li></ul>

## Iteration plan

Iteration no. | Planned features
:------------:|:----------------
1             | 1, 2
2             | 3, 4
3             | 5, 6

## Running scenarios

### Iteration 1

<table>
    <thead>
        <tr>
            <th>Step</th>
            <th>User</th>
            <th>Program</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td></td>
            <td>Starting application<br>
                Hello. Please insert a command. Type 'help' to show menu
            </td>
            <td>The application started.<br>
				The user is asked to input commands.
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td>help</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>3</td>
            <td></td>
			<td>Here are all the command you can use:<br>
			<ul>
		<li> list - displays the list of all transactions </li>
		<li> add X,Y,description - adds to the current day an in/out transaction of X RON with the given description</li>
		<li>insert X, Y, in/out, description – inserts in day X an in/out transaction of Y RON with the given description</li>
		<li>remove X – removes all the transactions from day X</li>
		<li>remove from X to Y – removes all the transactions from day X until day Y</li>
		<li>remove in/out – removes all the in/out transactions from the current month</li>
		<li>replace X, in/out, description with Y – replaces the amount for the in/out transaction having the specified description from day X with Y RON</li>
		<li>exit - to quit the application</li>
			</ul>
			</td>
            <td>Application show all the commands that can be made.</td>
        </tr>
        <tr>
            <td>4</td>
            <td>add 100,in,Added 100 LEI to the account</td>
            <td></td>
            <td>User adds an in transaction today, with 100 LEI and the given description.</td>
        </tr>
        <tr>
            <td>5</td>
            <td>list</td>
            <td></td>
            <td>User request the list of all the available transactions.</td>
        </tr>
        <tr>
			<td>6</td>
            <td></td>
			<td>These are the stored transactions:<
				* 1. 12, 100, in, Added 100 LEI to the account
            <td>User inserts participant with score 42 at the beginning.</td>
        </tr>
        <tr>
            <td>7</td>
            <td>exit</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>8</td>
            <td></td>
            <td>
                Exiting
            </td>
            <td>The application is closing.</td>
        </tr>
    </tbody>
</table>

## Work items/tasks

|Options |Description|
|--------|-----------|
|   T1   |Implement user interface                                  |
|   T2   |Display menu              	 							|
|   T3   |Display transactions          							|
|   T4   |Test whether the commands are correct          			|
|   T5   |Test whether the command's arguments are valid 			|
|   T6   |Implement the add transaction functionality          		|
|   T7   |Implement the insert transaction functionality         	|
|   T8   |Implement the remove transaction functionality            |
|   T9   |Implement the replace transaction functionality           |
|   T10  |Implement the filter by properies functionality           |
|   T11  |Implement the get balance function                        |
|   T12  |Implement the get sum function                            |
|   T13  |Implement the get max function                            |
|   T14  |Implement the get sort function                           |

### Iteration 2
|Step   |User                                   |Program                             |Description                                           |
|-------|---------------------------------------|------------------------------------|------------------------------------------------------|
|1      |salut                                  |           |the user first started the app, does not know what is doing            |
|2      |                                       |command not recognized           |tells the user that the command do not exist, reminds him about the 'help' command           |
|3      |help                                   |shows the list of the whole available commands (shown in the ui module)           |the user asks for help           |
|4      |                                       |shows the list of the whole available commands (shown in the ui module)           |the programs shows the available commands|
|5      |add 100,out,bought milk                | |the user inserts a 100 RON out transaction with the 'bought milk' description|
|6      |add 10000,out,money for the university | |the user inserts a 10000 RON out transaction with the 'money for the university' description|
|7      |list                                   |           |the user wans to have the whole transaction list printed           |
|8      |                                       |These are the stored transactions:<br>1. 20, 100, in, bought milk<br>2. 20, 10000, out, money for the university        | The app shows the user all the transaction stored right now in the list   |
|9      |insert 15,200,in,groceries             |           |The user insert a 200RON-out transaction on day 15 with the description 'groceries'  |
|10     |greater than 100                       | These are the transactions:<br>1. 20, 100, out, bought milk<br>2. 20, 10000, out, money for the university<br>3. 15, 200, in, groceries      |  The app shows the user all the transaction he asked for         |
|11     |less than 200 before 20                | | The user asks for all the transaction less than 100 before the 20th day of the week|
|12     |                                       |These are the transactions:<br>1. 20, 100, out, bought milk<br>2. 15, 200, in, groceries       |      The app shows the user all the transaction he asked for     |
|13     |all in                                 |           | The user asks all the in transaction          |
|14     |                                       |   These are the transactions:<br>1. 15, 200, in, groceries        |   :))The program brings the date the user wants        |
|15     |all out                                |           |    The user asks for all the out transaction       |
|16     |                                       |      These are the transactions:<br>1. 20, 100, out, bought milk<br>2. 20, 10000, out, money for the university     |   The program brings the information        |
|17     |balance 15                             |           |The users asks to compute the balance           |
|18     |                                       |      Balance on the given day was  200     |           |
|19     |balance 20                             |           |The users asks to compute the balance          |
|20     |                                       |      Balance on the given day was  -9900     |           |
|21     |sum in                                 |           |The users tries different command       |
|22     |                                       |      200     |           |
|23     |sum out                                |           |           |
|24     |                                       |10100           |           |
|25     |max out day                            |           |           |
|26     |                                       |     20      |           |
|27     |max in day                             |           |           |
|28     |                                       |     15      |           |
|29     |asc sort day                           |        |           |
|30     |                                       |     These are the transactions:<br>1. 20, 100, out, bought milk<br>2. 15, 200, in, groceries<br>3. 20, 10000, out, money for the university         |           |
|31     |desc sort in                           |           |           |
|32     |                                       |      These are the transactions:<br>1. 15, 200, in, groceries     |           |
|33     |desc sort out                          |           |           |
|34     |                           |           |    These are the transactions:<br>1. 20, 10000, out, money for the university<br>2. 20, 100, out, bought milk       |
|35     |exit                                   |               | The user wants to exit the application |
|36     |                                       |Exiting...| |