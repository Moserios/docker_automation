from playwright.async_api import async_playwright, Browser, BrowserContext, Page
import requests
import pytest
import httpx
from functions_api import GetCookies

# @pytest.fixture(scope="session")
# async def api_tests():
#     await GetCookies.setup_class()
#     return api_tests()

# class GetCookies:
#     browser: Browser = None
#     context: BrowserContext = None
#     page: Page = None
#     session_cookie_value = None
#     playwright_cookie = {}
#
#     @classmethod
#     async def setup_class(cls):
#         # Perform API-based login and retrieve the session cookie
#         login_url = "http://127.0.0.1:8000/login"
#         credentials = {"username": "Moser",
#                       "password": "12345"
#                        }
#         headers = {
#             "Content-Type": "application/x-www-form-urlencoded",
#             "accept": "application/json"
#         }
#
#         async with httpx.AsyncClient() as client:
#             response = await client.post(login_url, data=credentials, headers=headers)
#             print(response.text)  # Debugging
#             session_cookie_value = response.cookies.get('reminders_session')
#             print(session_cookie_value)
#
#             print(response.cookies)
#
#             playwright_cookie = {
#                 'name': 'reminders_session',
#                 'value': session_cookie_value,
#                 'domain': '127.0.0.1',  # Adjust as necessary
#                 'path': '/',  # The default path is '/'
#                 'httpOnly': True,
#                 'secure': False,  # Adjust based on your environment, True if HTTPS
#             }
#
#             cls.playwright_cookie['reminders_session'] = session_cookie_value
#             print(playwright_cookie)
#
