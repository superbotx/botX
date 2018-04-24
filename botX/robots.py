from abc import ABC, abstractmethod
from threading import Thread

class BaseRobot(ABC):

    def __init__(self):
        self.components = {}

    def add_component(self, component_id, component):
        self.components[component_id] = component

    def remove_component(self, component_id):
        if component_id in self.components:
            del self.components[component_id]
        else:
            print(component_id, ' does not exist')

    def setup_components(self, configs={}):
        waitlist = []
        for component_id, component in self.components.items():
            setup_args = {}
            if component_id in configs:
                setup_args = configs[component_id]
            setup_t = Thread(target=component.setup, kwargs=setup_args)
            waitlist.append(setup_t)
        for setup_t in waitlist:
            setup_t.start()
        for setup_t in waitlist:
            setup_t.join()

    def shutdown_components(self):
        waitlist = []
        for component_id, component in self.components.items():
            shutdown_t = Thread(target=component.shutdown)
            waitlist.append(shutdown_t)
        for shutdown_t in waitlist:
            shutdown_t.start()
        for shutdown_t in waitlist:
            shutdown_t.join()

    @abstractmethod
    def additional_setup(self):
        pass

    @abstractmethod
    def additional_shutdown(self):
        pass

    def start(self, **kwargs):
        configs = kwargs.pop('configs', {})
        self.additional_setup(**kwargs)
        self.setup_components(**configs)

    def shutdown(self, **kwargs):
        self.shutdown_components()
        self.additional_shutdown(**kwargs)
