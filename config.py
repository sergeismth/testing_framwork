import logging
import os


HOMEPAGE_URL = 'https://google.com'

RESULTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'results'))

# logging to file:
root = logging.getLogger()
root.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='{}/logs/log_{}_{}.log'.format(RESULTS_PATH,
                                                                           TestRunningParameters.ENVIRONMENT,
                                                                           TestRunningParameters.CUSTOMER),
                                   mode='w')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
root.addHandler(file_handler)

# logging to console:
console = logging.StreamHandler()
formatter = logging.Formatter("%(name)s %(levelname)s %(message)s")
console.setFormatter(formatter)
root.addHandler(console)