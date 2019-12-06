import os

def replace_file_name_str(origin_str, target_str):
    # 获取目录下的所有文件名
    file_name_list = os.listdir(filePath)

    # 便利替换文件名中的字符串
    n = 0
    for fileName in file_name_list:
        if fileName.find(origin_str) >= 0:
            new_file_name = fileName.replace(origin_str, target_str)
            os.rename(filePath + fileName, filePath + new_file_name)
        n += 1
    return


# 输入的文件目录
filePath = input('请输入文件所在的目录名：\n')

# 确认目录名
confirm = ''
if filePath != '':
    confirm = input('你输入的目录名称为：' + filePath + '\n'
                                              '请确认：y:确认，n:放弃\n')

has_continue = confirm == 'y'

# 输入的操作方式
operatorType = input('请按说明输入操作类型\n'
                     '1.删除所有文件名中的指定内容\n'
                     '2.替换所有文件名中的指定内容\n')

# 判断操作方式
# 1.删除所有文件名中的指定字符串
if has_continue and operatorType == '1':
    # 需删除的字符串
    targetStr = input('请输入需删除的内容：\n')

    # 修改文件名
    replace_file_name_str(targetStr, '')

# 2.替换所有文件名中的指定字符串
if has_continue and operatorType == '2':
    # 原字符串
    originStr = input('请输入需要替换的内容：\n')

    # 目标字符串
    targetStr = input('请输入替换内容：\n')

    # 修改文件名
    replace_file_name_str(originStr, targetStr)
