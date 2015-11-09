import atexit

from tests.tester import Tester
from ui.LibraryApplication import LibraryApplication
from controllers.LibraryController import LibraryController
from repository.LibraryRepository import LibraryRepository

from model.book import Book
from model.client import Client

__author__ = 'cosmin'

if __name__ == '__main__':
    tester = Tester()
    tester.testAll()

    repo = LibraryRepository()
    controller = LibraryController(repo)
    atexit.register(repo.saveHistory)
    app = LibraryApplication(controller)
    app.run()