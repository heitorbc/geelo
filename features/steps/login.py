from behave import *
from test.factories.user import UserFactory
import time



@given(u'Sou um usuario anonimo')
def step_impl(context):
    # from django.contrib.auth.models import User
    br = context.browser
    br.get('https://geelo.herokuapp.com/logout/')

    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='admin', email='admin@example.com')
    u.set_password('admin12345')
    # Don't omit to call save() to insert object in database
    u.save()


@when(u'Informo o usuario ou senha incorreto')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/')
    
    # Checks for Cross-Site Request Forgery protection input (once again)
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (invalid version)
    br.find_element_by_name('username').send_keys('adimn')
    br.find_element_by_name('password').send_keys('ad321')
    br.find_element_by_name('action-login').click()
    

    

@then(u'Sou redirecionado para a pagina de login ate que eu informe usuario e senha corretos')
def step_impl(context):
    time.sleep(1)
    br = context.browser
    
    # Checks redirection URL
    assert br.current_url.endswith('/')



@when(u'Informo o usuario e senha corretos')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/')
    
    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('admin')
    br.find_element_by_name('password').send_keys('admin12345')
    br.find_element_by_name('action-login').click()
    

@then(u'Sou redirecionado para a pagina principal do sistema')
def step_impl(context):
    time.sleep(1)
    br = context.browser
    
    # Checks success status
    assert br.current_url.endswith('/home/')


@then(u'Realizo logout')
def step_impl(context):
    br = context.browser
    br.get('https://geelo.herokuapp.com/logout/')
    
    time.sleep(1)
    assert br.current_url.endswith('/')
    
    
    

