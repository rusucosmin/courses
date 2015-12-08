from tester.tester import Tester

from ui.application import Application

from controller.controller import Controller

from repository.repository import Repository


with open("database.txt", "r") as f:

    t = Tester()
    repo = Repository()
    controller = Controller(repo, f)
    app = Application(controller, repo)
    app.run()