import aiohttp
import os
import psutil
from aiohttp import web


def show_memory_allocation():
    process = psutil.Process(os.getpid())
    print("The memory allocation for the process is {0:.4f}% of the total".format(process.memory_percent()))

async def http_async_get(url):
    res = await aiohttp.request('GET', url)
    if res.status == 200:
        ctype = res.headers.get('Content-type', '').lower()
        if 'json' in ctype or url.endswith('json'):
            data = await res.json()
        else:
            data = await res.read()
        return data
    elif res.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.errors.HttpProcessingError(
        code=res.status, message=res.reason,
        headers=res.headers)