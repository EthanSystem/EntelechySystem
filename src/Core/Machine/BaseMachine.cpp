//
// Created by Ethan on 2022/06/23.
//

#include "BaseMachine.h"

void Object::set_type_name() {
    this->type_name="machine";
}

SenderMachine BaseMachine::senderMachine() {
    return SenderMachine();
}

ReceiverMachine BaseMachine::receiverMachine() {
    return ReceiverMachine();
}
