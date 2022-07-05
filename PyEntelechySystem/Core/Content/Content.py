"""
@File   : BaseUnit.py
@Author : Ethan Lin
@Date   : 2022/07/05
@Desc   : 
"""
import uuid

from PyEntelechySystem.Core.Object.BaseObject import BaseObject


class Content(BaseObject):
    type_name: str = 'content type'

    content_head: str = ''
    content_body: str = ''

    def __init__(self, type_name, content_head='', content_body=''):
        super().__init__(self)
        self.type_name = type_name
        self.content_head = content_head
        self.content_body = content_body
        pass

    def set_content_body(self, content_body):
        self.content_body = content_body
        pass

    def set_content_head(self, content_head):
        self.content_head = content_head
        pass

    pass
