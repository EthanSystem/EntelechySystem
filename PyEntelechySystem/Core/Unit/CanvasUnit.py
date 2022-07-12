"""
@File   : CanvasUnit.py
@Author : Ethan Lin
@Date   : 2022/06/19
@Desc   : 画布件
"""

from PyEntelechySystem.Core.Unit import *


@dataclass
class CanvasUnit(BaseUnit):
    """画布件"""

    type_name: str = 'canvas unit type'
    content: Content = Content(type_name='content type', head='canvas unit content head', body='canvas unit content body')
    feedback_sign: Content = Content(type_name='feedback sign type', head='canvas unit feedback sign content head', body='canvas unit feedback sign content body')

    index_pos: tuple[float, float, float] = (0.0, 0.0, 0.0)

    def show_color_content(self):# TODO
        """
        显示颜色内容
        :return:
        :rtype:
        """


        self.feedback_sign = Content(type_name='connect feedback sign type', head='', body='showed')
        return self.feedback_sign
        pass  # class

