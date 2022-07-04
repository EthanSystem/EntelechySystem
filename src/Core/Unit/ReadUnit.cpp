//
// Created by Ethan on 2022/06/26.
//

#include "ReadUnit.h"


ReadUnit::ReadUnit(const std::string &unit_type_name,
                   const Content &feedback_sign,
                   const BaseUnit &baseUnit)
        : unit_type_name(unit_type_name),
          feedback_sign(feedback_sign),
          BaseUnit(baseUnit) {
}

Content ReadUnit::read_content(Content content) {
    feedback_sign = Content(
            "feed back sign",
            "",
            "read"
    );
    content = content;
    return feedback_sign;
}
