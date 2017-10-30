import abc
from typing import List


class Builder(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def build(self):
        """ this method actually does the building """
        pass

    @abc.abstractmethod
    def get_targets(self) -> List[str]:
        """ return the names of the files that you are sure you produce. If you do not know them,
        you must implement the get_results_names_post_build method and return None here."""
        pass

    @abc.abstractmethod
    def get_targets_post_build(self) -> List[str]:
        """ find out the names of the files that you produced.
        If you implemented the get_results_names and there you return all the results
        that you created then you don't need to implement anything here """
        pass

    @abc.abstractmethod
    def get_signature(self) -> str:
        """ return the sha1 of anything that identifies the build """
        pass


class Populator(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def populate(self):
        """ this method actually does the populating """
        pass
