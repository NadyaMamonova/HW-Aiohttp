import asyncio
import aiohttp

HOST = 'http://127.0.0.1:8080'


async def main():
    async with aiohttp.ClientSession() as session:
        # print("get func")
        # response = await session.get(f"{HOST}/api/1")
        # print(response.status)
        # json_data = await response.json()
        # print(json_data)
        #
        # print("create func")
        # response = await session.post(f"{HOST}/api/",
        #                               json = {"heading": "fast", "description": "12345", "user_id": 1})
        # print(response.status)
        # json_data = await response.json()
        # print(json_data)
        #
        # print("patch func")
        # response = await session.patch(f"{HOST}/api/11",
        #                                json = {"heading": "user_2", "description": "dasd", "user_id": 1})
        # print(response.status)
        # json_data = await response.json()
        # print(json_data)

        print("del func")
        response = await session.delete(f"{HOST}/api/1")
        print(response.status)
        json_data = await response.json()
        print(json_data)

asyncio.run(main())