"""
@File   : BaseUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""
import uuid

from PyEntelechySystem.Core.Content import Content
from PyEntelechySystem.Core.Object.BaseObject import BaseObject


class BaseUnit(BaseObject):
    """
    基单元
    """

    content: Content

    def __int__(self, content='', **kwargs):
        super().__init__(self)
        self.object_type_name = 'base unit type'
        self.id = uuid.uuid4()
        self.content = content
        pass

    pass
