from __future__ import print_function

import abc, six

@six.add_metaclass(abc.ABCMeta)
class BaseComponent(ABC):

    @abc.abstractmethod
    def setup(self, **kwargs):
        pass

    @abc.abstractmethod
    def shutdown(self):
        pass
