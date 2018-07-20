class BasePage(object):

    def __init__(self, driver, repository):
        self.driver = driver
        self.object_rep = repository
