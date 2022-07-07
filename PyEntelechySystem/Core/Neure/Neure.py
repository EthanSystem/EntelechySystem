"""
@File   : Neure.py
@Author : Ethan Lin
@Date   : 2022/06/19
@Desc   : 
"""
from PyEntelechySystem.Core.Unit import *

@dataclass
class Neure(BaseObject):
    """神经元件"""

    type_name: str = 'neure type'
    """类型名称"""
    axon = None
    """轴突指针"""
    dendrite = list([])
    """树突连接"""
    synapse = list([])
    """突触id，数组指针"""
    index_pos: tuple[float, float, float] = (0.0, 0.0, 0.0)
    """位置"""

    # content: Content = Content(type_name='neure type', head='neure content head', body='neure content body')
    # feedback_sign: Content = Content(type_name='feedback sign type', head='canvas unit feedback sign content head', body='canvas unit feedback sign content body')
    # feedback_sign.uid = Content.set_uuid()

    def init_position(self, space_range: tuple):
        """
        初始化位置
        :param space_range:
        :type space_range:
        """
        pass
