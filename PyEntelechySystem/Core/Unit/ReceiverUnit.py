"""
@File   : ReceiverUnit.py
@Author : Ethan Lin
@Date   : 2022/07/06
@Desc   : 
"""

from PyEntelechySystem import *

from PyEntelechySystem.Core.Unit.BaseUnit import BaseUnit
from PyEntelechySystem.Core.Content.Content import Content

class ReceiverUnit(BaseUnit):
    """接收件"""

    type_name: str = 'write unit type'
    content: Content = Content(type_name='content type', head='receiver unit content head', body='receiver unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='receiver unit feedback sign content head', body='receiver unit feedback sign content body')

    def send_content(self, content: Content):
        """
        接收内容
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """

        # TODO 对接管线

        self.feedback_sign = Content(type_name='send feedback sign type', head='', _body='received')
        self.content = content
        return content, self.feedback_sign
        pass

    pass