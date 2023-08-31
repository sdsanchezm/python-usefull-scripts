# scrapping asynchronously 

import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def get_async_profile(username, session):

    url = f"https://example.com/{username}"

    async with session.get(url) as response:

        if response.status == 200:

            content = await response.text()
            soup = BeautifulSoup(content, "lxml")

            user_info = soup.find("div", class_="user-profile")

            if user_info:
                joined_year = None
                followed_users = None

                joined_info = user_info.find("relative-time")

                if joined_info and "datetime" in joined_info.attrs:
                    joined_year = joined_info["datetime"].split("-")[0]

                followers_info = user_info.find("span", class_="text-bold color-text-primary")

                if followers_info:
                    followed_users = int(followers_info.text.replace(",", "").strip())

                return username, joined_year, followed_users
            else:
                return username, None, None
        else:
            print(f"Failed to fetch - status code: {response.status}")
            return username, None, None

async def scrapping_web_profiles(usernames):

    async with aiohttp.ClientSession() as session:

        tasks = [get_async_profile(username, session) for username in usernames]
        results = await asyncio.gather(*tasks)

        return results


if __name__ == "__main__":
    profile_user = ["superuserhere"]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        results = loop.run_until_complete(scrapping_web_profiles(profile_user))

        for username, joined_year, followed_users in results:
            if joined_year is not None and followed_users is not None:
                print(f"Username: {username}")
                print(f"Year of Joined: {joined_year}")
                print(f"Number of Followed Users: {followed_users}")
            else:
                print(f"Failed.")
    finally:
        
        loop.close()
