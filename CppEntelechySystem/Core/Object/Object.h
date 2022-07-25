//
// Created by Ethan on 2022/06/24.
//

#ifndef ENTELECHYSYSTEM_OBJECT_H
#define ENTELECHYSYSTEM_OBJECT_H

#include <istream>
#include <boost/uuid/uuid.hpp>
#include <boost/uuid/uuid_io.hpp>
#include <boost/uuid/uuid_generators.hpp>

/*
 * 基对象类，生成id与id名称。
 */
class Object {
private:
    /// 类型名称
    std::string object_type_name = "object type";
    /// id值
    boost::uuids::uuid id;
//    boost::uuids::uuid id = boost::uuids::random_generator()();

    /// id名称
    std::string id_string;
//    std::string id_string = boost::uuids::to_string(id);

public:
    Object(const std::string &objectTypeName,
           const boost::uuids::uuid &id,
           const std::string &idString);

    Object();

    const std::string &getTypeName() const;

    void setTypeName(const std::string &typeName);

    const boost::uuids::uuid &getId() const;

    void setId(const boost::uuids::uuid &id);

    const std::string &getIdString() const;

    void setIdString(const std::string &idString);


public:
//    /// 设置类型名称
//    virtual std::string set_type_name();
//
//    /// 获取类型名称
//    std::string get_type_name();
//
//    /// 获取id
//    std::string get_id();
};


#endif //ENTELECHYSYSTEM_OBJECT_H
