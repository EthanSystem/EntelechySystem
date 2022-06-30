//
// Created by Ethan on 2022/06/24.
//

#include <iostream>
#include "SenderUnit.h"

std::string SenderUnit::send_content(std::string content) {
    /// todo 对接管线
    content = content_body;
    feedback_sign="sent";
    return feedback_sign;
}
