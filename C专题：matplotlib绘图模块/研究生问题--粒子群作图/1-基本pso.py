import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fit_fun(x):  # 适应函数
    # return sum(100.0 * (x[0][1:] - x[0][:-1] ** 2.0) ** 2.0 + (1 - x[0][:-1]) ** 2.0)
    # y = np.sum(np.abs(x)) + np.prod(np.abs(x))
    # return y
    res = np.sum(x ** 2)
    return res


# res = np.sum(np.abs(x)) + np.prod(np.abs(x))
# return res

class Particle:
    # 初始化
    def __init__(self, x_max, max_vel, dim, ):
        self.__pos = np.random.uniform(-x_max, x_max, (1, dim))  # 粒子的位置
        self.__vel = np.random.uniform(-max_vel, max_vel, (1, dim))  # 粒子的速度
        self.__bestPos = np.zeros((1, dim))  # 粒子最好的位置
        self.__fitnessValue = fit_fun(self.__pos)  # 适应度函数值

    def set_pos(self, value):  # 新的 粒子位置  （属性设置为可修改）
        self.__pos = value

    def get_pos(self):  # 粒子当前位置   （属性设置为可读）
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


class PSO:
    def __init__(self, dim, size, iter_num, x_max, max_vel, tol, best_fitness_value=float('Inf'), C1=2, C2=2, W=1):
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

        # 对种群进行初始化
        self.Particle_list = [Particle(self.x_max, self.max_vel, self.dim) for i in range(self.size)]

    def set_bestFitnessValue(self, value):  # 种群最优适应值
        self.best_fitness_value = value

    def get_bestFitnessValue(self):  # 个体最优位置
        return self.best_fitness_value

    def set_bestPosition(self, value):  # 种群最优适应值
        self.best_position = value

    def get_bestPosition(self):  # 种群最优位置
        return self.best_position

    # 更新速度
    def update_vel(self, part):  # 粒子新速度=w*当前速度+C1*R1*(个体最优位置-粒子当前位置）+C2*R2*(种群最优位置-粒子当前位置）
        vel_value = (self.W * part.get_vel()) + self.C1 * np.random.rand() * (part.get_best_pos() - part.get_pos()) \
                    + self.C2 * np.random.rand() * (self.get_bestPosition() - part.get_pos())
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

    def update_ndim(self):

        for i in range(self.iter_num):
            for part in self.Particle_list:
                self.update_vel(part)  # 更新速度
                self.update_pos(part)  # 更新位置
            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
            print('第{}次最佳适应值为{}'.format(i, self.get_bestFitnessValue()))
            if self.get_bestFitnessValue() < self.tol:
                break

        return self.fitness_val_list, self.get_bestPosition()  # 最优适应值列表，最优位置


if __name__ == '__main__':
    # (dim, size, iter_num, x_max, max_vel, tol, best_fitness_value=float('Inf'), C1=2, C2=2)
    pso1 = PSO(9, 20, 300, 10, 10, 1e-15, C1=2, C2=2, W=1)
    pso2 = PSO(9, 30, 310, 15, 15, 1e-15, C1=2, C2=2, W=1)
    # pso2 = PSO(20, 50, 500, 30, 50, 1e-100, C1=2.05, C2=2.05, W=0.729)
    fit_var_list1, best_pos1 = pso1.update_ndim()
    fit_var_list2, best_pos2 = pso2.update_ndim()
    # print("最优位置:" + str(best_pos))
    # print("最优解:" + str(fit_var_list[-1]))
    plt.plot(range(len(fit_var_list1)), fit_var_list1, alpha=0.5)
    plt.plot(range(len(fit_var_list2)), fit_var_list2, alpha=0.5)
    plt.show()
