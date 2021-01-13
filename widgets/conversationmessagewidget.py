from arrow import arrow
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from models.conversationmessage import ConversationMessage


class ConversationMessageWidget(BoxLayout):
    conversation = ObjectProperty(ConversationMessage, rebind=True)
    humanized_time = StringProperty(rebind=True)

    def __init__(self, conversation: ConversationMessage, **kwargs):
        self.conversation = conversation
        super(ConversationMessageWidget, self).__init__(**kwargs)

    def on_conversation(self, instance, value):
        print('humanizing')
        self.humanized_time = arrow.Arrow.fromdatetime(value.send_time).humanize()
