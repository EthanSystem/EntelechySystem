//
// Created by Ethan on 2022/06/24.
//

#ifndef ENTELECHYSYSTEM_SENDERUNIT_H
#define ENTELECHYSYSTEM_SENDERUNIT_H


#include "BaseUnit.h"

/**
 * 发送部件
 */
class SenderUnit : BaseUnit {
private:


public:
    /// todo 发送内容
    Content send_content(Content content);

};


#endif //ENTELECHYSYSTEM_SENDERUNIT_H
