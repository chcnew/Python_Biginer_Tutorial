import math
import random
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


def fit_fun(x):  # 测试函数
    res = np.sum(x ** 2)  # sphere函数，位置范围在[-100,100]
    # 20220513改进
    num_list = np.arange(1, x.shape[1] + 1)  # [1]
    val_list = [np.cos(x / np.sqrt(i)) for i in num_list]
    res = 1 + np.sum(x ** 2) / 4000 - np.prod(val_list)
    return res


# def getvalue(x):  # Griewank 函数,位置在[-600,600]
#     num_list = np.arange(1, x.shape[0] + 1)  # [1]
#     val_list = [np.cos(x / np.sqrt(i)) for i in num_list]
#     res = 1 + np.sum(x ** 2) / 4000 - np.prod(val_list)
#     return res


# def fit_fun(value):             # Rosenbrock 函数,位置在[-10,10]
#     d = value.shape[0]
#     res = np.sum(np.abs(100 * (value[1:] - value[:-1] ** 2) ** 2 + (1 - value[:-1]) ** 2))
#     return res

# def fit_fun(x):                 # Rastrigrin 函数,位置在[-5,5]
#     d = self.x.shape[0]
#     res = 10 * d + np.sum(self.x ** 2 - 10 * np.cos(2 * np.pi * self.x))
#     return res

# def getvalue(self):             # Griewank 函数,位置在[-600,600]
#     d = self.x.shape[0]
#     i = np.arange(1, d + 1)
#     res = 1 + np.sum(self.x ** 2) / 4000 - np.prod(np.cos(self.x / np.sqrt(i)))
#     return res

class Particle(object):  # 定义单个粒子
    # 初始化
    def __init__(self, x_max, max_vel, dim):  # 定义函数，括号中是形参
        self.__pos = np.random.uniform(-x_max, x_max, (1, dim))  # 粒子的位置
        self.__vel = np.random.uniform(-max_vel, max_vel, (1, dim))  # 粒子的速度
        self.__bestPos = np.zeros((1, dim))  # 粒子历史最优位置
        self.__fitnessValue = fit_fun(self.__pos)  # 种群最优适应值

    def set_pos(self, value):  # 粒子的位置（设置属性）
        self.__pos = value

    def get_pos(self):  # 粒子的位置（读取属性）
        return self.__pos

    def set_best_pos(self, value):  # 个体最优位置（设置属性）
        self.__bestPos = value

    def get_best_pos(self):  # 个体最优位置（读取属性）
        return self.__bestPos

    def set_vel(self, value):  # 粒子的速度（设置属性）
        self.__vel = value

    def get_vel(self):  # 粒子的速度（读取属性）
        return self.__vel

    def set_fitness_value(self, value):  # 个体最优适应值（设置属性）
        self.__fitnessValue = value

    def get_fitness_value(self):  # 个体最优适应值（读取属性)
        return self.__fitnessValue


