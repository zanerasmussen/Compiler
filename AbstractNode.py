from abc import ABCMeta, abstractmethod

class ASTBASENODE(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError("Abstract Method")