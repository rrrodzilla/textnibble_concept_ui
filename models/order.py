from datetime import datetime


class Order:
    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)
        self.id: str
        self.order_time: datetime
        self.customer_name: str
        self.order_message: str
