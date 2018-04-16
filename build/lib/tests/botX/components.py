from abc import ABC, abstractmethod

class BaseComponent(ABC):

    @abstractmethod
    def setup(self, **kwargs):
        pass

    @abstractmethod
    def shutdown(self):
        pass
