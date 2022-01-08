from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver import ActionChains

# According to the selenium docs at https://selenium-python.readthedocs.io/ you can locate elements by id, name, xpath, link text, partial link text, tag name, class name and css selector

def check_exists_by_id(driver, id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_name(driver, name):
    try:
        driver.find_element_by_name(name)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_link_text(driver, link_text):
    try:
        driver.find_element_by_link_text(link_text)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_partial_link_text(driver, partial_link_text):
    try:
        driver.find_element_by_partial_link_text(partial_link_text)
    except NoSuchElementException:
        return False
    return True
    
def check_exists_by_tag_name(driver, tag_name):
    try:
        driver.find_element_by_tag_name(tag_name)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class_name(driver, classname):
    try:
        driver.find_element_by_class_name(classname)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_css_selector(driver, classnames):
    try:
        driver.find_element_by_css_selector(classnames)
    except NoSuchElementException:
        return False
    return True

def wait_till_exists(driver, type, key, timeout):
    found = False
    stopTime = time.time() + timeout
    if type == "id":
        while not found:
            if check_exists_by_id(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "name":
        while not found:
            if check_exists_by_name(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "xpath":
        while not found:
            if check_exists_by_xpath(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "link_text":
        while not found:
            if check_exists_by_link_text(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "partial_link_text":
        while not found:
            if check_exists_by_partial_link_text(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "tag_name":
        while not found:
            if check_exists_by_tag_name(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "class_name":
        while not found:
            if check_exists_by_class_name(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    elif type == "css_selector":
        while not found:
            if check_exists_by_css_selector(driver,key):
                found = True
                return True
            else:
                if time.time() > stopTime:
                    print("Could not find", type, key)
                    return False
    else:
        print('Type', type, 'not recognized.')
        return False

def click(element):
    try:
        element.click()
    except ElementClickInterceptedException:
        print("Encountered ElementClickInterceptedException, element", element, "not clickable.")
    except StaleElementReferenceException:
        print("Encountered StaleElementReferenceException, element", element, "is stale.")
    except NoSuchElementException:
        print("NoSuchElementException, unable to locate element", element)

def right_click(driver, element):
    try:
        action = ActionChains(driver)
        action.context_click(element).perform()
    except ElementClickInterceptedException:
        print("Encountered ElementClickInterceptedException, element", element, "not clickable.")
    except StaleElementReferenceException:
        print("Encountered StaleElementReferenceException, element", element, "is stale.")
    except NoSuchElementException:
        print("NoSuchElementException, unable to locate element", element)

def think(min, max):
    thinkTime = random.uniform(min, max)
    time.sleep(thinkTime)
    
def scroll_to_element(driver, element):
    try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except ElementClickInterceptedException:
        print("Encountered ElementClickInterceptedException, element", element, "not clickable.")
    except StaleElementReferenceException:
        print("Encountered StaleElementReferenceException, element", element, "is stale.")
    except NoSuchElementException:
        print("NoSuchElementException, unable to locate element", element)






