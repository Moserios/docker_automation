from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def click_element(self, locator):
        await self.page.click(locator)

    async def type_text(self, locator, text):
        await self.page.fill(locator, text)

    async def get_element_text(self, locator):
        element = await self.page.locator(locator).first()
        return await element.text()

    async def is_element_visible(self, locator):
        return bool(await self.page.locator(locator).first())
