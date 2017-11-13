from behave import *
from test.factories.user import UserFactory



@given(u'Sou um usuario anonimo')
def step_impl(context):
    # from django.contrib.auth.models import User

    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='thales', email='thales@example.com')
    u.set_password('thales123')
    # Don't omit to call save() to insert object in database
    u.save()



@when(u'Informo o usuario e senha corretos')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('thales')
    br.find_element_by_name('password').send_keys('thales123')
    br.find_element_by_name('action-login').click()



@then(u'Sou redirecionado para a pagina principal do sistema')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/home/')
    # assert br.find_element_by_id('main_title').text == "Login success"


@when(u'Informo o usuario ou senha incorreto')
def step_impl(context):
    br = context.browser

    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input (once again)
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (invalid version)
    br.find_element_by_name('username').send_keys('thales')
    br.find_element_by_name('password').send_keys('tha321')
    br.find_element_by_name('action-login').click()


@then(u'Sou redirecionado para a pagina de login ate que eu informe usuario e senha corretos')
def step_impl(context):

    # Checks redirection URL
    assert br.current_url.endswith('/')
    # assert br.find_element_by_id('main_title').text == "Login failure"