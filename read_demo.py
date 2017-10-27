#coding=utf-8
"""
演示如何读取excel文件,注意数字部分,读取出来以后都是float类型
如果期望的是int类型,那么需要你自己去做转换
"""
import xlrd
# 打开文件
book = xlrd.open_workbook(u'./data/读取示例.xlsx')
"""
选择要读取的sheet,可以使用位置,利用sheet_by_index方法
或者根据sheet的名字
"""
sheet = book.sheet_by_index(0)
# sheet = book.sheet_by_name('data')
# 获取基本信息,有多少行,有多少列
nrows = sheet.nrows
ncols = sheet.ncols

# 按行读取,使用row_values 方法
for i in range(nrows):
    print sheet.row_values(i)

# 按列读取,使用col_values 方法
for j in range(ncols):
    print sheet.col_values(j)

print '-'*40
# 将员工信息读取到字典中
person = {}

for i in range(1, nrows):
    row = sheet.row_values(i)
    info = {'age': int(row[1]), 'salary': float(row[2])}
    person[row[0]] = info

# 遍历字典
for k, v in person.items():
    print k, v
