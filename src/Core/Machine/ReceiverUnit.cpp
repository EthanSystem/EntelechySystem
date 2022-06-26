//
// Created by Ethan on 2022/06/24.
//

#include "ReceiverUnit.h"

#include <utility>

std::string ReceiverUnit::receive_content(std::string content) {
    /// TODO 对接管线
    content_body = content;
    feedback_sign = "received";
    return feedback_sign;
}
