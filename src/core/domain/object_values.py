
from abc import ABCMeta

from pydantic import BaseModel


class IObjectValue(BaseModel, ABCMeta):
    """ Object Value Interface class """
