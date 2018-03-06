from abc import ABC, abstractmethod

class BaseTask(ABC):

    def __init__(self, robot):
        self.robot = robot
        self.subtasks = {}

    def add_subtask(self, task_id, task):
        self.subtasks[task_id] = task(self.robot)

    def remove_subtask(self, task_id):
        if task_id in self.subtasks:
            del self.subtasks[task_id]
        else:
            print(task_id, ' does not exist')

    def get_subtask(self, task_id):
        if task_id in self.subtasks:
            return self.subtasks[task_id]
        else:
            print(task_id, ' does not exist')

    def setup_subtasks(self, configs={}):
        for task_id in self.subtasks:
            setup_args = None
            if task_id in configs:
                setup_args = configs[task_id]
            self.subtasks[task_id].setup_subtasks(**setup_args)
        self_args = configs['self']
        self.setup(**self_args)

    @abstractmethod
    def setup(self, **kwargs):
        pass

    @abstractmethod
    def run(self, **kwargs):
        pass
