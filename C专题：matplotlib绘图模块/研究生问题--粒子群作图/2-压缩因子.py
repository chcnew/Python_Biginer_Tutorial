import math
import random
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


def fit_fun(x):  # 适应函数
    # return sum(100.0 * (x[0][1:] - x[0][:-1] ** 2.0) ** 2.0 + (1 - x[0][:-1]) ** 2.0)
    # y = np.sum(np.abs(x)) + np.prod(np.abs(x))
    # return y
    res = np.sum(x ** 2)
    return res


class Particle(object):
    # 初始化
    def __init__(self, x_max, max_vel, dim):
        self.__pos = np.random.uniform(-x_max, x_max, (1, dim))  # 粒子的位置
        self.__vel = np.random.uniform(-max_vel, max_vel, (1, dim))  # 粒子的速度
        self.__bestPos = np.zeros((1, dim))  # 粒子最好的位置
        self.__fitnessValue = fit_fun(self.__pos)  # 适应度函数值

    def set_pos(self, value):  # 新的 粒子位置
        self.__pos = value

    def get_pos(self):  # 粒子当前位置
        return self.__pos

    def set_best_pos(self, value):  # 新的 个体最优位置
        self.__bestPos = value

    def get_best_pos(self):  # 个体最优位置
        return self.__bestPos

    def set_vel(self, value):  # 粒子新速度
        self.__vel = value

    def get_vel(self):  # 粒子当前速度
        return self.__vel

    def set_fitness_value(self, value):  # 种群最优适应值
        self.__fitnessValue = value

    def get_fitness_value(self):  # 个体历史最优适应值
        return self.__fitnessValue


class PSO(object):
    def __init__(self, dim, size, iter_num, x_max, max_vel, tol, best_fitness_value=float('Inf'), C1=2.05, C2=2.05, W=0.729):
        self.C1 = C1  # 自我学习因子
        self.C2 = C2  # 社会学习因子
        self.W = W  # 惯性权重
        self.dim = dim  # 粒子的维度
        self.size = size  # 粒子个数
        self.iter_num = iter_num  # 迭代次数
        self.x_max = x_max  # 粒子最大位置
        self.max_vel = max_vel  # 粒子最大速度
        self.tol = tol  # 截至条件
        self.best_fitness_value = best_fitness_value  # 粒子适应值
        self.best_position = np.zeros((1, dim))  # 种群最优位置
        self.fitness_val_list = []  # 每次迭代最优适应值
        self.Particle_list = [Particle(self.x_max, self.max_vel, self.dim) for i in range(self.size)]  # 对种群进行初始化

    def set_bestFitnessValue(self, value):  # 种群最优适应值
        self.best_fitness_value = value

    def get_bestFitnessValue(self):  # 获取个体最优位置
        return self.best_fitness_value

    def set_bestPosition(self, value):  # 种群最优适应值
        self.best_position = value

    def get_bestPosition(self):  # 种群最优位置
        return self.best_position

    # 更新速度
    def update_vel(self, part):  # 粒子新速度=w*当前速度+C1*R1*(个体最优位置-粒子当前位置）+C2*R2*(种群最优位置-粒子当前位置）
        vel_value = self.W * part.get_vel() + self.C1 * np.random.rand() * (
                part.get_best_pos() - part.get_pos()) + self.C2 * np.random.rand() * (
                            self.get_bestPosition() - part.get_pos())
        vel_value[vel_value > self.max_vel] = self.max_vel  # 速度限制 粒子新速度大于界限，速度边界赋值给新速度
        vel_value[vel_value < -self.max_vel] = -self.max_vel  # 速度限制 粒子新速度小于界限，速度边界赋值给新速度
        part.set_vel(vel_value)

    # 更新位置
    def update_pos(self, part):  # 更新粒子的新位置
        pos_value = part.get_pos() + part.get_vel()  # 新位置=当前位置+速度  位置更新公式
        part.set_pos(pos_value)  # 新位置的适应值
        value = fit_fun(part.get_pos())  # 新位置的适应值
        if value < part.get_fitness_value():  # 将粒子新位置对应的适应值与历史最优值相比较，如果新位置的适应值较小
            part.set_fitness_value(value)  # 更新 新的个体最优适应值
            part.set_best_pos(pos_value)  # 更新 新的个体最优位置
        if value < self.get_bestFitnessValue():  # 将粒子新位置对应的适应值与历史最优值相比较，如果新位置的适应值较小
            self.set_bestFitnessValue(value)  # 更新 新的种群最优适应值
            self.set_bestPosition(pos_value)  # 更新 新的种群最优位置

    def update_dima(self):
        total_val = 0
        for i in range(self.iter_num):
            for part in self.Particle_list:
                self.update_vel(part)  # 更新速度
                self.update_pos(part)  # 更新位置
                vel = part.get_vel()
                pos = part.get_pos()

            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
            print('第{}次最佳适应值为{}'.format(i, self.get_bestFitnessValue()))
            total_val += self.get_bestFitnessValue()  # 最优值相加存放

            if self.get_bestFitnessValue() < self.tol:
                break
        print('全部次数最佳适应平均值为{}\n'.format(total_val / self.iter_num))
        return self.fitness_val_list, self.get_bestPosition()

    def update_dimb(self):
        total_val = 0
        for i in range(self.iter_num):
            for part in self.Particle_list:
                self.update_vel(part)  # 更新速度
                self.update_pos(part)  # 更新位置
                vel = part.get_vel()
                pos = part.get_pos()
            # 每次迭代变化
            self.W = 0.9 - (0.9 - 0.4) * (i / self.iter_num)
            self.C1 = 1.3 + 1.2 * math.cos(self.W / self.iter_num)
            self.C2 = 2 - 1.2 * math.cos(self.W / self.iter_num)

            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
            print('第{}次最佳适应值为{}'.format(i, self.get_bestFitnessValue()))
            total_val += self.get_bestFitnessValue()  # 最优值相加存放

            if self.get_bestFitnessValue() < self.tol:
                break
        print('全部次数最佳适应平均值为{}\n'.format(total_val / self.iter_num))
        return self.fitness_val_list, self.get_bestPosition()


