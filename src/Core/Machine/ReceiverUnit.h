//
// Created by Ethan on 2022/06/24.
//

#ifndef ENTELECHYSYSTEM_RECEIVERUNIT_H
#define ENTELECHYSYSTEM_RECEIVERUNIT_H


#include <iostream>

class ReceiverUnit {
private:
    std::string content_body;
    std::string feedback_sign;

public:
    /// 接收内容
    std::string receive_content(std::string content);

};


#endif //ENTELECHYSYSTEM_RECEIVERUNIT_H
