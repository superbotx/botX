from .botX.components import BaseComponent
from .botX.robots import BaseRobot

class DummyComponent(BaseComponent):

    def __init__(self):
        super(DummyComponent, self).__init__()

    def setup(self):
        print('setup component')
        return 3

    def shutdown(self):
        print('shutdown component')
        return 5

    def get_img(self, config):
        return 'img'

    def get_coord(self, bbox):
        return 10

class DummyRobot(BaseRobot):

    def __init__(self):
        super(DummyRobot, self).__init__()
        self.add_component('dummy_component', DummyComponent())

    def additional_setup(self):
        print('setting up dummy robot')

    def additional_shutdown(self):
        print('shutting down dummy robot')

def test_dummy_component():
    dummy = DummyRobot()
    dummy.start()
    assert(dummy.components['dummy_component'].get_img('i want img') == 'img')
    assert(dummy.components['dummy_component'].get_coord('bbox') == 10)
    dummy.shutdown()
