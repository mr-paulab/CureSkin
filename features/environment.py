from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.application import Application
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# options.set_preference("browser.download.folderList",2)
# options.set_preference("browser.download.manager.showWhenStarting", False)
# options.set_preference("browser.download.dir","/Data")
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
# CHROME ###
    context.driver = webdriver.Chrome(
    executable_path="C:\\Users\\mrpau\\OneDrive\\Documents\\jobeasy\\CureSkin\\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

    # ### HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #         chrome_options=options,
    #         executable_path=r'C:\Users\mrpau\OneDrive\Documents\jobeasy\CureSkin\chromedriver.exe')
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(10)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)

    # ### FIREFOX ###
    # c = webdriver.FirefoxOptions()
    # c.binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    # context.driver = webdriver.Firefox(
    # options=c, executable_path=r'C:\Users\mrpau\OneDrive\Documents\jobeasy\CureSkin\geckodriver.exe')
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(10)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)

# for browerstack ###
#    desired_cap = {
#        'bstack:options': {
#            "os": "Windows",
#            "osVersion": "11",
#            "browserVersion": "latest",
#            "projectName": "CureSkin",
#            "buildName": "Build 2022-12-21",
#            "local": "false",
#            "networkLogs": "true",
#            "seleniumVersion": "3.14.0",
#        },
#        "browserName": "Chrome",
#        'name': test_name
#    }

#    bs_user = 'paulbrandon_uLjnpw'
#    bs_key = 'QzTF5YkAvZnsSthHRh7X'
#    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#   context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
#   context.app = Application(context.driver)


# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/sign-in.feature

# For Browserstack with Mobile
    desired_cap = {
         'bstack:options' : {
            "osVersion" : "16",
            "deviceName" : "iPhone 14 Plus",
            "projectName" : "Cureskin",
            "buildName" : "2022-12-23",
            "sessionName" : "Cureskin Mobile",
            "local" : "false",
            "deviceOrientation": "landscape",
         },
    }

    bs_user = 'paulbrandon_uLjnpw'
    bs_key = 'QzTF5YkAvZnsSthHRh7X'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    context.app = Application(context.driver)

# For Browserstack with Mobile
#    desired_cap = {
#         'bstack:options' : {
#            "osVersion" : "12.0",
#            "deviceName" : "Samsung Galaxy S22 Plus",
#            "projectName" : "Cureskin",
#            "buildName" : "2022-12-23",
#            "sessionName" : "Cureskin Mobile",
#            "local" : "false",
#        },
#        "browserName": "chrome",
#    }
#
#    bs_user = 'paulbrandon_uLjnpw'
#    bs_key = 'QzTF5YkAvZnsSthHRh7X'
#   url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
#    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
