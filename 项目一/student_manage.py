# 函数版学员管理系统
#完成时间：2026年9月4日
"""要求：
1.添加学员信息（学号，姓名，手机号，姓名不重复）
2.删除学员信息（按姓名删除）
3.修改学员信息（按姓名修改学号手机号）
4.查询学员信息（按姓名查询）
5.显示所有学员信息
6.退出系统（二次确认）"""

info = [] # 全局变量：存储所有学员的信息（列表+字典）

# 添加学员
def add_stu():
    # 接收用户输入
    new_name = input("请输入姓名：")
    new_id = input("请输入学号：")
    new_tel = input("请输入手机号：")
    # 判断学员是否存在
    for student in info:
        if new_name == student['name']:
            print(f"学员【{new_name}】已存在，无法添加")
            return # 结束函数运行，不执行后续代码

    # 保存到学员字典
    student_dict = {
        "name": new_name,
        "id": new_id,
        "tel": new_tel
    }
    #添加到列表
    info.append(student_dict)
    print(f"学员{student_dict}添加成功")

# 删除学员
def del_stu():
    del_name = input("请输入要删除的学员：")

    # 判断学员是否存在
    for student in info:
        if del_name == student['name']:
            info.remove(student) # 列表删除该字典
            print(f"删除成功!已删除姓名【{del_name}】的学员信息")
            print(f"当前剩余学员：【{info}】")
            return

    # 遍历完没找到学员
    print(f"错误，找不到姓名【{del_name}的学员信息】")

# 修改学员信息
def modify_stu():
    modify_name = input(f"请输入要修改的姓名：")

    # 判断学员是否存在
    for student in info:
        if modify_name == student['name']:
            student["id"] = input(f"请输入修改后的学号：")
            student["tel"] = input(f"请输入修改后的手机号：")
            print(f"修改成功！修改后的信息为【{student}】")
            return
    # 遍历一遍没有找到
    print(f"错误！找不到姓名【{modify_name}的学员信息")

#查询学员信息
def search_info():
    search_name = input(f"请输入要查询的姓名:")

    for student in info:
        if search_name == student['name']:
            print(f"这是姓名【{search_name}】的学员信息：【{student}】")
            return

    print(f"错误！找不到姓名{search_name}的学员信息")

# 显示所有学员信息
def print_all():
    #判断是否有学员数据
    if not info:
        print("当前暂无学员信息")
        return

    # 有数据，格式化表头
    print("=" * 33)
    print("姓名\t\t学号\t\t手机号")
    print("-" * 33)

    # 遍历信息，打印每个学员信息
    for student in info:
        print(f"{student['name']}\t\t{student['id']}\t\t{student['tel']}")
    print("=" * 33)

def info_print():
    print("=" * 33)
    print("           学员管理系统           ")
    print("1.添加学员信息")
    print("2.删除学员信息")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示所有学员信息")
    print("6.退出系统")
    print("=" * 33)

while True:
    # 显示功能界面
    info_print()

    user_sum = input("请输入你要操作的序号（1-6）：")
    if user_sum == "1":
        print("您选择了【添加学员】")
        add_stu()
    elif user_sum == "2":
        print("您选择了【删除学员】")
        del_stu()
    elif user_sum == "3":
        print("您选择了【修改学员】")
        modify_stu()
    elif user_sum == "4":
        print("您选择了【查询学员】")
        search_info()
    elif user_sum == "5":
        print("您选择了【显示所有学员】")
        print_all()
    elif user_sum == "6":
        quit_config = input("您确认要退出吗：y/n")
        if quit_config == "y":
            print("退出成功！")
            break
    else:
        print("输入有误，请重新输入！")
