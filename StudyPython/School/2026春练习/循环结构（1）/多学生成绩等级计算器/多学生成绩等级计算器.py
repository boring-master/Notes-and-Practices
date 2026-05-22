students = {}  # 创建一个空字典 保存所有学生成绩和等级
while True:
    # 输入学生姓名,给name赋值,若name为exit,则结束循环
    name = input()
    if name == 'exit':
        break
    try:
        # 格式化输入学生的平时成绩1:stu_score1，平时成绩2:stu_score2
        stu_score1, stu_score2 = eval(input())
        # 格式化输入学生的期中成绩stu_mscore和期末成绩stu_fscore
        stu_mscore, stu_fscore = eval(input())
        # 输入验证
        if any(score < 0 or score > 100 for score in [stu_score1, stu_score2, stu_mscore, stu_fscore]):
            raise ValueError("成绩必须在0-100分之间")  # 抛出ValueError异常信息，程序在此中止
    except ValueError as e:
        print(f"输入错误: {e},请重新输入")
        continue
    # 计算总评,若期末成绩<30分,则总评成绩为期末成绩
    total = stu_score1 * 0.2 + stu_score2 * 0.3 + stu_mscore * 0.1 + stu_fscore * 0.4
    # 根据总评成绩判断学生等级
    if 90 < total < 100:
        grade = '优秀'
    elif 80 < total < 90:
        grade = '良好'
    elif 70 < total < 80:
        grade = '中等'
    elif 60 < total < 70:
        grade = '及格'
    else:
        grade = '不及格'
    if stu_fscore < 30:
        total = stu_fscore
        grade = '不及格'

    # 将学生总评和等级加入字典中，建立学生成绩等级字典，成绩保留小数点后1位输出
    students[name] = {"总评": round(total, 1), "等级": grade}
print("最终成绩汇总：")
for name, result in students.items():
    print(f"{name}:{result['总评']}分,{result['等级']}")