__author__ = 'cosmin'

import unittest
from model.book import Book
from model.client import Client
from model.command import Command
from model.loan import Loan

from model.exception import LibraryException
from controllers.LibraryController import LibraryController
from repository.LibraryRepository import LibraryRepository

class UnitTester(unittest.TestCase):
    '''
    Class to implement the unit test functions for the whole application.
    '''

    def testBook(self):
        '''
        Method to test the getter and the setter of the Book class
        '''
        book = Book(1, "Introduction to algorithms", "The Bible", "Thomas H Cormen")
        assert book.getId() == 1
        assert book.getTitle() == "Introduction to algorithms"
        assert book.getDescription() == "The Bible"
        assert book.getAuthor() == "Thomas H Cormen"
        book.setAuthor("Cosmin")
        assert book.getAuthor() == "Cosmin"
        book.setTitle("Title")
        assert book.getTitle() == "Title"
        book.setDescription("Descr")
        assert book.getDescription() == "Descr"

    def testClient(self):
        '''
        Method to test the getter and the setter of the Client class
        '''
        client = Client(1960715060015, "Rusu Cosmin-Ionut")
        assert client.getCnp() == 1960715060015
        assert client.getName() == "Rusu Cosmin-Ionut"
        client.setCnp(2960715060015)
        assert client.getCnp() == 2960715060015
        client.setName("Rusu Cosmin")
        assert client.getName() == "Rusu Cosmin"

    def testCommand(self):
        '''
        Method to test the getter and the setter of the Command class
        '''
        try:
            Command("addBook|||")
            assert False
        except LibraryException:
            pass

        try:
            Command("addBook|Title||")
            assert False
        except LibraryException:
            pass

        try:
            Command("addBook||Description|")
            assert False
        except LibraryException:
            pass

        try:
            Command("addBook|||Author")
            assert False
        except LibraryException:
            pass

        try:
            Command("addBook|Title|Description|")
            assert False
        except LibraryException:
            pass

        try:
            Command("addBook|Title||Author")
            assert False
        except LibraryException:
            pass

        try:
            Command("addBook||Description|Author")
            assert False
        except LibraryException:
            pass

        command = Command("addBook|Title|Description|Author")
        assert command.toAddBook(1) == Book(1, "Title",  "Description", "Author")

        try:
            Command("Cosmin")
            assert False
        except LibraryException:
            pass

        try:
            Command("addClient|1960715060015")
            assert False
        except LibraryException:
            pass

        try:
            command = Command("addClient|numarul25|Rusu Cosmin")
            command.toAddClient()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("removeBook|numarul25")
            command.toRemoveBook()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("removeBook|1|Title")
            command.toRemoveBook()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("removeClient|numarul25")
            command.toRemoveClient()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("removeClient")
            command.toRemoveClient()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("removeClient|1960715060|Rusu Cosmin")
            command.toRemoveClient()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateCnp|numarul25|newValue")
            command.toUpdateCnp()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateCnp|1960715060015|newValue")
            command.toUpdateCnp()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateCnp|numarul25|1960715060015")
            command.toUpdateCnp()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateCnp||")
            command.toUpdateCnp()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateCnp||1960715060015")
            command.toUpdateCnp()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateCnp|1960715060015|")
            command.toUpdateCnp()
            assert False
        except LibraryException:
            pass

        Command("updateCnp|2960715060015|1960715060015")

        try:
            command = Command("updateName|numarul25|newValue")
            command.toUpdateName()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateName||")
            command.toUpdateName()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateName||1960715060015")
            command.toUpdateName()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateName|1960715060015|")
            command.toUpdateName()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateTitle|numarul25|NewValue")
            command.toUpdateTitle()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateTitle||")
            command.toUpdateTitle()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateTitle||1960715060015")
            command.toUpdateTitle()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateTitle|1960715060015|")
            command.toUpdateTitle()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateTitle|numarul25|NewValue")
            command.toUpdateTitle()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateAuthor|numarul25|NewValue")
            command.toUpdateAuthor()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateAuthor||")
            command.toUpdateAuthor()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateAuthor||1960715060015")
            command.toUpdateAuthor()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateAuthor|1960715060015|")
            command.toUpdateAuthor()
            assert False
        except LibraryException:
            pass

        try:
            command = Command("updateAuthor|numarul25|NewValue")
            command.toUpdateAuthor()
            assert False
        except LibraryException:
            pass

        command = Command("addClient|1960715060015|Rusu Cosmin")
        assert command.toAddClient() == Client(1960715060015, "Rusu Cosmin")

    def testRunningScenarios(self):
        #Running scenario 1
        books = []
        clients = []
        testrepo = LibraryRepository(False)
        controller = LibraryController(testrepo)
        cmd = Command("addBook|Introduction to Algorithms|The Bible for every computer scientist|Thomas H Cormen")
        controller.addBook(cmd.toAddBook(0))
        books.append(cmd.toAddBook(0))
        cmd = Command("addBook|Learning Python - 3rd Edition|A very nice book for learning Python from scratch|Mark Lutz")
        controller.addBook(cmd.toAddBook(1))
        books.append(cmd.toAddBook(1))
        cmd = Command("addClient|1960715060015|Rusu Cosmin")
        controller.addClient(cmd.toAddClient())
        clients.append(cmd.toAddClient())
        cmd = Command("addClient|2960715060015|Rusu Raluca")
        controller.addClient(cmd.toAddClient())
        clients.append(cmd.toAddClient())
        assert controller.getBooks() == books
        assert controller.getClients() == clients
        cmd = Command("updateName|1960715060015|Rusu Cosmin-Ionut")
        controller.updateClientName(int(cmd.getArg(1)), cmd.getArg(2))
        clients[0].setName("Rusu Cosmin-Ionut")
        assert controller.getClients() == clients
        cmd = Command("updateCnp|2960715060015|2020715060015")
        controller.updateClientCnp(int(cmd.getArg(1)), int(cmd.getArg(2)))
        clients[1].setCnp(2020715060015)
        assert controller.getClients() == clients
        cmd = Command("removeClient|2020715060015")
        controller.removeClient(int(cmd.getArg(1)))
        clients = clients[:-1]
        assert controller.getClients() == clients
        cmd = Command("removeBook|1")
        controller.removeBook(int(cmd.getArg(1)))
        books = books[:-1]
        cmd = Command("updateDescription|0|The best book on algorithms and data structures")
        controller.updateDescription(int(cmd.getArg(1)), cmd.getArg(2))
        books[0].setDescription("The best book on algorithms and data structures")
        assert controller.getBooks() == books
        controller.undo()
        controller.undo()
        assert controller.getBooks() == [Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen"),
                                        Book(1, "Learning Python - 3rd Edition", "A very nice book for learning Python from scratch", "Mark Lutz")]
        assert controller.getClients() == [Client(1960715060015, "Rusu Cosmin-Ionut")]
        controller.redo()
        assert controller.getBooks() == [Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen")]
        assert controller.getClients() == [Client(1960715060015, "Rusu Cosmin-Ionut")]

        #tests exactly like the running scenario here: https://github.com/rusucosmin/courses/tree/master/fop/lab05-07

        books = []
        clients = []
        testrepo = LibraryRepository(False)
        controller = LibraryController(testrepo)
        cmd = Command("addBook|Introduction to Algorithms|The Bible for every computer scientist|Thomas H Cormen")
        controller.addBook(cmd.toAddBook(0))
        books.append(cmd.toAddBook(0))
        cmd = Command("addBook|Learning Python - 3rd Edition|A very nice book for learning Python from scratch|Mark Lutz")
        controller.addBook(cmd.toAddBook(1))
        books.append(cmd.toAddBook(1))
        cmd = Command("addClient|1960715060015|Rusu Cosmin")
        controller.addClient(cmd.toAddClient())
        clients.append(cmd.toAddClient())
        cmd = Command("addClient|2960715060015|Rusu Raluca")
        controller.addClient(cmd.toAddClient())
        clients.append(cmd.toAddClient())
        assert controller.getBooks() == books
        assert controller.getClients() == clients
        cmd = Command("updateName|1960715060015|Rusu Cosmin-Ionut")
        controller.updateClientName(int(cmd.getArg(1)), cmd.getArg(2))
        clients[0].setName("Rusu Cosmin-Ionut")
        assert controller.getClients() == clients
        cmd = Command("updateCnp|2960715060015|2020715060015")
        controller.updateClientCnp(int(cmd.getArg(1)), int(cmd.getArg(2)))
        clients[1].setCnp(2020715060015)
        assert controller.getClients() == clients
        cmd = Command("removeClient|2020715060015")
        controller.removeClient(int(cmd.getArg(1)))
        clients = clients[:-1]
        assert controller.getClients() == clients
        cmd = Command("removeBook|1")
        controller.removeBook(int(cmd.getArg(1)))
        books = books[:-1]
        cmd = Command("updateDescription|0|The best book on algorithms and data structures")
        controller.updateDescription(int(cmd.getArg(1)), cmd.getArg(2))
        books[0].setDescription("The best book on algorithms and data structures")
        assert controller.getBooks() == books
        controller.undo()
        controller.undo()
        assert controller.getBooks() == [Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen"),
                                        Book(1, "Learning Python - 3rd Edition", "A very nice book for learning Python from scratch", "Mark Lutz")]
        assert controller.getClients() == [Client(1960715060015, "Rusu Cosmin-Ionut")]
        controller.redo()
        assert controller.getBooks() == [Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen")]
        assert controller.getClients() == [Client(1960715060015, "Rusu Cosmin-Ionut")]

        cmd = Command("addClient|2960715060015|Rusu Raluca-Rusu")
        controller.addClient(cmd.toAddClient())
        cmd = Command("addBook|Dorian Gray's Portret|Modern novel|Oscar Wilde")
        controller.addBook(cmd.toAddBook(1))
        cmd = Command("addBook|The basis of Math|A nice book on Math for students|Dorin Andrica")
        controller.addBook(cmd.toAddBook(2))
        print(controller.getClients())
        print(controller.getLoans())
        cmd = Command("rentBook|1960715060015|0")
        controller.rentBook(int(cmd.getArg(1)), int(cmd.getArg(2)))
        cmd = Command("rentBook|1960715060015|1")
        controller.rentBook(int(cmd.getArg(1)), int(cmd.getArg(2)))
        cmd = Command("returnBook|2960715060015|1")
        controller.returnBook(int(cmd.getArg(1)), int(cmd.getArg(2)))
        assert controller.getBooks() == [
            Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen"),
            Book(1, "Dorian Gray's Portret", "Modern novel", "Oscar Wilde"),
            Book(2, "The basis of Math", "A nice book on Math for students", "Dorin Andrica")
        ]
        assert controller.getClients() == [
            Client(1960715060015, "Rusu Cosmin-Ionut"),
            Client(2960715060015, "Rusu Raluca-Rusu")
        ]
        assert controller.getLoans() == [
            Loan(Client(1960715060015, "Rusu Cosmin-Ionut"),
                 Book(0, "Introduction to Algorithms", "The Bible for every computer scientist", "Thomas H Cormen"))
        ]
        '''
        Should look like this
        Book #0:
        Title: Introduction to Algorithms
        Description: The Bible for every computer scientist
        Author: Thomas H Cormen


        Book #1:
        Title: Dorian Gray's Portret
        Description: Modern novel
        Author: Oscar Wilde


        Book #2:
        Title: The basis of Math
        Description: A nice book on Math for students
        Author: Dorin Andrica


        Client Name: Rusu Cosmin-Ionut
        CNP: 1960715060015

        Client Name: Rusu Raluca-Rusu
        CNP: 2960715060015

        Client Rusu Cosmin-Ionut has the book #0
        with the Title: Introduction to Algorithms
        '''
