# In consumers.py
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class YourConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        # Accept the connection
        await self.accept()

    async def receive_json(self, content):
        # This method is called when the consumer receives a message
        # You can write your logic here to handle different types of messages
        # For example, ride requests, fare offers, etc.
        pass

    # Define other methods to handle different events (e.g., disconnecting)
