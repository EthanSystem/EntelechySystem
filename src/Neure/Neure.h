//
// Created by Ethan on 2022/06/18.
//

#ifndef ENTELECHYSYSTEM_NEURE_H
#define ENTELECHYSYSTEM_NEURE_H

#include <iostream>

using namespace std;

template <class type>
class Neure {
private:
    unsigned int id;
    string type;
    unsigned int *axon; // 轴突连接数组指针
    unsigned int *dendrite; // 树突连接数组指针
};


#endif //ENTELECHYSYSTEM_NEURE_H
