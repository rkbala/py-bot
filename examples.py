import http.server
import json
import asyncio
from botbuilder.schema import (Activity, ActivityTypes, ChannelAccount, HeroCard)
from botbuilder.core import BotFrameworkAdapter
from botbuilder.schema import (Activity, ActivityTypes, ChannelAccount)
from botframework.connector import ConnectorClient
from botframework.connector.auth import (MicrosoftAppCredentials, JwtTokenValidation, SimpleCredentialProvider)
from botframework.connector.models import CardImage

APP_ID = ''
APP_PASSWORD = ''

class BotRequestHandler(http.server.BaseHTTPRequestHandler):

    @staticmethod
    def __create_hero_cart(request_activity, title, url):
        return HeroCard(
            title="Test hero card image",
            subtitle="Testing subtitle",
            text="Here is some text",
            images=[CardImage()]
        )

    def __handle_conversation_update_activity(self, activity: Activity):
        self.send_response(202)
        self.end_headers()
        if activity.members_added[0].id != activity.recipient.id:
            self._adapter.send([BotRequestHandler.__create_reply_activity(activity, 'Hello and welcome to the echo bot!')])

    def __handle_message_activity(self, activity: Activity):
        self.send_response(200)
        self.end_headers()
        self._adapter.send([BotRequestHandler.__create_reply_activity(activity, 'You said: %s' % activity.text)])
        self._adapter.send()

    def __unhandled_activity(self):
        self.send_response(404)
        self.end_headers()

    def on_receive(self, activity: Activity):
        if activity.type == ActivityTypes.conversation_update.value:
            self.__handle_conversation_update_activity(activity)
        elif activity.type == ActivityTypes.message.value:
            self.__handle_message_activity(activity)
        else:
            self.__unhandled_activity()

    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(str(body, 'utf-8'))
        activity = Activity.deserialize(data)
        self._adapter = BotFrameworkAdapter(APP_ID, APP_PASSWORD)
        self._adapter.on_receive = self.on_receive
        self._adapter.receive(self.headers.get("Authorization"), activity)


try:
    SERVER = http.server.HTTPServer(('localhost', 9000), BotRequestHandler)
    print('Started http server on localhost:9000')
    SERVER.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down server')
    SERVER.socket.close()
