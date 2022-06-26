//
// Created by Ethan on 2022/06/26.
//

#ifndef ENTELECHYSYSTEM_READUNIT_H
#define ENTELECHYSYSTEM_READUNIT_H


#include "../Object/Object.h"

class ReadUnit : Object {
private:
    std::string content_body;
    std::string feedback_sign;

public:
    std::string read_content(std::string content);




};


#endif //ENTELECHYSYSTEM_READUNIT_H
