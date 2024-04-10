from playwright.async_api import Page
from .login_page_actions import LoginPageActions

class LoginPage(LoginPageActions):
    def __init__(self, page: Page):
        super().__init__(page)


# from playwright.async_api import Page
# from .base_page import BasePage
# from ..locators.locators import Locators
#
#
# class LoginPage(BasePage):
#     def __init__(self, page: Page):
#         super().__init__(page)
#         self.locators = Locators
#
#     async def login(self, username, password):
#         await self.type_text(self.locators.USERNAME_INPUT, username)
#         await self.type_text(self.locators.PASSWORD_INPUT, password)
#         await self.click_element(self.locators.LOGIN_BUTTON)
#
#     async def get_login_error_message(self):
#         return await self.get_element_text(self.locators.LOGIN_ERROR_MESSAGE)
