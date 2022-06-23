//
// Created by Ethan on 2022/06/24.
//

#ifndef ENTELECHYSYSTEM_OBJECT_H
#define ENTELECHYSYSTEM_OBJECT_H

#include <istream>
#include <boost/uuid/uuid.hpp>
#include <boost/uuid/uuid_io.hpp>
#include <boost/uuid/uuid_generators.hpp>

class Object {
private:
    /// 类型名称
    std::string type_name;
    /// id
    boost::uuids::uuid id = boost::uuids::random_generator()();
    /// id名称
    std::string uuid_string = boost::uuids::to_string(id);
public:
    /// 设置类型名称
    virtual void set_type_name();

    /// 获取类型名称
    std::string get_type_name();
};


#endif //ENTELECHYSYSTEM_OBJECT_H
