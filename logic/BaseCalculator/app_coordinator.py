# ===The application coordinator: it starts the application and it let it run===

"""
It instantiate two objects:

1. a **tester** to run the unit tests
2. an **app** and runs the run() method
"""

__author__ = 'cosmin'

import model
import tester
import ui

from tester.tester import Tester
from ui.calculator import Calculator

if __name__ == '__main__':
    t = Tester()
    t.test()

    app = Calculator()
    app.run()