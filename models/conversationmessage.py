from datetime import datetime, timezone

from kivy.event import EventDispatcher


class ConversationMessage(EventDispatcher):

    def __init__(self, **kwargs):

        self.id: str
        self.sender: str
        self.send_time: datetime.now(tz=timezone.utc)
        self.message: str
        self.is_business_response: bool = False

        super(ConversationMessage, self).__init__(**kwargs)

    def __repr__(self):
        return "Conversation Message Object"
