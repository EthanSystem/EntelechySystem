#include <iostream>
#include <ctime>
#include "Core/Tasks/Task.h"

/**
 * 主程序。简单的世界模拟器，用于初始化和运行模型。
 * @return
 */
int main() {
    /// 设置：总步数
    int totol_step = 1000;
    /// 设置阶段步数
    int delta_step = 100;
    int start_step = 0;
    int finish_step = start_step + totol_step;
    clock_t start_time, finish_time;

    // 定时开始
    start_time = clock();

    /// 初始化模型 ==========

    // TODO

    /// =========================


    // 运行程序，一直到设定的停时为止
    for (int current_step = 0; current_step < finish_step; ++current_step) {

        if (current_step % delta_step == 0) {
            std::cout << "步：" << current_step << endl;
        }

        /// 运行系统模型 ==========


        /// =========================

    }

    // 定时结束
    finish_time = clock();

    std::cout << "耗时：" << finish_time - start_time << endl;

}



