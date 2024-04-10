
class PageLocators:
    login_form = 'form.login-form'
    username_input_field = 'input[name="username"]'
    password_input_field = 'input[name="password"]'
    login_button = 'button[data-testid="login-button"]'
    HOME_PAGE_TITLE = "Reminders | Bulldoggy reminders app"
    new_list_input_field = 'input[name="reminder_list_name"]'
    add_list_confirm_button = 'img[src="/static/img/icons/icon-check-circle.svg"]'
    ADD_LIST_BUTTON = 'div.reminders-list-list img[src="/static/img/icons/icon-add.svg"]'
    ADD_REMINDER_BUTTON = 'div.reminders-item-list img[src="/static/img/icons/icon-add.svg"]'
    REMINDER_LIST_TITLE = '.reminders-card-title p'
    NEW_REMINDER_ELEMENT = '.REMINDER_LIST .reminder-row[data-id="new-reminder-item-row"]'
    ADD_REMINDER_INPUT_FIELD = 'input[name="reminder_item_name"]'
    ADD_REMINDER_CONFIRM_BUTTON = 'div.reminders-item-list img[src="/static/img/icons/icon-check-circle.svg"]'
    list_name = 'p[data-id^="reminder-row-"][hx-trigger="click"]'
    reminder_name = 'input[name="reminder_item_name"]'


    locators = {
        'login_form': login_form,
        'login_input_field': username_input_field,
        'password_input_field': password_input_field,
        'login_button': login_button,
        'home_page_title': HOME_PAGE_TITLE,
        'new_list_input_field': new_list_input_field,
        'add_list_confirm_button': add_list_confirm_button,
        'ADD_LIST_BUTTON': ADD_LIST_BUTTON,
        'ADD_REMINDER_BUTTON': ADD_REMINDER_BUTTON,
        'REMINDER_LIST_TITLE': REMINDER_LIST_TITLE,
        'NEW_REMINDER_ELEMENT': NEW_REMINDER_ELEMENT,
        'ADD_REMINDER_INPUT_FIELD': ADD_REMINDER_INPUT_FIELD,
        'ADD_REMINDER_CONFIRM_BUTTON': ADD_REMINDER_CONFIRM_BUTTON,
        'list_name': list_name,
        'reminder_name': reminder_name,
    }