class PSO(object):  # 定义种群  下面用part调用
    def __init__(self, dim, size, iter_num, x_max, max_vel, tol, best_fitness_value=float('Inf'), C1=2.05, C2=2.05, W=0.729):  # 定义函数的参数
        self.C1 = C1  # 自我学习因子
        self.C2 = C2  # 社会学习因子
        self.W = W  # 惯性权重
        self.dim = dim  # 种群的维度
        self.size = size  # 粒子个数
        self.iter_num = iter_num  # 迭代次数
        self.x_max = x_max  # 粒子最大位置
        self.max_vel = max_vel  # 粒子最大速度
        self.tol = tol  # 截至条件
        self.best_fitness_value = best_fitness_value  # 粒子适应值
        self.best_position = np.zeros((1, dim))  # 种群最优位置
        self.fitness_val_list = []  # 每次迭代最优适应值
        self.Particle_list = [Particle(self.x_max, self.max_vel, self.dim) for i in range(self.size)]  # 对种群进行初始化

    def set_bestFitnessValue(self, value):  # 种群最优适应值（设置属性)
        self.best_fitness_value = value

    def get_bestFitnessValue(self):  # 种群最优适应值(读取属性）
        return self.best_fitness_value

    def set_bestPosition(self, value):  # 种群最优位置（设置属性）
        self.best_position = value

    def get_bestPosition(self):  # 种群最优位置（读取属性）
        return self.best_position

    # 更新速度      第一、二、三条曲线的速度更新公式                                       # part是类里面的一个参数
    def update_vel(self, part):  # 粒子的新速度=w*当前速度+C1*R1*(个体最优位置-粒子当前位置）+C2*R2*(种群最优位置-粒子当前位置）
        vel_value = self.W * part.get_vel() + self.C1 * np.random.rand() * (part.get_best_pos() - part.get_pos()) + self.C2 * np.random.rand() * (self.get_bestPosition() - part.get_pos())
        vel_value[vel_value > self.max_vel] = self.max_vel  # 速度限制（新速度大于界限，速度边界赋值给新速度）
        vel_value[vel_value < -self.max_vel] = -self.max_vel  # 速度限制（新速度小于界限，速度边界赋值给新速度）
        part.set_vel(vel_value)  # 粒子的速度

    # 第一、二条曲线的更新位置，
    def update_pos(self, part):  # 更新粒子的新位置
        pos_value = part.get_pos() + part.get_vel()  # 新位置=当前位置+速度  （位置更新公式）
        part.set_pos(pos_value)  # 新位置
        value = fit_fun(part.get_pos())  # 新位置的适应值
        if value < part.get_fitness_value():  # 将粒子新位置对应的适应值与历史最优值相比较，如果新位置的适应值更优
            part.set_fitness_value(value)  # 更新 个体最优适应值
            part.set_best_pos(pos_value)  # 更新 个体最优位置
        if value < self.get_bestFitnessValue():  # 将粒子新位置对应的适应值与种群最优值相比较，如果新位置的适应值更优
            self.set_bestFitnessValue(value)  # 更新 种群最优适应值
            self.set_bestPosition(pos_value)  # 更新 种群最优位置

    # 第三条曲线的更新位置
    def update_pos3(self, part):  # 更新粒子的新位置
        pos_value = part.get_pos() + (0.1 + self.W) * part.get_vel()
        part.set_pos(pos_value)  # 新位置
        value = fit_fun(part.get_pos())  # 新位置的适应值
        if value < part.get_fitness_value():  # 将粒子新位置对应的适应值与历史最优值相比较，如果新位置的适应值更优
            part.set_fitness_value(value)  # 更新 个体最优适应值
            part.set_best_pos(pos_value)  # 更新 个体最优位置
        if value < self.get_bestFitnessValue():  # 将粒子新位置对应的适应值与种群最优值相比较，如果新位置的适应值更优
            self.set_bestFitnessValue(value)  # 更新 种群最优适应值
            self.set_bestPosition(pos_value)  # 更新 种群最优位置

    # 第一条曲线更新策略
    def update_dima(self):  # 定义函数dima
        # total_val = 0                                # 初始值=0（为104和108行，计算平均最优适应值)
        for i in range(self.iter_num):  # 对n个粒子进行循环
            for part in self.Particle_list:  # 粒子的循环
                self.update_vel(part)  # 更新速度
                self.update_pos(part)  # 更新位置
            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应值存到列表
            # print('第{}次最佳适应值为{}'.format(i, self.get_bestFitnessValue()))  # 输出 第{}次最佳适应值
            # total_val += self.get_bestFitnessValue()                            # 最优值相加存放
            if self.get_bestFitnessValue() < self.tol:  # 判断（如果最优适应值在误差范围内）
                break  # 结束循环
        # print('全部次数最佳适应平均值为{}\n'.format(total_val / self.iter_num))     # 输出 全部次数最佳适应平均值为{}
        return self.fitness_val_list, self.get_bestPosition()  # 结束更新每次迭代最优适应值值和种群最优位置

    # 第二条曲线的更新策略
    def update_dimb(self):  # 定义函数dimb
        total_val = 0  # 初始值=0（134行计算平均最优适应值)
        for i in range(self.iter_num):  # 对n个粒子进行循环
            for part in self.Particle_list:  # 粒子的循环
                self.update_vel(part)  # 更新速度
                self.update_pos(part)  # 更新位置

            # 每次迭代变化
            self.W = 0.9 - (0.9 - 0.4) * pow(i / self.iter_num, 0.5)
            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
            # print('第{}次最佳适应值为{}'.format(i, self.get_bestFitnessValue()))  # 输出 第{}次最佳适应值
            total_val += self.get_bestFitnessValue()  # 最优值相加存放
            if self.get_bestFitnessValue() < self.tol:  # 判断（如果最优适应值在误差范围内
                break  # 结束循环
        # print('全部次数最佳适应平均值为{}\n'.format(total_val / self.iter_num))  # 输出 全部次数最佳适应平均值为{}
        return self.fitness_val_list, self.get_bestPosition()  # 结束更新每次迭代最优适应值值和种群最优位置    # 第三条曲线的更新位置

    # 第三条曲线的更新策略
    def update_dimc(self):  # 定义函数dimb
        for i in range(self.iter_num):  # 对n个粒子进行循环
            for part in self.Particle_list:  # 粒子的循环
                self.update_vel(part)  # 更新速度
                self.update_pos3(part)  # 更新位置
            # 每次迭代变化
            self.W = (0.55 / 2) * math.cos(math.pi * i / self.iter_num) + (1.35 / 2)  # 第三条曲线的w的更新策略
            self.C1 = 0.5 * math.pow(self.W, 2) + self.W + 0.5  # 第三条曲线的c1的更新策略
            self.C2 = 2.5 - self.C1  # 第三条曲线的c2的更新策略
            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
            # print('第{}次最佳适应值为{}'.format(i, self.get_bestFitnessValue()))  # 输出 第{}次最佳适应值
            if self.get_bestFitnessValue() < self.tol:  # 判断（如果最优适应值在误差范围内
                break  # 结束循环
        return self.fitness_val_list, self.get_bestPosition()  # 结束更新每次迭代最优适应值值和种群最优位置


