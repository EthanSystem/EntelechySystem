//
// Created by Ethan on 2022/06/24.
//

#include "Object.h"

std::string Object::get_type_name() {
    return this->type_name;
}

std::string Object::get_id() {
    return this->uuid_string;
}