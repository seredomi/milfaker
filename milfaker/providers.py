from faker.providers import BaseProvider

from milfaker.data.misc import BRANCHES


class MilitaryProvider(BaseProvider):
    def military_branch(self, simple=False):
        if simple:  # return 'Army', or 'Marine Corps', etc.
            return self.random_element(BRANCHES.keys())
        else:  # first pick a branch, then a sub-branch like 'Army Active Duty'
            return self.random_element(self.random_element(BRANCHES.values()))
