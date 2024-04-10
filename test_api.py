import functions_api
from functions_ui import LoginPageActions

#
#
# # Check via API if the reminder in the list exists
# async def test_list_check():
#     random_list_name = LoginPageActions.generate_random_name(8)
#     await LoginPageActions.create_list(random_list_name)
#
#     # Create a new reminder
#     random_reminder_name = LoginPageActions.generate_random_name(10)
#     await LoginPageActions.create_reminder(random_reminder_name)
#
#
#     # Check via API if the list exists
#     api_tests = functions_api.APITests()
#     # CREATING A SESSION! DO NOT REMOVE!
#     await api_tests.setup_class()
#
#     lists = await api_tests.get_all_lists()
#     # print("Lists:", lists)
#     list_id = await api_tests.find_element_id_by_name(lists, random_list_name, 'name')
#
#     # print("List ID:", list_id)
#     list_name = await api_tests.get_list_by_id(list_id)
#     # print(list_name)
#     assert list_name == random_list_name
#
#     # Check via API if the reminder in the list exists
#     api_test = functions_api.APITests()
#     lists = await api_test.get_all_lists()
#     list_id = await api_test.find_element_id_by_name(lists, random_list_name, 'name')
#     # print(list_id)
#     reminders = await api_test.get_all_reminders(list_id)
#     reminder_id = await api_test.find_element_id_by_name(reminders, random_reminder_name, 'description')
#     # reminder_name = await api_test.get_list_by_id(reminder_id)
#     reminder_name = await api_test.get_reminder_by_id(reminder_id)
#     # assert list_name ==  random_list_name
#     assert reminder_name == random_reminder_name
