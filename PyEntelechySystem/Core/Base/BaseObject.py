"""
@File   : BaseObject.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

from PyEntelechySystem import dataclass,uuid


@dataclass()
class BaseObject:
    """
    基对象类，生成id与id名称。
    """

    type_name = 'base object type'
    uid = uuid.uuid4()
    uid_string = 'str: ' + uid.__str__()


    # def __int__(self, *args, **kwargs):
    #     self.type_name = 'base object type'
    #     self.uid = uuid.uuid4()
    #     self.uid_string = self.uid.__str__()
    #     pass

    pass
