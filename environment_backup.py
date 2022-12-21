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


def browser_init(context):
    """
    :param context: Behave context
    """
    # ### CHROME ###
    # context.driver = webdriver.Chrome(executable_path="C:\\Users\\mrpau\\OneDrive\\Documents\\jobeasy\\CureSkin\\chromedriver.exe")
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(10)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)

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
    # context.driver = webdriver.Firefox(options=c, executable_path=r'C:\Users\mrpau\OneDrive\Documents\jobeasy\CureSkin\geckodriver.exe')
    # context.driver.maximize_window()
    # context.driver.implicitly_wait(10)
    # context.driver.wait = WebDriverWait(context.driver, 10)
    # context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
