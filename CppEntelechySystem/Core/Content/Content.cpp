//
// Created by Ethan on 2022/07/03.
//

#include "Content.h"


void
Content::setSignContentHead(const std::string &ContentHead) {
    this->content_head = ContentHead;
}


const std::string &Content::getContentBody() const {
    return this->content_body;
}

void Content::setContentBody(const std::string &ContentBody) {
    this->content_body = ContentBody;
}


Content::Content(
        const std::string &content_type_name,
        const std::string &content_head,
        const std::string &content_body
        /*const Object &object*/)
        : type_name(content_type_name),
          content_head(content_head),
          content_body(content_body)
          /*Object(object)*/ {}

const std::string &Content::getContentHead() const {
    return content_head;
}

const std::string &Content::getContentTypeName() const {
    return type_name;
}

void Content::setContentTypeName(const std::string &contentTypeName) {
    type_name = contentTypeName;
}










