from abc import ABCMeta, abstractmethod


class CommandBase(metaclass=ABCMeta):
    def __subclasscheck__(self, subclass):
        return hasattr(subclass, "execute") or NotImplemented

    @abstractmethod
    def execute(self):
        """Method executed as the latest"""
        raise NotImplementedError("All methods must be implemented")
