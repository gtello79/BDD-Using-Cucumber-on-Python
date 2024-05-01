from behave import when, given, then

@given('I create a new User')
def create_new_user(context):

    """
        Para realizar el llamado a los parámetros, es necesario incluir la sgnte linea de comando
        behave test/Basic_Examples/ --no-capture -D user_email=gtello@qservus.com -D pass=123123
    """

    user_data = context.config.userdata

    user_email = user_data['user_email']
    password = user_data['pass']

    pass

@when('I type {field}')
def type_field(context, field):
    pass

@when("I click on 'Login'")
def click_on(context):
    pass

@then('I should see the text Welcome')
def see_text_welcome(context):
    pass


@given('I am a passing steps')
def passing_steps(context):
    print(context.text.strip())
    pass

@then('I another a passing step')
def another_passing_steps(context):
    pass