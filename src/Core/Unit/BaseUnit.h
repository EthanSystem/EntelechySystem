//
// Created by Ethan on 2022/06/03.
//

#ifndef ENTELECHYSYSTEM_BASEUNIT_H
#define ENTELECHYSYSTEM_BASEUNIT_H

#include <iostream>
#include <vector>
#include "../Object/Object.h"
#include "ContentUnit.h"

using namespace std;

// 基准单元
class BaseUnit:Object {
protected:
    ContentUnit content_body;
    std::string feedback_sign;

public:
    vector<uint> unit_interface; // 单元接口
};


#endif //ENTELECHYSYSTEM_BASEUNIT_H
