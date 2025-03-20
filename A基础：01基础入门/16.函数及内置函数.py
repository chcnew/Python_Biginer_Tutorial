# -*- coding: utf-8 -*-

# =======遇讯录管理系统======
# 1、增加姓名和手机
# 2、删除姓名
# 3、修改手机
# 4、查询用户
# 5、根据姓名查寻手机号
# 6、退出程序#

# 永远记住哦 默认input是输入字符型数据。

def main():
    import time
    # 创建空字典
    cx_dict = dict()
    xz = 0
    while xz is not None:
        print('=========遇讯录管理系统========')
        print('\t\t1、增加姓名和手机号')
        print('\t\t2、删除信息')
        print('\t\t3、根据姓名修改手机号')
        print('\t\t4、查询所有用户')
        print('\t\t5、根据姓名查寻手机号')
        print('\t\t6、退出程序')
        xz = input('请选择：')

        while xz == '1':
            name = input('请输入增加的姓名：')
            num = input('请输入增加的手机号：')
            cx_dict[name] = num
            print('添加成功！')
            time.sleep(1)
            break

        while xz == '2':

            name = input('请输入要删除的姓名：')
            if name not in cx_dict:
                print('该用户不存在，请重新输入！')
                time.sleep(1)
                continue

            judge = input('是否确定删除( A：是 B：否)? 请选择：')
            if judge == 'A' or judge == 'a':
                del cx_dict[name]
                print('删除完成！')
                time.sleep(1)
                break
            elif judge == 'B' or judge == 'b':
                print('信息未删除!2秒后返回主页面...')
                time.sleep(2)
                break
            else:
                print('输入错误！')
                time.sleep(1)
                continue

        while xz == '3':
            name = input('请输入要修改信息的用户姓名：')
            if name in cx_dict:
                print('你要修改的原信息为：', cx_dict[name])
                new_value = input('请输入你要改为的号码：')
                judge = input('是否确定修改( A：是 B：否)? 请选择：')
                if judge == 'A' or judge == 'a':
                    cx_dict[name] = new_value
                    print('修改完成！')
                    time.sleep(1)
                    break
                elif judge == 'B' or judge == 'b':
                    print('信息未修改!2秒后返回主页面...')
                    time.sleep(2)
                    break
                else:
                    print('输入错误！')
                    time.sleep(1)
                    break
            else:
                print('系统中没有该用户！')
                time.sleep(1)
                break

        while xz == '4':
            if cx_dict == {}:
                print("当前未录入任何用户的信息！")
                time.sleep(1)
                break
            else:
                print('系统中所有用户信息如下：', '\n', cx_dict)
                exit_sr = input('按任意键返回主菜单！')
                if exit_sr is not None:
                    main()

        while xz == '5':
            name = input('请输入要查询的姓名：')
            if name in cx_dict:
                print('该用户手机号为：', cx_dict[name])
                time.sleep(1)
                break
            else:
                print('系统中没有该用户！')
                time.sleep(1)
                break

        if xz == '6':
            xz = None
            print('3秒后结束程序...')
            time.sleep(3)
            break

        while xz not in ['1', '2', '3', '4', '5', '6']:
            print('输入错误，请重新选择！')
            time.sleep(1)
            break


def myDivmod():
    """ divmod函数可以获取除法的商和余数,存为元组类型 """
    print(divmod(99, 10))  # (9,9)
    print(divmod(91, 10))  # (9,1)
    print(divmod(90, 10))  # (9,0)


# main()

myDivmod()
