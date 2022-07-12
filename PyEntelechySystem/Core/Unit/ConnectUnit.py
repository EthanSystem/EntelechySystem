"""
@File   : ConnectUnit.py
@Author : Ethan Lin
@Date   : 2022/07/07
@Desc   : 连接件
"""
from PyEntelechySystem.Core.Unit import *


@dataclass
class ConnectUnit(BaseUnit):
    """连接件"""

    type_name: str = 'connect unit type'
    content: Content = Content(type_name='content type', head='connect unit content head', body='connect unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='connect unit feedback sign content head', body='connect unit feedback sign content body')

    index_pos: tuple[float, float] = (0.0, 0.0)



    def connect_to_unit(self, content: Content):
        """
        连接功能
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """

        # TODO 对接管线


        self.feedback_sign = Content(type_name='connect feedback sign type', head='', body='connected')
        self.content = content
        return content, self.feedback_sign
        pass

    pass  # class
