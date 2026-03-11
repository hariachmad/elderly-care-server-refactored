from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler 

    @abstractmethod
    def handle(self, request, lang="en"):
        if self._next_handler:
            return self._next_handler.handle(request, lang)
        return None