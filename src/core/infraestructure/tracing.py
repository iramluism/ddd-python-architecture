
from typing import NoReturn
from typing import Optional

from core.application.tracing import ILogger
from core.application.tracing import ITracer


class Logger(ILogger):
    def info(self, info: str, context: Optional[dict] = None) -> NoReturn:
        pass  # TODO log info with logging library

    def error(self, info: str, context: Optional[dict] = None) -> NoReturn:
        pass  # TODO log error with logging library


class Tracer(ITracer):
    def trace(self, info: str, context: Optional[dict] = None) -> NoReturn:
        pass  # TODO trace with OpenTelemetry
