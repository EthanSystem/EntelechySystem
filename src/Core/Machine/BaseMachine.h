//
// Created by Ethan on 2022/06/23.
//

#ifndef ENTELECHYSYSTEM_BASEMACHINE_H
#define ENTELECHYSYSTEM_BASEMACHINE_H

#include <iostream>
#include <boost/uuid/uuid.hpp>
#include <boost/uuid/uuid_io.hpp>
#include <boost/uuid/uuid_generators.hpp>

class BaseMachine {
private:
    /// 类型名称
    std::string type_name;
    /// id
    boost::uuids::uuid id = boost::uuids::random_generator()();
    /// id名称
    std::string uuid_string = boost::uuids::to_string(id);
};


#endif //ENTELECHYSYSTEM_BASEMACHINE_H
