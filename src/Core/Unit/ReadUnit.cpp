//
// Created by Ethan on 2022/06/26.
//

#include "ReadUnit.h"

std::string ReadUnit::read_content(std::string content) {
    feedback_sign="read";
    content_body=content;
    return feedback_sign;
}
