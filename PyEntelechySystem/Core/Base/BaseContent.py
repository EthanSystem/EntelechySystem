"""
@File   : BaseContent.py
@Author : Ethan Lin
@Date   : 2022/07/07
@Desc   : 
"""

from PyEntelechySystem import dataclass, uuid

from PyEntelechySystem.Core.Base.BaseObject import BaseObject


@dataclass()
class BaseContent(BaseObject):
    """
    内容对象
    """

    uid: uuid = uuid.uuid4()
    uid_string: str = uid.__str__()
    type_name: str = 'base content type'
    head: str = 'base content head'
    body: str = 'base content body'

    # def __init__(self, *args, **kwargs):
    #     # self.type_name: str = 'content type'
    #     # self.head: str = 'content head'
    #     # self.body: str = 'content body'
    #     self.uid: uuid = uuid.uuid4()
    #     self.uid_string = self.uid.__str__()
    #     self.type_name: str = kwargs.get('type_name')
    #     self.head: str = kwargs.get('head')
    #     self.body: str = kwargs.get('body')
    #     super().__init__()
    #     pass

    @classmethod
    def set_uuid(self):
        self.uid = uuid.uuid4()
        return self.uid
        pass

    def set_content_body(self, body):
        self.body = body
        pass

    def set_content_head(self, head):
        self.head = head
        pass

    pass
