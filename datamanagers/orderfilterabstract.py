from abc import ABC, abstractmethod

from models.order import Order


class OrderFilterAbstract(ABC):
    @abstractmethod
    def Filter(self, orders: Order):
        pass
