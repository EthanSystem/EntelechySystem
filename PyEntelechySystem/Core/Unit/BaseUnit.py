"""
@File   : BaseUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

from PyEntelechySystem import *

from PyEntelechySystem.Core.Content import Content
from PyEntelechySystem.Core.Object.BaseObject import BaseObject


class BaseUnit(BaseObject):
    """
    基件
    """

    # content: Content

    def __int__(self, *args, **kwargs):
        self.type_name:str = 'base unit type'
        # self.uid = uuid.uuid4()
        self.content:Content = Content(type_name='base unit type', content_head='base unit content head', content_body='base unit content body')
        super().__init__()
        pass

    pass
