import asyncio
import aiohttp

HOST = 'http://127.0.0.1:8080'


async def main():
    async with aiohttp.ClientSession() as session:

        async with session.post(f'{HOST}/user/',
                                json={
                                'title': 'Название',
                                'description': 'description',
                                'owner': 'owner'
                                }) as response:
            response = await response.json()
            print('user created')


        async with session.get(f'{HOST}/user/') as response:
            response = await response.json()
            print('get user')


        async with session.delete(f'{HOST}/user/') as response:
            response = await response.json()
            print('user deleted')


asyncio.run(main())

