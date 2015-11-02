__author__ = 'cosmin'

from model.book import Book
from model.client import Client
from model.command import Command
from model.loan import Loan

from repository.LibraryRepository import LibraryRepository
from ui.LibraryController import LibraryController

class Tester:
    '''
    Class to implement the test functions for the whole application.
    '''
    def __init__(self):
        pass

    def testBook(self):
        '''
        Method to test the getter and the setter of the Book class
        '''
        book = Book(1, "Introduction to algorithms", "The Bible", "Thomas H Cormen");
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
        except SyntaxError:
            pass

        try:
            Command("addBook|Title||")
            assert False
        except SyntaxError:
            pass

        try:
            Command("addBook||Description|")
            assert False
        except SyntaxError:
            pass

        try:
            Command("addBook|||Author")
            assert False
        except SyntaxError:
            pass

        try:
            Command("addBook|Title|Description|")
            assert False
        except SyntaxError:
            pass

        try:
            Command("addBook|Title||Author")
            assert False
        except SyntaxError:
            pass

        try:
            Command("addBook||Description|Author")
            assert False
        except SyntaxError:
            pass

        command = Command("addBook|Title|Description|Author")
        assert command.toAddBook(1) == Book(1, "Title",  "Description", "Author")

        try:
            Command("Cosmin")
            assert False
        except SyntaxError:
            pass

        try:
            Command("addClient|1960715060015")
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("addClient|numarul25|Rusu Cosmin")
            command.toAddClient()
            assert False
        except ValueError:
            pass

        try:
            command = Command("removeBook|numarul25")
            command.toRemoveBook()
            assert False
        except ValueError:
            pass

        try:
            command = Command("removeBook|1|Title")
            command.toRemoveBook()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("removeClient|numarul25")
            command.toRemoveClient()
            assert False
        except ValueError:
            pass

        try:
            command = Command("removeClient")
            command.toRemoveClient()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("removeClient|1960715060|Rusu Cosmin")
            command.toRemoveClient()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateCnp|numarul25|newValue")
            command.toUpdateCnp()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateCnp|1960715060015|newValue")
            command.toUpdateCnp()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateCnp|numarul25|1960715060015")
            command.toUpdateCnp()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateCnp||")
            command.toUpdateCnp()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateCnp||1960715060015")
            command.toUpdateCnp()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateCnp|1960715060015|")
            command.toUpdateCnp()
            assert False
        except SyntaxError:
            pass

        Command("updateCnp|2960715060015|1960715060015")

        try:
            command = Command("updateName|numarul25|newValue")
            command.toUpdateName()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateName||")
            command.toUpdateName()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateName||1960715060015")
            command.toUpdateName()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateName|1960715060015|")
            command.toUpdateName()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateTitle|numarul25|NewValue")
            command.toUpdateTitle()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateTitle||")
            command.toUpdateTitle()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateTitle||1960715060015")
            command.toUpdateTitle()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateTitle|1960715060015|")
            command.toUpdateTitle()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateTitle|numarul25|NewValue")
            command.toUpdateTitle()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateAuthor|numarul25|NewValue")
            command.toUpdateAuthor()
            assert False
        except ValueError:
            pass

        try:
            command = Command("updateAuthor||")
            command.toUpdateAuthor()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateAuthor||1960715060015")
            command.toUpdateAuthor()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateAuthor|1960715060015|")
            command.toUpdateAuthor()
            assert False
        except SyntaxError:
            pass

        try:
            command = Command("updateAuthor|numarul25|NewValue")
            command.toUpdateAuthor()
            assert False
        except ValueError:
            pass

        command = Command("addClient|1960715060015|Rusu Cosmin")
        assert command.toAddClient() == Client(1960715060015, "Rusu Cosmin")

    def testAll(self):
        '''
        Method to invoke every other test functions
        '''
        self.testBook()
        self.testClient()
        self.testCommand()
