//
// Created by Ethan on 2022/07/03.
//

#ifndef ENTELECHYSYSTEM_CONTENT_H
#define ENTELECHYSYSTEM_CONTENT_H

#include <iostream>
#include "../Object/Object.h"


//class contentType;

class Content : Object {
//    Content(const Content& c);
private:

    std::string type_name;
    std::string content_head;
    std::string content_body;
    using Object::Object;
public:

    Content(const std::string &content_type_name,
            const std::string &content_head,
            const std::string &content_body
            /*const Object &object*/);

    const std::string &getContentTypeName() const;

    void setContentTypeName(const std::string &contentTypeName);

    const std::string &getContentHead() const;

    void setSignContentHead(const std::string &ContentHead);


    const std::string &getContentBody() const;

    void setContentBody(const std::string &ContentBody);


};


#endif //ENTELECHYSYSTEM_CONTENT_H
