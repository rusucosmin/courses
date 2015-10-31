from ui.LibraryApplication import LibraryApplication
from ui.LibraryController import LibraryController

import atexit

__author__ = 'cosmin'

controller = LibraryController()
atexit.register(controller.saveHistory)
app = LibraryApplication(controller)
app.run()