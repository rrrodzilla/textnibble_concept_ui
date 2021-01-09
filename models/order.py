from datetime import datetime
from models.order_status_enum import OrderStatus


class Order:

    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)
        self.id: str
        self.time: datetime
        self.customer_name: str
        self.order_message: str
        self.status: OrderStatus = OrderStatus.NEW
