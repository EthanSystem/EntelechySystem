"""
@File   : Object.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

import uuid


class BaseObject:
    """
    基对象类，生成id与id名称。
    """

    type_name: str = 'object type'

    id: uuid = uuid.uuid4()

    id_string: str = id.__str__()

    def __int__(self, type_name, id):
        self.type_name = type_name
        self.id = id
        pass



    pass
