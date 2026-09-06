"""项目二：命令行简易记账本
完成时间：2026年9月6日
核心知识点：JSON文件存储、列表与字典嵌套、函数（模块化）、时间处理。

功能设想：

程序启动后显示菜单：1. 添加账目 2. 查看账单 3. 计算本月总支出/收入 4. 删除一条记录 5. 退出。
每笔记录包含：金额、类型（收入/支出）、分类（餐饮/购物/工资等）、日期（自动取当天日期）。
数据持久化：所有记录保存到一个 data.json 文件里，下次启动自动加载。
查看账单时，可以按 月份 筛选，并显示收支汇总。
进阶挑战：

给收入/支出记录增加颜色（用\033[92m红色，\033[91m绿色），让控制台输出更直观。
收获：掌握JSON模块（json.dump和json.load），学会写菜单循环、函数拆分功能，这是未来一切复杂程序的雏形。"""

import json
from datetime import datetime

# 自动获取当前时间
now = datetime.now()
date_text = now.strftime("%Y-%m-%d %H")

info = []
income_cate = ["工资","兼职","奖金","理财","红包","退款","其他"] # 收入分类
expend_cate = ["餐饮","房租","交通","购物","娱乐","医疗","其他"] # 支出分类
records = info

# 将记录保存到一个data.json中
# 加载：程序启动运行
def load_data():
    global info
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            info = json.load(f)
    except FileNotFoundError:
        info = []

 # 保存函数：把内存info写入json
def save_data():
    global info
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)

load_data()

# 开启菜单
def info_print():
    print("=" * 30)
    print("         简易账本记录          ")
    print("1.添加账目")
    print("2.查看账单")
    print("3.计算某月总支出/收入")
    print("4.删除一条记录")
    print("5.退出")
    print("=" * 30)

# 添加账目
def add_bill():
    # 接受用户输入
    new_type = input("请输入收入还是支出：").strip()
    if new_type not in ["收入","支出"]:
        print("输入错误！请输入'收入'或'支出'")
        return
    new_category = input("请输入类型：")

    try:
        new_money = float(input("请输入金额："))
        if new_money < 0:
            print("金额必须大于0！")
            return
    except ValueError:
        print("金额必须是数字！")
        return

    # 账单字典
    bill_dict = {
        "type" : new_type,
        "category" : new_category,
        "money" : new_money,
        "date": date_text
    }

    info.append(bill_dict)
    save_data()
    print(f"账单【{new_type}:{new_category}，金额：{new_money}元，日期：{now}】添加成功")

# 查询账单

def view_bill():
    # 没有记录
    if not info:
        print("没有查询到账单记录")
        return

    # 有记录则遍历
    print("=" * 50)
    print(f"{'类型':<8}{'来源':<12}{'金额':<12}{'日期':<20}")
    print("=" * 50)

    # 用颜色区分收入和支出
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"

    for bill in info:
        bill_type = bill['type']
        category = bill['category']
        money = bill['money']
        date = bill['date']

        if bill_type == "收入":
            color = GREEN
        else:
            color = RED

        # 带颜色格式化输出表格一行
        print (f"{color}{bill['type']:<8}{bill['category']:<12}{bill['money']:<12}{bill['date']}{RESET}")

    print("=" * 50)

# 计算本月总支出/收入

def ccl_bill():
    try:
        record_year = int(input("请输入年份："))
        record_month = int(input("请输入月份："))
    except ValueError:
        print("请输入有效的数字！")
        return

    total_income = 0.0
    total_expend = 0.0

    for bill in info:
        # 先把日期字符串解析成datetime对象
        date_str = bill['date']
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H")

        if date_obj.year == record_year and date_obj.month == record_month:
            if bill["type"] == "收入":
                total_income += bill['money']
            elif bill["type"] == "支出":
                total_expend += bill['money']

    print(f"\n======== {record_year}年{record_month}月 统计 ========")
    print(f"{record_year}年{record_month}月总收入：{total_income:.2f}元")
    print(f"{record_year}年{record_month}月总支出：{total_expend:.2f}元")
    print(f"{record_year}年{record_month}月结余：{total_income - total_expend:.2f}元")
    print("====================================================\n")

# 删除一条记录

def del_bill():
    if not info:
        print("账单为空，没有可以删除的记录！")
        return

    # 先打印带序号的账单出来
    print("=======================帐单列表=======================")
    for idx, bill in enumerate(info):
        print(f"{idx + 1}. {bill['type']} | {bill['category']} | {bill['money']}元 | {bill['date']}")

    del_record = input("请输入要删除的记录序号：")
    if not del_record:
        print("输入错误，请输入数字")
        return

    del_idx = int(del_record) - 1  # 用户输入从1开始，列表下标从0开始

    # 判断下标是否合法
    if 0 <= del_idx < len(info):
        removed = info.pop(del_idx)
        save_data()  # 删除后立刻保存到json！
        print(f"删除成功，已删除序号为{del_record}账单的记录")
    else:
        print("没有找到该序号的记录，删除失败")

while True:
    info_print()
    num = input("请输入你要操作的序号（1-5）：")
    if num == "1":
        print("您选择了添加账目")
        print("添加收入:工资,兼职,奖金,理财,红包,退款,其它")
        print("添加支出:餐饮,房租，交通,购物,娱乐,医疗,其它")
        add_bill()
    elif num == "2":
        print("您选择了查看账单")
        view_bill()
    elif num == "3":
        print("您选择了计算总支出/收入")
        ccl_bill()
    elif num == "4":
        print("您选择了删除一条记录")
        del_bill()
    elif num == "5":
        quit_config = input("您是否选择退出（y/n）:")
        if quit_config == "y":
            save_data()
            print("退出成功！账单已保存！")
            break
    else:
        print("输入有误！请重新输入（1-5）:")
