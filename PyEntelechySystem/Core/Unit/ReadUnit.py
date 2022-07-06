"""
@File   : ReadUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""
from PyEntelechySystem import *

from PyEntelechySystem.Core.Content.Content import Content
from PyEntelechySystem.Core.Unit.BaseUnit import BaseUnit


@dataclass
class ReadUnit(BaseUnit):
    """读件"""

    type_name: str = 'read unit type'
    content: Content = Content(type_name='content type', head='read unit content head', body='read unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='read unit feedback sign content head', body='read unit feedback sign content body')


    # def __init__(self, *args, **kwargs):
    #     self.type_name: str = 'read unit type'
    #     self.content: Content = Content(type_name='content type', head='read unit content head', body='read unit content body')
    #     self.feedback_sign: Content = Content(type_name='feedback sign type', head='read unit feedback sign content head', body='read unit feedback sign content body')
    #     super().__init__()
    #     pass


    def read_content(self, content: Content):
        """
        读内容
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """
        self.feedback_sign = Content(type_name='read feedback sign type', head='', body='read')
        return content, self.feedback_sign
        pass

    pass
