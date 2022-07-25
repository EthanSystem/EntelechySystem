//
// Created by Ethan on 2022/06/26.
//

#ifndef ENTELECHYSYSTEM_READUNIT_H
#define ENTELECHYSYSTEM_READUNIT_H


#include "BaseUnit.h"

class ReadUnit : BaseUnit {
protected:
    std::string unit_type_name = "read unit type";
private:
    Content feedback_sign;
    using BaseUnit::BaseUnit;
public:
    ReadUnit(const std::string &unit_type_name,
             const Content &feedback_sign,
             const BaseUnit &baseUnit);

    Content read_content(Content content);


};


#endif //ENTELECHYSYSTEM_READUNIT_H
