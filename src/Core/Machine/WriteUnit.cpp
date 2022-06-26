//
// Created by Ethan on 2022/06/26.
//

#include "WriteUnit.h"

std::string WriteUnit::write_content(std::string content) {
    content_body = content;
    feedback_sign = "wrote";
    return feedback_sign;
}
