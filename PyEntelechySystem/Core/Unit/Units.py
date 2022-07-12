"""
@File   : Units.py
@Author : Ethan Lin
@Date   : 2022/07/12
@Desc   : 
"""

from PyEntelechySystem import dataclass
from PyEntelechySystem.Core.Content import Content
from PyEntelechySystem.Core.Base import BaseUnit

"""
@File   : ReadUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 读件
"""


@dataclass()
class ReadUnit(BaseUnit):
    """读件"""

    type_name: str = 'read unit type'
    content: Content = Content(type_name='content type', head='read unit content head', body='read unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='read unit feedback sign content head', body='read unit feedback sign content body')
    feedback_sign.uid = Content.set_uuid()

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

    pass  # class


"""
@File   : WriteUnit.py
@Author : Ethan Lin
@Date   : 2022/07/06
@Desc   : 写件
"""


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

    pass  # class


"""
@File   : ReceiverUnit.py
@Author : Ethan Lin
@Date   : 2022/07/06
@Desc   : 接收件
"""


@dataclass()
class ReceiverUnit(BaseUnit):
    """接收件"""

    type_name: str = 'write unit type'
    content: Content = Content(type_name='content type', head='receiver unit content head', body='receiver unit content body')

    # feedback_sign: Content = Content(type_name='feedback sign type', head='receiver unit feedback sign content head', body='receiver unit feedback sign content body')

    def receive_content(self, content: Content):
        """
        接收内容
        :param content: 内容
        :type content: Content
        :return: content, feedback_sign
        :rtype: Content, Content
        """

        # TODO 对接管线

        feedback_sign: Content = Content(type_name='feedback sign type', head='', body='received')
        self.content = content
        return content, feedback_sign
        pass

    pass  # class


"""
@File   : WriteUnit.py
@Author : Ethan Lin
@Date   : 2022/07/06
@Desc   : 写件
"""


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

    pass  # class


"""
@File   : ConnectUnit.py
@Author : Ethan Lin
@Date   : 2022/07/07
@Desc   : 连接件
"""


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


"""
@File   : CanvasUnit.py
@Author : Ethan Lin
@Date   : 2022/06/19
@Desc   : 画布件
"""



@dataclass
class CanvasUnit(BaseUnit):
    """画布件"""

    type_name: str = 'canvas unit type'
    content: Content = Content(type_name='content type', head='canvas unit content head', body='canvas unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='canvas unit feedback sign content head', body='canvas unit feedback sign content body')

    index_pos: tuple[float, float, float] = (0.0, 0.0, 0.0)

    def show_color_content(self):  # TODO
        """
        显示颜色内容
        :return:
        :rtype:
        """

        self.feedback_sign = Content(type_name='connect feedback sign type', head='', body='showed')
        return self.feedback_sign
        pass  # class
