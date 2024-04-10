from playwright.async_api import async_playwright, Page, Locator
from page_locators import PageLocators
import asyncio
import requests
import dotenv
import os
import logging
import pytest
import json
import random
import string



dotenv.load_dotenv()

current_folder = os.path.dirname(__file__)
save_path = os.path.join(current_folder, 'logs', 'playwright.log')

# print("Current Working Directory:", os.getcwd())

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=save_path,
    filemode='a'
)


class LoginPageActions:
    def __init__(self, page: Page):
        self.page = page
        self.exceptions = []

    async def login(self, username, password):
        await self.type_text(PageLocators.username_input_field, username)
        await self.type_text(PageLocators.password_input_field, password)
        await self.click_element(PageLocators.login_button)

    async def find_element(self, locator: str, timeout: int = 2000):
        return await self.page.wait_for_selector(locator, timeout=timeout)

    async def type_text(self, locator: str, text: str, timeout: int = 2000):
        await self.page.fill(locator, text, timeout=timeout)

    async def click_element(self, locator: str, timeout: int = 2000):
        await self.page.click(locator, timeout=timeout)

    async def check_page_title(self, expected_title: str) -> bool:
        # actual_title = await self.page.title()
        # return expected_title in actual_title
        try:
            actual_title = await self.page.title()
            assert expected_title in actual_title, f"Expected title: '{expected_title}', Actual title: '{actual_title}'"
            return True
        except AssertionError as e:
            self.exceptions.append(e)
            return False

    async def create_list(self, list_name: str):
        try:
            await self.click_add_list_button()
            await self.enter_list_name(list_name)
            await self.confirm_list_creation()
        except Exception as e:
            self.exceptions.append(e)

    async def click_add_list_button(self, timeout: int = 2000):
        try:
            await self.click_element(PageLocators.ADD_LIST_BUTTON, timeout=timeout)
        except Exception as e:
            self.exceptions.append(e)

    async def enter_list_name(self, list_name: str, timeout: int = 2000):
        try:
            await self.type_text(PageLocators.new_list_input_field, list_name, timeout=timeout)
        except Exception as e:
            self.exceptions.append(e)

    async def confirm_list_creation(self, timeout: int = 2000):
        try:
            await self.click_element(PageLocators.add_list_confirm_button, timeout=timeout)
        except Exception as e:
            self.exceptions.append(e)

    async def click_add_reminder_button(self, timeout: int = 2000):
        try:
            await self.click_element(PageLocators.ADD_REMINDER_BUTTON, timeout=timeout)
        except Exception as e:
            self.exceptions.append(e)

    async def type_reminder_name(self, reminder_name: str, timeout: int = 2000):
        try:
            await self.type_text(PageLocators.ADD_REMINDER_INPUT_FIELD, reminder_name, timeout=timeout)
        except Exception as e:
            self.exceptions.append(e)

    async def click_add_reminder_confirm_button(self, timeout: int = 2000):
        try:
            await self.click_element(PageLocators.ADD_REMINDER_CONFIRM_BUTTON, timeout=timeout)
        except Exception as e:
            self.exceptions.append(e)

    async def create_reminder(self, reminder_name: str):
        await self.click_add_reminder_button()
        await self.type_reminder_name(reminder_name)
        await self.click_add_reminder_confirm_button()

    @staticmethod
    def generate_random_name(length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    async def check_list_name(self, expected_name: str, timeout: int = 2000):
        try:
            list_element = await self.find_element(PageLocators.list_name, timeout=timeout)
            actual_name = await list_element.text_content()
            print(f"\nActual List name: {actual_name}, Expected: {expected_name}")
            assert expected_name == actual_name, f"Expected list name: '{expected_name}', Actual list name: '{actual_name}'"
        except Exception as e:
            self.exceptions.append(e)

    async def check_reminder_name(self, expected_name: str, timeout: int = 2000):
        try:
            reminder_element = await self.find_element(PageLocators.reminder_name, timeout=timeout)
            actual_name = await reminder_element.get_attribute('value')
            print(f"\nActual Reminder name: {actual_name}, Expected: {expected_name}")
            assert expected_name == actual_name, f"Expected reminder name: '{expected_name}', Actual reminder name: '{actual_name}'"
        except Exception as e:
            self.exceptions.append(e)

    # async def check_api(self, request_type: str, request_endp: str, expected_value: str, resp_code: int):
    #     pass


class LoginPage(LoginPageActions):
    def __init__(self, page: Page):
        super().__init__(page)


class Locators:
    @staticmethod
    def get_locator(name: str) -> str:
        return getattr(PageLocators, name, None)

# @pytest.mark.asyncio
# @pytest.mark.ui
# async def test_login_and_check_home_page():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False, timeout=2000, slow_mo=200)
#         context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
#         page = await context.new_page()
#
#         login_page = LoginPage(page)
#         await page.goto(URL)
#
#         # Perform login
#         await login_page.login(LOGIN, PASSWORD)
#
#         is_home_page = await login_page.check_page_title(
#             PageLocators.HOME_PAGE_TITLE)  # ("Reminders | Bulldoggy reminders app")
#         print("\nIs home page:", is_home_page)
#         assert is_home_page, "Failed to navigate to the home page"
#
#         # Close browser
#         await browser.close()
