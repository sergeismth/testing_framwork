"""Page methods"""

from base import BaseOperations
import locators
import config


class HomePage(BaseOperations):
    def come_here(self):
        self.navigate(config.HOMEPAGE_URL)
        self.wait_page_element_is_displayed(locators.HomePage.header)

    def search(self, search_for):
        pass

class SearchResultsPage(HomePage):
    pass