import asyncio
from scraping_the_data import scrap
from math_and_results import similarity



async def async_scrap(username):
    loop = asyncio.get_event_loop()
    data= await loop.run_in_executor(None, scrap, username)
    return data

async def get_results(username1, username2):
    user1_data, user2_data = await asyncio.gather(
            async_scrap(username1),
            async_scrap(username2)
        )
    if not user1_data or user2_data:
        return 0
    return similarity(user1_data, user2_data)
    