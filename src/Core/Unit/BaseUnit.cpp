//
// Created by Ethan on 2022/06/03.
//

#include "BaseUnit.h"

BaseUnit::BaseUnit(const std::string &unit_type_name,
                   const Content &content,
                   const Content &feedback_sign,
                   const Object &object) :
        type_name(unit_type_name),
        content(content),
        feedback_sign(feedback_sign),
        Object(object) {

}
