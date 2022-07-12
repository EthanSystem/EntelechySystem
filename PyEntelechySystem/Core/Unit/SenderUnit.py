"""
@File   : SenderUnit.py
@Author : Ethan Lin
@Date   : 2022/07/06
@Desc   : 发送件
"""


from PyEntelechySystem.Core.Unit import *

@dataclass()
class SenderUnit(BaseUnit):
    """发送件"""

    type_name: str = 'write unit type'
    content: Content = Content(type_name='content type', head='sender unit content head', body='sender unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='sender unit feedback sign content head', body='sender unit feedback sign content body')

    def send_content(self, content: Content):
        """
        发送内容
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """

        # TODO 对接管线

        self.feedback_sign = Content(type_name='send feedback sign type', head='', body='sent')
        self.content = content
        return content, self.feedback_sign
        pass

    pass  # class
