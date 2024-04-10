from playwright.async_api import Page
from .base_page import BasePage
from ..page_locators.locators import Locators


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = Locators

    async def navigate_to_settings(self):
        await self.click_element(self.locators.SETTINGS_BUTTON)

    # Add more methods as needed for interacting with elements on the home page
