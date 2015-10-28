from ui.LibraryApplication import LibraryApplication
from repository.LibraryRepository import  LibraryRepository
from ui.LibraryController import LibraryController

__author__ = 'cosmin'

controller = LibraryController()
app = LibraryApplication(controller)
app.run()