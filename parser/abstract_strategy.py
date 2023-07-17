from abc import ABC, abstractmethod


class ParserStrategy(ABC):

    @abstractmethod
    def logic(self):
        pass

    @abstractmethod
    def collect_chapter(self):
        pass

    @abstractmethod
    def collect_links(self):
        pass

    @abstractmethod
    def get_next_link(self):
        pass

    @abstractmethod
    def get_webpage(self, language):
        pass
