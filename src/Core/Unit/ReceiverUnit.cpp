//
// Created by Ethan on 2022/06/24.
//

#include "ReceiverUnit.h"

#include <utility>

Content ReceiverUnit::receive_content(Content content) {
    // todo 对接管线
    content = content;
    feedback_sign = "received";
    return feedback_sign;
}
