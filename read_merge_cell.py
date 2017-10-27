# coding=utf-8
"""
演示合并单元格的读取
"""
import xlrd
from common import *

book = xlrd.open_workbook(u'./data/读取合并单元格.xlsx')
sheet = book.sheet_by_index(0)
nrows = sheet.nrows

# 合并后的单元格,只有合并区域里的左上角的cell里有值
for i in range(nrows):
    print i, get_cn_unicode(sheet.row_values(i))

# 读取一行中的指定区域
print_cn_unicode(sheet.row_values(1, start_colx=1, end_colx=3))
