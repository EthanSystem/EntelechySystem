"""
@File   : Object.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

from PyEntelechySystem import *


class BaseObject:
    """
    基对象类，生成id与id名称。
    """

    type_name = 'base object type'
    uid = uuid.uuid4()
    uid_string = 'str: ' + uid.__str__()
    # type_name:str
    # uid:uuid
    # uid_string:str

    def __int__(self, *args, **kwargs):
        self.type_name = 'base object type'
        self.uid = uuid.uuid4()
        self.uid_string = self.uid.__str__()
        pass

    pass
