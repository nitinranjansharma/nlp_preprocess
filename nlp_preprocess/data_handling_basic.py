import numpy as np
import logging
logger = logging.getLogger(__name__)


class TestPackage():

    def __init__(self, text):
        self.text = text

    def print_text(self):
        print(self.text)
