from playwright.async_api import Page
import page


class LoginPageLocators:
    LOGIN_FORM = 'form.login-form'
    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    LOGIN_BUTTON = 'button[data-testid="login-button"]'

    locators = {
        'login_form': LOGIN_FORM,
        'login_input_field': USERNAME_INPUT,
        'password_input_field': PASSWORD_INPUT,
        'login_button': LOGIN_BUTTON
    }

