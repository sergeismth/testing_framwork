""" Webdriver base operations."""

import time
import logging
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class BaseOperations(object):
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)
        logger.debug('Going to {}'.format(url))

    def wait(self, wait_seconds):
        logger.debug("Waiting for {} seconds".format(wait_seconds))
        time.sleep(wait_seconds)

    def wait_page_element_is_displayed(self, element, wait=15):
        logger.debug("Waiting for the element: {}".format(element))
        try:
            WebDriverWait(self.driver, wait).until(
                ec.visibility_of_element_located((By.XPATH, element)))
        except Exception:
            logger.error('The element is not present: {}'.format(element), exc_info=True)
            now = datetime.now().strftime('%F_%H-%M-%S')
            screenshot_name = 'screenshot_{}.png'.format(now)
            self.driver.get_screenshot_as_file('../../results/screenshots/{}'.format(screenshot_name))
            raise AssertionError(
                '\nTime: {}'
                '\nElement: {}'
                '\nScreenshot name: {}'.format(now, element, screenshot_name))

    def element_is_present(self, element, wait=15):
        try:
            WebDriverWait(self.driver, wait).until(
                ec.visibility_of_element_located((By.XPATH, element)))
            return True
        except:
            return False

    def element_is_not_present(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        if len(elements) == 0:
            return True
        else:
            return False

    def send_result(self, test_case_number):
        """Send test result:

        Based on sys.exc_info output:
        If sys.exc_info()[0] exist it means that the test failed"""

        if sys.exc_info()[0]:
            """ Test failed, so send appropriate API call to your test report system. """

            sys.stdout.write('Test: {} - Failed'.format(test_case_number))  # it's just a placeholder. Replace with a code which send result.

        else:
            """ Test passed"""
            sys.stdout.write('Test: {} - Passed'.format(test_case_number))  # it's just a placeholder. Replace with a code which send result.
