from behave import *

@given(u'Launch chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Launch chrome browser')

@when(u'User creates the customer')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User creates the customer')


@then(u'Verify customer created in application')
def step_impl(context):
    raise NotImplementedError(u'Then Verify customer created in application')