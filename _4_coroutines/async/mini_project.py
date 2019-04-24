import asyncio
import collections
import json
import aiohttp

from helper import http_async_get
inner_count = 0
outer_count = 0
Character = collections.namedtuple('Character', 'name film_count extra')

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def process_star_wars(response, loop):
    global inner_count
    result = {}
    inner_tasks = []
    for person in response['results']:
        result[person["name"]] = {}
        print("\tInner count: {0}".format(inner_count))
        inner_count += 1
        inner_tasks.append(loop.create_task(fetch_star_wars_character(result, person)))
    await asyncio.gather(*inner_tasks)
    return result

async def fetch_star_wars_character(data, person):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, person['url'])
        data[person['name']] = json.loads(response)

async def fetch_star_wars_characters(loop):
    global outer_count
    result = {}
    url = "https://swapi.co/api/people"
    should_stop = False
    async with aiohttp.ClientSession() as session:
        while should_stop == False:
            print("Outer count: {0}".format(outer_count))
            outer_count += 1
            response = await fetch(session, url)
            json_response = json.loads(response)
            result ={**result,**(await process_star_wars(json_response, loop))}
            url = json_response['next']
            should_stop = url == None
    print(result)
    return result


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.gather(fetch_star_wars_characters(loop))]
    res = loop.run_until_complete(asyncio.wait(tasks))
