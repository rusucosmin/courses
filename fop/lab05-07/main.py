import model
import repository
import tests
import ui

from repository.LibraryRepository import LibraryRepository

from tests.tester import Tester

from ui.LibraryApplication import LibraryApplication
from ui.LibraryController import LibraryController

import atexit

__author__ = 'cosmin'

if __name__ == '__main__':
    tester = Tester()
    tester.testAll()
    controller = LibraryController()
    atexit.register(controller.saveHistory)
    app = LibraryApplication(controller)
    app.run()