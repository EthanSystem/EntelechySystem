"""
@File   : WriteUnit.py
@Author : Ethan Lin
@Date   : 2022/07/06
@Desc   : 写件
"""
from PyEntelechySystem.Core.Unit import *

@dataclass()
class WriteUnit(BaseUnit):
    """写件"""

    type_name: str = 'write unit type'
    content: Content = Content(type_name='content type', head='write unit content head', body='write unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='write unit feedback sign content head', body='write unit feedback sign content body')


    def write_content(self, content: Content):
        """
        写内容
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """
        self.feedback_sign = Content(type_name='write feedback sign type', head='', body='wrote')
        self.content = content
        return content, self.feedback_sign
        pass

    pass
