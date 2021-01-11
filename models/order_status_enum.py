from enum import Enum


class OrderStatus(Enum):
    NEW = 1
    UPDATED = 3
    PAID = 5
    AWAITING_REPLY = 2
    AWAITING_PAYMENT = 4
    AWAITING_PICKUP = 7
    WORKING = 6
    FULFILLED = 8
