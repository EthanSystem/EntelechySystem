"""
@File   : NeedMachine.py
@Author : Ethan Lin
@Date   : 2022/06/19
@Desc   : 
"""

from PyEntelechySystem.Core.Machine import *

@dataclass
class NeedMachine:
    """
    需求机
    """

    # NOW

    # 接收需求信号
    def receive_want_to_need_sign(self):
        pass

    # 发送需求
    def send_need(self):
        pass

    pass