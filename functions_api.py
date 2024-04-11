import pytest
import data
import httpx
import asyncio
from playwright.async_api import async_playwright, Browser, BrowserContext, Page


class GetCookies:
    browser: Browser = None
    context: BrowserContext = None
    page: Page = None
    session_cookie_value = None
    playwright_cookie = {}

    @classmethod
    async def setup_class(cls):
        login_url = f"{data.BASE_URL}{data.LOGIN_ENDPOINT}"
        credentials = {"username": data.LOGIN,
                       "password": data.PASSWORD
                       }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(login_url, data=credentials, headers=headers)
            session_cookie_value = response.cookies.get('reminders_session')

            playwright_cookie = {
                'name': 'reminders_session',
                'value': session_cookie_value,
                'domain': data.DOMAIN,  # Adjust as necessary
                'path': '/',  # The default path is '/'
                'httpOnly': True,
                'secure': False,  # Adjust based on your environment, True if HTTPS
            }

            cls.playwright_cookie['reminders_session'] = session_cookie_value


@pytest.mark.asyncio
class APITests(GetCookies):
    # GetCookies.setup_class() # DO NOT REMOVE! CREATING A SESSION
    async def get_all_lists(self):
        url = f"{data.GET_ALL_LISTS}"
        async with httpx.AsyncClient(cookies=self.playwright_cookie, follow_redirects=True) as client:
            response = await client.get(url)

            # print(f"Response status code: {response.status_code}")
            if response.status_code == 200:
                # print(f"Lists: {response.text}")
                return response.json()
            if response.status_code == 307:
                print(f"Redirecting to: {response.headers['Location']}")
            else:
                print(f"Failed to retrieve lists. Status code: {response.status_code}")
                return None

    async def get_all_reminders(self, list_id: int):
        url = f"{data.GET_ALL_LISTS}/{list_id}/items"
        async with httpx.AsyncClient(cookies=self.playwright_cookie, follow_redirects=True) as client:
            response = await client.get(url)
            # print(f"Response status code: {response.status_code}")
            if response.status_code == 200:
                # print(f"Reminders: {response.text}")
                return response.json()
            if response.status_code == 307:
                print(f"Redirecting to: {response.headers['Location']}")
            else:
                print(f"Failed to retrieve reminders. Status code: {response.status_code}")
                return None
            # json_response = response.json()
            return response

    async def find_element_id_by_name(self, item_list, name_to_find: str, key: str):
        for item in item_list:
            if item[key] == name_to_find:  # name (for list) or description (for reminder)
                return item['id']
        return None

    async def get_list_by_id(self, list_id: int):
        # print(f"List ID: {list_id}")
        url = f"{data.GET_ALL_LISTS}/{list_id}"
        async with httpx.AsyncClient(cookies=self.playwright_cookie, follow_redirects=True) as client:
            response = await client.get(url)
            response_json = response.json()
            list_name = response_json['name']
            # print(f"List name: {list_name}")
            return list_name

    async def get_reminder_by_id(self, reminder_id: int):
        # print(f"Reminder ID: {reminder_id}")
        url = f"{data.GET_LIST_REMINDER_BY_ID}/{reminder_id}"
        async with httpx.AsyncClient(cookies=self.playwright_cookie, follow_redirects=True) as client:
            response = await client.get(url)
            response_json = response.json()
            reminder_name = response_json['description']
            # print(f"Reminder name: {reminder_name}")
            return reminder_name



async def main():
    await GetCookies.setup_class()  # Ensure setup_class is called and awaited
    api_tests = APITests()
    await api_tests.get_all_lists()  # Now this should work as expected


if __name__ == "__main__":
    asyncio.run(main())
