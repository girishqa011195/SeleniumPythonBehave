from selenium import webdriver
import pytest
import platform
import pytest_html
import socket


@pytest.fixture()
def setup(browser):
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    driver.maximize_window()
    return driver

# Get the value from CL
def pytest_addoption(parser):
    parser.addoption("--browser")

#Return the browser value
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############# pytest html report #####################
# It is a hook for adding env info to the html report
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.metadata = {
        'Project Name': 'eComm',
        'Module Name': 'Customers',
        'Tester': socket.gethostname()
    }
    # html_report = os.path.join(config.rootdir, 'Reports', 'report.html')
    # with open(html_report, 'a') as f:
    #     f.write('<meta name="Project Name" content="eComm">\n')
    #     f.write('<meta name="Module Name" content="Customers">\n')
    #     f.write('<meta name="Tester" content="Girish">\n')


#It is a hook for delete/modify env info to the html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# This hook adds custom metadata to the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'eComm'
    metadata['Module Name'] = 'Customers'
    metadata['Tester'] = socket.gethostname()
