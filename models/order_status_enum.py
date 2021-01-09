from enum import Enum


class OrderStatus(Enum):
    NEW = 1
    AWAITING_REPLY = 2
    UPDATED = 3
    AWAITING_PAYMENT = 4
    PAID = 5
    WORKING = 6
    AWAITING_PICKUP = 7
    FULFILLED = 8
