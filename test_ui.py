from playwright.async_api import async_playwright, Page, Locator
import pytest
import functions_ui
import page_locators
import functions_db
import functions_api
import data


exceptions = []

@pytest.mark.asyncio
@pytest.mark.e2e
async def test_check_reminder_creation():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, timeout=2000, slow_mo=500)
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()
        login_page = functions_ui.LoginPage(page)
        await page.goto(data.BASE_URL)

        print(data.LOGIN, data.PASSWORD)
        # Perform login
        await login_page.login(data.LOGIN, data.PASSWORD)

        is_home_page = await login_page.check_page_title(page_locators.PageLocators.HOME_PAGE_TITLE)
        print("\nIs home page:", is_home_page)
        assert is_home_page, "Failed to navigate to the home page"

        # Create a new list
        random_list_name = login_page.generate_random_name(8)
        await login_page.create_list(random_list_name)

        # Check if the list was created
        await login_page.check_list_name(random_list_name)

        # Create a new reminder
        random_reminder_name = login_page.generate_random_name(10)
        await login_page.create_reminder(random_reminder_name)

        # Check if the reminder was created
        await login_page.check_reminder_name(random_reminder_name)

        # Check if the data exists in the database
        data_exists = await functions_db.check_database_for_data(random_list_name, random_reminder_name)
        assert data_exists, "Data not found in the database"

        # Check via API if the list exists
        api_tests = functions_api.APITests()
        # CREATING A SESSION! DO NOT REMOVE!
        await api_tests.setup_class()

        lists = await api_tests.get_all_lists()
        # print("Lists:", lists)
        list_id = await api_tests.find_element_id_by_name(lists, random_list_name, 'name')

        # print("List ID:", list_id)
        list_name = await api_tests.get_list_by_id(list_id)
        # print(list_name)
        assert list_name ==  random_list_name

        # Check via API if the reminder in the list exists
        api_test = functions_api.APITests()
        lists = await api_test.get_all_lists()
        list_id = await api_test.find_element_id_by_name(lists, random_list_name, 'name')
        # print(list_id)
        reminders = await api_test.get_all_reminders(list_id)
        reminder_id = await api_test.find_element_id_by_name(reminders, random_reminder_name, 'description')
        # reminder_name = await api_test.get_list_by_id(reminder_id)
        reminder_name = await api_test.get_reminder_by_id(reminder_id)
        # assert list_name ==  random_list_name
        assert reminder_name == random_reminder_name


        # Close browser
        await browser.close()


if len(exceptions) > 0:
    raise Exception(exceptions)
print(exceptions)
