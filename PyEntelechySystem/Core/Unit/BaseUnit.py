"""
@File   : BaseUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

from PyEntelechySystem import *

from PyEntelechySystem.Core.Object.BaseObject import BaseObject
from PyEntelechySystem.Core.Content.Content import Content

@dataclass
class BaseUnit(BaseObject):
    """
    基件
    """

    type_name: str = 'base unit type'
    # self.uid = uuid.uuid4()
    content: Content = Content(type_name='base unit type', head='base unit content head', body='base unit content body')

    # def __int__(self, *args, **kwargs):
    #     self.type_name: str = 'base unit type'
    #     # self.uid = uuid.uuid4()
    #     self.content: Content = Content(type_name='base unit type', content_head='base unit content head', content_body='base unit content body')
    #     super().__init__()
    #     pass

    pass