if __name__ == '__main__':  # 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行，当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    start = datetime.timestamp(datetime.now())

    pso1 = PSO(15, 30, 500, 100, 100, 1e-10, C1=2, C2=2, W=1)  # 曲线1的参数设置 pso
    pso2 = PSO(15, 30, 500, 100, 100, 1e-10, C1=2, C2=2, W=0.9)  # 曲线2的参数设置 压缩因子pso
    # 第0次传入值
    # w = 0.675
    # self.C1 = 0.5 * math.pow(self.W ,2) + self.W + 0.5
    # self.C2 = 2.5 - self.C1
    # print(c1, "\n", c2)
    pso3 = PSO(15, 30, 500, 100, 65, 1e-10, C1=1.4028125, C2=1.0971875, W=0.675)  # 曲线3的参数设置 对w和c1，c2进行改进
    fit_var_list1, best_pos1 = pso1.update_dima()  # 曲线一的最优解和最优值（依据函数dima更新）
    fit_var_list2, best_pos2 = pso2.update_dimb()  # 曲线二的最优解和最优值（依据函数dima更新）
    fit_var_list3, best_pos3 = pso3.update_dimc()  # 曲线三的最优解和最优值（依据函数dimc更新）
    print("曲线一最优位置:" + str(best_pos1))  # 输出曲线一最优位置
    print("曲线一最优解:" + str(fit_var_list1[-1]))  # 输出曲线一最优位置
    print("\n曲线二最优位置:" + str(best_pos2))  # 输出曲线二最优位置
    print("曲线二最优解:" + str(fit_var_list2[-1]))  # 输出曲线二最优解
    print("\n曲线三最优位置:" + str(best_pos3))  # 输出曲线三最优位置
    print("曲线三最优解:" + str(fit_var_list3[-1]))  # 输出曲线三最优解

    plt.figure(figsize=(8, 5))  # 设置图形的大小(图形的宽,图形的高）
    plt.plot(range(len(fit_var_list1)), fit_var_list1, alpha=0.5, color="red", label="基本pso")  # 曲线一
    plt.plot(range(len(fit_var_list2)), fit_var_list2, alpha=0.5, color="yellow", label="hpso")  # 曲线二
    plt.plot(range(len(fit_var_list3)), fit_var_list3, alpha=0.5, color="blue", label="改进pso")  # 曲线三
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
    plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符
    plt.rcParams['figure.figsize'] = (8.0, 4.0)  # 图像显示大小
    plt.title("Ackley函数对比图")  # 图片标题
    plt.xlabel("迭代次数")  # 图片x轴为迭代次数
    plt.ylabel("适应度")  # 图片y轴为适应度
    plt.legend()  # 给图片加图例
    plt.savefig("./outpic0.png", dpi=300)  # 输出图片
    plt.show()  # 输出图片

    end = datetime.timestamp(datetime.now())
    print("运行时间：" + str(round(end - start, 2)))
