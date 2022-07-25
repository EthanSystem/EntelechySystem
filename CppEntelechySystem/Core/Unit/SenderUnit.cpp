//
// Created by Ethan on 2022/06/24.
//

#include <iostream>
#include "SenderUnit.h"

Content SenderUnit::send_content(Content content) {
    /// todo 对接管线
    content = content;
    feedback_sign="sent";
    return feedback_sign;
}
