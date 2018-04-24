from botX.tasks import BaseTask
from test_dummy_robot import DummyRobot

class DummyTask(BaseTask):

    def __init__(self, robot):
        super(DummyTask, self).__init__(robot)

    def setup(self):
        print('setting up ...')

    def run(self):
        assert(self.robot.components['dummy_component'].get_img('i want img') == 'img')
        assert(self.robot.components['dummy_component'].get_coord('bbox') == 10)

def test_dummy_task():
    robot = DummyRobot()
    task = DummyTask(robot)
