//
// Created by Ethan on 2022/06/18.
//

#ifndef ENTELECHYSYSTEM_NEURE_H
#define ENTELECHYSYSTEM_NEURE_H

#include <iostream>


using namespace std;

class Neure {
private:
    unsigned int id;
    string type;
    unsigned int *axon; // 轴突连接id，数组指针
    unsigned int *dendrite; // 树突连接id，数组指针
    unsigned int *synapse; // 突触id，数组指针


public:
    int setNeureId();

    string setNeureType();

    unsigned int *setAxonId();

    unsigned int *setDendrite();
};


#endif //ENTELECHYSYSTEM_NEURE_H
