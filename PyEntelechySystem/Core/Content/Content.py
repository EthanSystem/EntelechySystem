"""
@File   : BaseUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""

from PyEntelechySystem import *

from PyEntelechySystem.Core.Object.BaseObject import BaseObject


@dataclass
class Content(BaseObject):
    type_name: str = 'content type'

    # head: str
    # body: str

    # def __init__(self, type_name, head='', body=''):
    #     super().__init__(self)
    #     self.type_name = type_name
    #     self.head = head
    #     self.body = body
    #     pass

    # type_name: str = 'content type'
    # head: str = 'content head'
    # body: str = 'content body'

    def __init__(self, *args, **kwargs):
        # self.type_name: str = 'content type'
        # self.head: str = 'content head'
        # self.body: str = 'content body'
        self.uid: uuid = uuid.uuid4()
        self.uid_string = self.uid.__str__()
        self.type_name: str = kwargs.get('type_name')
        self.head: str = kwargs.get('head')
        self.body: str = kwargs.get('body')
        super().__init__()
        pass

    def set_content_body(self, content_body):
        self.body = content_body
        pass

    def set_content_head(self, content_head):
        self.head = content_head
        pass

    pass
