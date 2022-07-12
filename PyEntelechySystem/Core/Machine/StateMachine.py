"""
@File   : StateMachine.py
@Author : Ethan Lin
@Date   : 2022/07/12
@Desc   : 
"""

from PyEntelechySystem.Core.Machine import *


@dataclass
class StateMachine:
    """
    状态机
    """

    # 接收状态信号 TODO
    def receive_state_sign(self):
        pass

    # 发送当前状态 TODO
    def send_current_state(self):
        pass

    pass  # class
