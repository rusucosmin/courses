__author__ = 'cosmin'

from tester.tester import Tester
from controller.controller import Controller
from ui.calculator import Calculator


if __name__ == '__main__':
    t = Tester()
    t.test()

    controller = Controller()
    app = Calculator(controller)
    app.run()