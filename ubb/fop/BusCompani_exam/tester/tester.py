from model.route import Route
from controller.controller import Controller
from repository.repository import Repository

class Tester:
    def __init__(self):
        self.test()

    def test(self):
        x = Route(1,"24b",93,3)
        assert(x.getId() == 1)
        x.setId(2)
        assert(x.getId() == 2)
        assert(x.getRouteCode() == "24b")
        x.setRouteCode("24")
        assert(x.getRouteCode() == "24")
        assert(x.getUsage() == 93)
        x.setUsage(95)
        assert(x.getUsage() == 95)
        assert(x.getBuses() == 3)
        x.setBuses(x.getBuses() + 1)
        assert(x.getBuses() == 4)
        x = Route(1,"24b",93,3)
        repo = Repository()
        repo.add(x)
        assert(repo.getRoutes() == [Route(1,"24b",93,3)])
        y = Route(13,"25",93,7)
        repo.add(y)
        assert(repo.getRoutes() == [Route(1,"24b",93,3), Route(13,"25",93,7)])
        repo.add(y)
        assert(repo.getRoutes() == [Route(1,"24b",93,3), Route(13,"25",93,7), Route(13,"25",93,7)])