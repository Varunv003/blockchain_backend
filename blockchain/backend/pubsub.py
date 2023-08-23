from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
import time

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-95bda9ee-e37d-4a42-aa40-31cd4b3e020e'
pnconfig.publish_key = 'pub-c-2b56007e-fa4a-43fc-ba44-572e0bbd7d33'
pnconfig.user_id = 'varunvij000@gmail.com'
pubnub = PubNub(pnconfig)
test_channel = 'TEST_CHANNEL'
class PubSub():
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([test_channel]).execute()
        self.pubnub.add_listener(Listener())
    def publish(self, channel, message):
        self.pubnub.publish().channel(channel).message(message).sync()


# pubnub.subscribe().channels([test_channel]).execute()
class Listener(SubscribeCallback):
    def message(self, pubnub, message):
        print(
              f"\n  Channel : {message.channel}"
              f"\n  Message : {message.message}"
            )
# pubnub.add_listener(Listener())

def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(test_channel, {"eren":"hatake"})
if __name__ == '__main__':
    main()
