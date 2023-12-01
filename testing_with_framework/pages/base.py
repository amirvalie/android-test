from utils.page_utils import PageUtils


class Base:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.page_utils = PageUtils(self.driver)
