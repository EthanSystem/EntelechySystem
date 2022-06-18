cmake_minimum_required(VERSION 3.22)
project(EntelechySystem)

set(CMAKE_CXX_STANDARD 20)

include_directories("/usr/local/include/eigen3")
include_directories("/Applications/Julia-1.7.app/Contents/Resources/julia/include/julia")

add_executable(
        EntelechySystem
        main.cpp
        src/Unit/BaseUnit.cpp
        src/Unit/BaseUnit.h
        src/Unit/GateUnit.cpp
        src/Unit/GateUnit.h
        src/Unit/CanvasUnit.cpp
        src/Unit/CanvasUnit.h
        src/Tasks/TaskManager.cpp
        src/Tasks/TaskManager.h
        src/KnowledgeBase/KnowledgeManager.cpp
        src/KnowledgeBase/KnowledgeManager.h
        src/Neure/Neure.cpp src/Neure/Neure.h)

#cmake_minimum_required(VERSION 3.22)
#project(ElementalCognitionSystem)
#
#set(CMAKE_CXX_STANDARD 14)
#
#include_directories("/usr/local/include/eigen3")
#include_directories("/Applications/Julia-1.7.app/Contents/Resources/julia/include/julia")
#
#add_executable(ElementalCognitionSystem main.cpp src/Unit/BaseUnit.cpp src/Unit/BaseUnit.h src/Unit/GateUnit.cpp src/Unit/GateUnit.h src/Unit/CanvasUnit.cpp src/Unit/CanvasUnit.h src/Tasks/TaskManager.cpp src/Tasks/TaskManager.h src/Tasks/BaseTask.h)
#
#
##add_executable(rundraft rundraft.cpp)

