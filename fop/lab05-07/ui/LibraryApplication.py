from model.command import Command

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
                    self._controller.addBook(opt.toAddBook(self._controller.getBooksSize()))
                elif arg == "addClient".lower():
                    self._controller.addClient(opt.toAddClient())
                elif arg == "removeBook".lower():
                    self._controller.removeBook(opt.toRemoveBook())
                elif arg == "removeClient".lower():
                    self._controller.removeClient(opt.toRemoveClient())
                elif arg == "updateCnp".lower():
                    self._controller.updateClientCnp(opt.toUpdateCnp())
                elif arg == "updateName".lower():
                    self._controller.updateClientName(opt.toUpdateName())
                elif arg == "updateTitle".lower():
                    self._controller.updateTitle(opt.toUpdateTitle())
                elif arg == "updateDescription".lower():
                    self._controller.updateDescription(opt.toUpdateDescription())
                elif arg == "updateAuthor".lower():
                    self._controller.updateAuthor(opt.toUpdateAuthor())
                elif arg == "listBooks".lower():
                    self._controller.listBooks()
                elif arg == "listClients".lower():
                    self._controller.listClients()
                elif arg == "undo":
                    self._controller.undo()
                elif arg == "redo":
                    self._controller.redo()
                elif arg == "list":
                    self._controller.listLibrary()
                elif arg == "save":
                    self._controller.saveHistory()
                elif arg == "exit":
                    print("Exiting...")
                    break
                elif arg == 'delete':
                    self._controller.createFreshLibrary()
                else:
                    print("Command not recognized!")
            except SyntaxError as se:
                print(str(se))
            except ValueError as ve:
                print(str(ve))
            except TypeError as te:
                print(str(te))
            except Exception as e:
                print(str(e))

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
        print("     'undo' - undo the last operation")
        print("     'redo' - reverse of undo")
        print("     'save' - save current library state")
        print("     'exit' - save and exit")
