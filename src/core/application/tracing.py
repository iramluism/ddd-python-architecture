import abc
from typing import NoReturn
from typing import Optional


class ITracer(abc.ABCMeta):
    @abc.abstractmethod
    def trace(self, info: str, context: Optional[dict] = None) -> NoReturn:
        raise NotImplementedError()


class ILogger(abc.ABCMeta):
    @abc.abstractmethod
    def info(self, info: str, context: Optional[dict] = None) -> NoReturn:
        raise NotImplementedError()

    @abc.abstractmethod
    def error(self, info: str, context: Optional[dict] = None) -> NoReturn:
        raise NotImplementedError()
