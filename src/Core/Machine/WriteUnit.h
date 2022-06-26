//
// Created by Ethan on 2022/06/26.
//

#ifndef ENTELECHYSYSTEM_WRITEUNIT_H
#define ENTELECHYSYSTEM_WRITEUNIT_H


#include <string>

class WriteUnit {
private:
    std::string content_body;
    std::string feedback_sign;

public:
    /// 写入内容
    std::string write_content(std::string content);
};


#endif //ENTELECHYSYSTEM_WRITEUNIT_H
