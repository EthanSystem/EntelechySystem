//
// Created by Ethan on 2022/06/03.
//

#ifndef ENTELECHYSYSTEM_BASEUNIT_H
#define ENTELECHYSYSTEM_BASEUNIT_H

#include <iostream>
#include <vector>

using namespace std;

// 基准单元
class BaseUnit {
private: uint id; // 单元id
public: vector<uint> unit_interface; // 单元接口
};


#endif //ENTELECHYSYSTEM_BASEUNIT_H
