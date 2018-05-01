from .botX.tasks import BaseTask
from .botX.robots import BaseRobot
#from .abc import ABC, abstractmethod

robot = BaseRobot(self)
task = BaseTask(self, robot)

def test_init():
	return task.robot == robot and task.subtasks == {}

#def test_add_subtask():
#	task.subtasks.add_subtask(self, 1, task)
#	return self.subtasks[1] == task(self.robot)