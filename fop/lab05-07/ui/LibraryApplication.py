from model.command import Command
from model.exception import LibraryException

__author__ = 'cosmin'


class LibraryApplication:
    '''
        Class LibraryApplication which is represents an application instance.
        In encapsulate all the ui interaction
            - _controller - the LibraryController for the Library Application
    '''
    def __init__(self, controller):
        self._controller = controller

    def run(self):
        '''
        Main function which handles the ui menu:
            - handles the user inputted commands: it's the bridge between the ui and the backend application
        '''
        while True:
            try:
                opt = Command(input("Type a command. Press 'help' for the available commands: "))
                arg = opt.getArg(0)
                if arg == "help":
                    self.showMenu()
                elif arg == "addBook".lower():
                    self._controller.addBook(opt.toAddBook(len(self._controller.getBooks())))
                elif arg == "addClient".lower():
                    self._controller.addClient(opt.toAddClient())
                elif arg == "removeBook".lower():
                    self._controller.removeBook(int(opt.getArg(1)))
                elif arg == "removeClient".lower():
                    self._controller.removeClient(int(opt.getArg(1)))
                elif arg == "updateCnp".lower():
                    self._controller.updateClientCnp(int(opt.getArg(1)), int(opt.getArg(2)))
                elif arg == "updateName".lower():
                    self._controller.updateClientName(int(opt.getArg(1)), opt.getArg(2))
                elif arg == "updateTitle".lower():
                    self._controller.updateTitle(int(opt.getArg(1)), opt.getArg(2))
                elif arg == "updateDescription".lower():
                    self._controller.updateDescription(int(opt.getArg(1)), opt.getArg(2))
                elif arg == "updateAuthor".lower():
                    self._controller.updateAuthor(int(opt.getArg(1)), opt.getArg(2))
                elif arg == "listBooks".lower():
                    print('\n\n'.join(str(book) for book in self._controller.getBooks()))
                elif arg == "listClients".lower():
                    print('\n\n'.join(str(client) for client in self._controller.getClients()))
                elif arg == "listLoans".lower():
                    print('\n\n'.join(str(loan) for loan in self._controller.getLoans()))
                elif arg == "list":
                    print(self._controller.getLibrary())
                elif arg == "rentBook".lower():
                    self._controller.rentBook(int(opt.getArg(1)), int(opt.getArg(2)))
                elif arg == "returnBook".lower():
                    self._controller.returnBook(int(opt.getArg(1)), int(opt.getArg(2)))
                elif arg == "undo":
                    self._controller.undo()
                elif arg == "redo":
                    self._controller.redo()
                elif arg == "save":
                    self._controller.save()
                elif arg == "exit":
                    print("Exiting...")
                    break
                elif arg == 'delete':
                    self._controller.recreate()
                else:
                    print("Command not recognized!")
            except ValueError as ve:
                print("ValueError - Argument should be integer!")
            except LibraryException as le:
                print(str(le))

    def showMenu(self):
        '''
        Function to print all the available commands.
        '''
        print("Here are the commands:")
        print("     'addBook|Title of the book|Description of the book|Author of the book'")
        print("     'addClient|CNP|Name of the client'")
        print("     'removeBook|ID; - removes the specific book")
        print("     'removeClient|CNP' - removes the client with the given CNP")
        print("     'updateCnp|ACTUAL_CNP|NEW_CNP' - update the cnp of a person")
        print("     'updateName|CNP|NEW_NAME' - update the name of a person")
        print("     'updateTitle|ID_BOOK|NEW_TITLE' - update the title of a specific book")
        print("     'updateDescription|ID_BOOK|NEW_DESC' - update the description of a specific book")
        print("     'updateAuthor|ID_BOOK|NEW_AUTH' - update the author of a specific book")
        print("     'listBooks' - print all books")
        print("     'listClients' - print all clients")
        print("     'rentBook|CNP|BOOK_ID' - rent the BOOK_ID to the client with the given CNP")
        print("     'returnBOOK|CNP|BOOK_ID' - the client with the given CNP returns the BOOK_ID book")
        print("     'undo' - undo the last operation")
        print("     'redo' - reverse of undo")
        print("     'save' - save current library state")
        print("     'exit' - save and exit")
