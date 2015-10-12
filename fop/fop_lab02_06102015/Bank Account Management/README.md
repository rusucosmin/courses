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
			 list - displays the list of all transactions <br>
			 add X,Y,description - adds to the current day an in/out transaction of X RON with the given description<br>
			 insert X, Y, in/out, description – inserts in day X an in/out transaction of Y RON with the given description<br>
			 remove X – removes all the transactions from day X<br>
			 remove from X to Y – removes all the transactions from day X until day Y<br>
			 remove in/out – removes all the in/out transactions from the current month<br>
			 replace X, in/out, description with Y – replaces the amount for the in/out transaction having the specified description from day X with Y RON<br>
			 exit - to quit the application<br>
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
