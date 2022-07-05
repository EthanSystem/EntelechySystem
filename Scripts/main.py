import time

if __name__ == "__main__":

    print("hello world")
    ## 设置：总步数
    totol_step = 1000
    ## 设置阶段步数
    delta_step = 100
    start_step = 0
    finish_step = start_step + totol_step

    ## 定时开始
    start_time = time.time()

    ## TODO 初始化模型 ==========

    ## =========================

    ## 运行程序，一直到设定的停时为止
    for current_step in range(finish_step):

        if (current_step % delta_step == 0):
            print("步：", current_step)

        ## TODO 运行系统模型 ==========

        ## =========================

    ## 定时结束
    finish_time = time.time()

    print("耗时：", finish_time - start_time)
