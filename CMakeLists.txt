cmake_minimum_required(VERSION 3.22)
project(EntelechySystem)

set(CMAKE_CXX_STANDARD 20)


#if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#    conan_basic_setup()
#else()
#    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
#endif()


#set(BOOST_ROOT "/usr/local/include/boost")

#让Clion自动寻找boost
find_package(Boost 1.79.0 COMPONENTS system filesystem REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})

#include_directories("/usr/local/include/eigen3")
#include_directories("/usr/local/include/boost")
#include_directories("/Applications/Julia-1.7.app/Contents/Resources/julia/include/julia")

## 手动配置搜索路径

#添加头文件搜索路径
include_directories(/usr/local/include)

#添加库文件搜索路径
link_directories(/usr/local/lib)

#用于将当前目录下的所有源文件的名字保存在变量 DIR_SRCS 中
aux_source_directory(. DIR_SRCS)


#在这里根据名字boost_thread去寻找libboost_thread.a文件
#target_link_libraries(demo boost_thread boost_system)


add_executable(
        EntelechySystem
        ${DIR_SRCS}
        src/main.cpp
        src
        src/Core
        src/Core/Tasks
        src/Core/Unit/BaseUnit.cpp
        src/Core/Unit/BaseUnit.h
        src/Core/Unit/GateUnit.cpp
        src/Core/Unit/GateUnit.h
        src/Core/Unit/CanvasUnit.cpp
        src/Core/Unit/CanvasUnit.h
        src/Core/Tasks/TaskManager.cpp
        src/Core/Tasks/TaskManager.h
        src/Core/KnowledgeBase/KnowledgeManager.cpp
        src/Core/KnowledgeBase/KnowledgeManager.h
        src/Core/Neure/Neure.cpp
        src/Core/Neure/Neure.h
        src/World/CreateNeuroNetwork.cpp
        src/World/CreateNeuroNetwork.h
        src/Core/Tasks/Task.cpp
        src/Core/Tasks/Task.h
        src/Core/Lingo/Lingo.cpp
        src/Core/Lingo/Lingo.h
        src/Core/Storage.cpp
        src/Core/Storage.h
        src/Core/Machine/NeedsPerceptionMachine.cpp
        src/Core/Machine/NeedsPerceptionMachine.h
        src/Core/Machine/BaseMachine.cpp
        src/Core/Machine/BaseMachine.h
        src/Core/Object/Object.cpp src/Core/Object/Object.h src/Core/Unit/SenderUnit.cpp src/Core/Unit/SenderUnit.h src/Core/Unit/ReceiverUnit.cpp src/Core/Unit/ReceiverUnit.h src/Core/Agent/Agent.cpp src/Core/Agent/Agent.h src/Core/Unit/ReadUnit.cpp src/Core/Unit/ReadUnit.h src/Core/Unit/WriteUnit.cpp src/Core/Unit/WriteUnit.h src/Core/Unit/AddressUnit.cpp src/Core/Unit/AddressUnit.h src/Core/Unit/ContentUnit.cpp src/Core/Unit/ContentUnit.h)


