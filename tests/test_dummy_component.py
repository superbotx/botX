from botX.components import BaseComponent

class DummyComponent(BaseComponent):

    def __init__(self):
        super(DummyComponent, self).__init__()

    def setup(self):
        print('setup component')
        return 3

    def shutdown(self):
        print('shutdown component')
        return 5

def test_dummy_component():
    dummy = DummyComponent()
    assert(dummy.setup() == 3)
    assert(dummy.shutdown() == 5)
