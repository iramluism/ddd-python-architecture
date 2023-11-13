
import abc
from dataclasses import dataclass
from dataclasses import field
from typing import NoReturn
from typing import Optional

from fastapi import APIRouter
from fastapi import FastAPI
from injector import Injector
from injector import singleton

from core.presentation.rest.routers import router


@dataclass
class IComponent(metaclass=abc.ABCMeta):
    """ Component Interface class
    :param interface: Map<IterfaceClass:ImplemnetClass>
    """

    injector: Injector
    application: FastAPI
    parent_router: APIRouter
    interfaces: dict = field(default_factory=dict)
    router: Optional[APIRouter] = field(default=router)

    async def setup(self) -> NoReturn:
        await self.make_injections()
        await self.attach_router()

    async def make_injections(self) -> NoReturn:
        injector = self.injector
        for interface, implementation in self.interfaces.items():
            injector.binder.bind(
                interface=interface,
                to=implementation,
                scope=singleton,
            )

    async def attach_router(self) -> NoReturn:

        print(self.router)
        if not self.router:
            return None

        self.parent_router.include_router(self.router)
