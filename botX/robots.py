from __future__ import print_function
import abc, six

@six.add_metaclass(abc.ABCMeta)
class BaseRobot():

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
        for component_id, component in self.components.items():
            setup_args = {}
            if component_id in configs:
                setup_args = configs[component_id]
            component.setup(**setup_args)

    def shutdown_components(self):
        for component_id, component in self.components.items():
            component.shutdown()

    @abc.abstractmethod
    def additional_setup(self):
        pass

    @abc.abstractmethod
    def additional_shutdown(self):
        pass

    def start(self, **kwargs):
        configs = kwargs.pop('configs', {})
        self.additional_setup(**kwargs)
        self.setup_components(**configs)

    def shutdown(self, **kwargs):
        self.shutdown_components()
        self.additional_shutdown(**kwargs)
