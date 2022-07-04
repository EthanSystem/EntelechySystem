//
// Created by Ethan on 2022/06/24.
//

#include "Object.h"

//std::string Object::get_type_name() {
//    return this->object_type_name;
//}
//
//std::string Object::get_id() {
//    return this->id_string;
//}

Object::Object(const std::string &objectTypeName,
               const boost::uuids::uuid &id,
               const std::string &idString)
        : object_type_name(objectTypeName),
          id(id),
          id_string(idString) {
    this->id = boost::uuids::random_generator()();
    this->id_string = boost::uuids::to_string(id);
}

const std::string &Object::getTypeName() const {
    return object_type_name;
}

void Object::setTypeName(const std::string &typeName) {
    object_type_name = typeName;
}

const boost::uuids::uuid &Object::getId() const {
    return id;
}

void Object::setId(const boost::uuids::uuid &id) {
    Object::id = id;
}

const std::string &Object::getIdString() const {
    return id_string;
}

void Object::setIdString(const std::string &idString) {
    id_string = idString;
}

Object::Object() {}
