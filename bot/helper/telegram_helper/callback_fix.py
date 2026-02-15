from functools import wraps
from pyrogram.errors import FloodWait, RPCError
import asyncio

def callback_handler(func):
    @wraps(func)
    async def wrapper(client, query):
        try:
            # Answer immediately to stop the loading animation
            try:
                await query.answer()
            except:
                pass
            await func(client, query)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await wrapper(client, query)
        except RPCError as e:
            # log or handle other RPC errors
            pass
    return wrapper
