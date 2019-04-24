import asyncio
import random

fake_item_list = [
        {
            "name": "one"
        },
        {
            "name":" two"
        }
    ]

async def get_items(loop):
    await asyncio.sleep(3)
    for item in fake_item_list:
        await loop.create_task(enrich_item(item))
        # item = await enrich_item(item)
    print(fake_item_list)
    return fake_item_list


async def enrich_item(item):
    await asyncio.sleep(random.randint(0,2))
    item["extra"] = random.randint(0,3)
    print(item)
    return item

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(get_items(loop))]
    res = loop.run_until_complete(asyncio.gather(*tasks))
    print("RES: {0}".format(res[0]))

