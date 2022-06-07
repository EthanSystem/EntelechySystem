//
// Created by Ethan on 2022/06/04.
//

#ifndef ENTELECHYSYSTEM_TASKMANAGER_H
#define ENTELECHYSYSTEM_TASKMANAGER_H


class TaskManager {
    
    // TODO 初始化任务
    void initTask();
    // TODO 管理当前任务数
    void getNumOfTasks();
    // TODO 排序任务优先级
    void sortTask();
    // TODO 计算任务优先级
    void calcPriorityOfTask();
    // TODO 判定任务完成情况
    void decideTaskProcess();
    // TODO 调用任务扫描器，扫描内存中与外存中所有任务。
    void scheduleTasks();
};


#endif //ENTELECHYSYSTEM_TASKMANAGER_H
