from abc import ABC, abstractmethod


class ParserStrategy(ABC):

    @abstractmethod
    def collect_chapters(self, url):
        pass
