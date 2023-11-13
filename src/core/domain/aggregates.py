
from abc import ABCMeta

from pydantic import BaseModel


class IAggregate(BaseModel, ABCMeta):
    """  Aggregate Interface class """
