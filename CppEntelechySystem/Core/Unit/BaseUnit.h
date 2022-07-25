//
// Created by Ethan on 2022/06/03.
//

#ifndef ENTELECHYSYSTEM_BASEUNIT_H
#define ENTELECHYSYSTEM_BASEUNIT_H

#include <iostream>
#include <vector>
#include "../Object/Object.h"
#include "../Content/Content.h"


/** 基准单元
 *
 */
class BaseUnit : Object {
private:
    std::string type_name = "unit type";
    Content content;
    Content feedback_sign;
    using Object::Object;

public:

    BaseUnit(const std::string &unit_type_name,
             const Content &content,
             const Content &feedback_sign,
             const Object &object);

    std::vector <uint> unit_interface; // 单元接口
};


#endif //ENTELECHYSYSTEM_BASEUNIT_H
