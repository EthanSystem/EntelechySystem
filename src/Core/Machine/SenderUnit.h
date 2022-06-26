//
// Created by Ethan on 2022/06/24.
//

#ifndef ENTELECHYSYSTEM_SENDERUNIT_H
#define ENTELECHYSYSTEM_SENDERUNIT_H


#include "../Object/Object.h"
/**
 * 发送部件
 */
class SenderUnit : public Object {
private:
    std::string content_body;
    std::string feedback_sign;

public:
    /// todo 发送内容
    std::string send_content(std::string content);

};


#endif //ENTELECHYSYSTEM_SENDERUNIT_H
