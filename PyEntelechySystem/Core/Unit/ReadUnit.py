"""
@File   : ReadUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

from PyEntelechySystem.Core.Content.Content import Content
from PyEntelechySystem.Core.Unit.BaseUnit import BaseUnit


class ReadUnit(BaseUnit):
    """读取单元"""

    feedback_sign: Content

    def __init__(self, feedback_sign):
        super().__init__(self)
        self.feedback_sign = feedback_sign
        pass

    def read_content(self, content: Content):
        """
        读取内容
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """
        self.feedback_sign = Content(type_name='feed back sign', content_head='', content_body='read')
        return content, self.feedback_sign
        pass

    pass
