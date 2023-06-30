# import re
# import logging
from random import randint

import json
import discord as dis

token = json.loads(str(open("data\\token.json").read()))["token"]

mess_elem = json.loads(str(open("data\\stockage.json").read()))["mess_elem"]

class MainClient(dis.Client):
    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}!")

    async def on_message(self, message) -> None:
        quotes = mess_elem[0]["quotes"][0]
        responses = mess_elem[0]["responses"][0]
        banned = mess_elem[0]["quotes"][0]

        if message.author == self.user:
            return

        else:
            for kw in quotes:
                for i in range(len(quotes[kw])):
                    if quotes[kw][i] in message.content:
                        await message.channel.send(responses[kw][randint(0, len(responses[kw]) - 1)])

            for cat in banned:
                for i in range(len(quotes[cat])):
                    if banned[cat][i] in message.content:
                        warn_data = (banned[cat][i], cat)


intents = dis.Intents.default()
intents.message_content = True

client = MainClient(intents=intents)
client.run(token)
