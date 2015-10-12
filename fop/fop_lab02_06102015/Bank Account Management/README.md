#  BANK ACCOUNT MANAGEMENT

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
1             | Add a new transaction into the list.				    | * add X,Y,description * insert X, Y, in/out, * description>
2             | Modify transactions from the list                       | * remove X * remove from X to Y * remove in/out * replace X, in/out, description with Y
3             | Write the transactions having different properties.     | * greater than X * less than X before Y * all in/out * list * balance X
4             | Obtain different characteristics of transactions        | * avg X Y * min X Y * mul X Y Z
5             | Filter transactions.                                    | * filter mul X * filter greater X
6             | Undo the last operation.                                | * undo

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
            <td>`help`</td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>3</td>
            <td></td>
			<td>Here are all the command you can use:<br>
			* list - displays the list of all transactions
			* add X,Y,description - adds to the current day an in/out transaction of X RON with the given description
			* insert X, Y, in/out, description – inserts in day X an in/out transaction of Y RON with the given description
			* remove X – removes all the transactions from day X
			* remove from X to Y – removes all the transactions from day X until day Y
			* remove in/out – removes all the in/out transactions from the current month
			* replace X, in/out, description with Y – replaces the amount for the in/out transaction having the specified description from day X with Y RON
			* exit - to quit the application
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
