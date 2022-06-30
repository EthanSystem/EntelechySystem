//
// Created by Ethan on 2022/06/26.
//

#ifndef ENTELECHYSYSTEM_ADDRESSUNIT_H
#define ENTELECHYSYSTEM_ADDRESSUNIT_H


#include <string>
#include "BaseUnit.h"

class AddressUnit:BaseUnit {
private:


public:
    void address_content();


    void address_content(std::list<int> content);
};


#endif //ENTELECHYSYSTEM_ADDRESSUNIT_H
