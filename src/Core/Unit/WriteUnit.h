//
// Created by Ethan on 2022/06/26.
//

#ifndef ENTELECHYSYSTEM_WRITEUNIT_H
#define ENTELECHYSYSTEM_WRITEUNIT_H


#include <string>
#include "BaseUnit.h"

class WriteUnit:BaseUnit {
private:


public:
    /// 写入内容
    Content write_content(Content content);
};


#endif //ENTELECHYSYSTEM_WRITEUNIT_H
