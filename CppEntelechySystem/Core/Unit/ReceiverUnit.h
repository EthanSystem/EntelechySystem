//
// Created by Ethan on 2022/06/24.
//

#ifndef ENTELECHYSYSTEM_RECEIVERUNIT_H
#define ENTELECHYSYSTEM_RECEIVERUNIT_H


#include <iostream>
#include "BaseUnit.h"

class ReceiverUnit:BaseUnit {
private:


public:
    /// 接收内容
    Content receive_content(Content content);

};


#endif //ENTELECHYSYSTEM_RECEIVERUNIT_H
