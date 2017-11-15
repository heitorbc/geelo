from selenium import webdriver

def before_all(context):
    context.browser = webdriver.PhantomJS()
    context.browser.implicitly_wait(1)
    context.server_url = 'http://0.0.0.0:8080'

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass

