import requests
from bs4 import BeautifulSoup


def scrapping_site(username):
    url = f"https://example.com/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")

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

            return {
                "Username": username,
                "Year of Joined": joined_year,
                "Number of Followed Users": followed_users
            }
        else:
            return {
                "Username": username,
                "Year of Joined": None,
                "Number of Followed Users": None
            }
    else:
        print(f"fetch failed, user: {username} - status code: {response.status_code}")
        return None


if __name__ == "__main__":

    example_username = "superusername"

    profile_details = scrapping_site(example_username)

    if profile_details:
        print("Details: ")
        for key, value in profile_details.items():
            print(f"{key}: {value}")
    else:
        print("Something failed.")