if __name__ == '__main__':
    pso1 = PSO(9, 30, 200, 10, 10, 1e-10, C1=2, C2=2, W=1)
    pso2 = PSO(9, 30, 200, 10, 10, 1e-10, C1=2.05, C2=2.05, W=0.792)
    # 第0次传入值
    # w = 0.9
    # c1 = 1.3 + 1.2 * math.cos(0.9 / 200)
    # c2 = 2 - 1.2 * math.cos(0.9 / 200)
    # print(c1, "\n", c2)

    pso3 = PSO(9, 30, 200, 10, 10, 1e-10, C1=2.499987850020503, C2=0.800012149979497, W=0.9)

    fit_var_list1, best_pos1 = pso1.update_dima()
    fit_var_list2, best_pos2 = pso2.update_dima()
    fit_var_list3, best_pos3 = pso3.update_dimb()
    print("曲线一最优位置:" + str(best_pos1))
    print("曲线一最优解:" + str(fit_var_list1[-1]))
    print("曲线二最优位置:" + str(best_pos2))
    print("曲线二最优解:" + str(fit_var_list2[-1]))
    print("曲线三最优位置:" + str(best_pos3))
    print("曲线三最优解:" + str(fit_var_list3[-1]))

    plt.figure(figsize=(12, 8))
    plt.plot(range(len(fit_var_list1)), fit_var_list1, alpha=0.5, color="red", label="基本pso")
    plt.plot(range(len(fit_var_list2)), fit_var_list2, alpha=0.5, color="yellow", label="压缩因子pso")
    plt.plot(range(len(fit_var_list3)), fit_var_list3, alpha=0.5, color="blue", label="变异学习因子PSO")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 显示手动设置
    plt.rcParams['figure.figsize'] = (8.0, 4.0)
    plt.title("Ackley函数对比图")
    plt.xlabel("迭代次数")
    plt.ylabel("适应度")
    # plt.annotate(
    #     text='曲线一',  # 注释文本内容
    #     xy=(7, 12),  # 注释的坐标点
    #     xytext=(40, 40),  # 注释文字的始末位置
    #     textcoords='offset points',
    #     color="r",
    #     fontsize=16,
    #     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=.2', alpha=0.6, facecolor='#74C476')
    # )
    # plt.annotate(
    #     text='曲线二',  # 注释文本内容
    #     xy=(7, 12),  # 注释的坐标点
    #     xytext=(80, 80),  # 注释文字的始末位置
    #     textcoords='offset points',
    #     color="r",
    #     fontsize=16,
    #     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=.2', alpha=0.6, facecolor='#74C476')
    # )
    # plt.annotate(
    #     text='曲线三',  # 注释文本内容
    #     xy=(7, 12),  # 注释的坐标点
    #     xytext=(120, 120),  # 注释文字的始末位置
    #     textcoords='offset points',
    #     color="r",
    #     fontsize=16,
    #     arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=.2', alpha=0.6, facecolor='#74C476')
    # )
    plt.legend()
    plt.show()
