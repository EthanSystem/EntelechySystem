//
// Created by Ethan on 2022/06/23.
//

#ifndef ENTELECHYSYSTEM_NEEDSMACHINE_H
#define ENTELECHYSYSTEM_NEEDSMACHINE_H

#include "../Unit/BaseMachine.h"

/**
 * 感知需求机
 */
class NeedsMachine : BaseMachine {
public:
    Content SendNeeds(Content needsContent);


};


#endif //ENTELECHYSYSTEM_NEEDSMACHINE_H
