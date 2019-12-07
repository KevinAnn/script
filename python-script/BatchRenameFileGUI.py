# -*- coding: UTF-8 -*-
import os
from tkinter import *
from tkinter import messagebox


# ==================== 函数 ====================

def alert(title, message):
    """ 弹框提示 """
    messagebox.showinfo(title=title, message=message)


def center_window(cont, width, height):
    """ 窗口居中 """
    screenwidth = cont.winfo_screenwidth()
    screenheight = cont.winfo_screenheight()
    size = "%sx%s+%s+%s" % (
        width, height, (screenwidth - width) // 2,
        (screenheight - height) // 2)
    return size


def add_sep(path):
    """ 给路径后加上‘/’ """
    if path and not path.endswith('/'):
        path += '/'
    return path


def get_filename_list(path):
    """ 获取路径下的文件名 """
    try:
        # 给路径末尾拼上'/'
        path = add_sep(path)
        # 获取目录下的所有文件名
        filenames = os.listdir(path)
    except BaseException as e:
        alert('提示', e)
        return list()
    else:
        return filenames


def put_filename_list(filenames):
    """ 给列表中填充文件名 """
    # 清除原有内容
    listbox.delete(0, END)
    # 遍历赋值
    i = 0
    for filename in filenames:
        listbox.insert(i, filename)
        i += 1
    # 原内容输入框中填充列表中第一个文件名
    if filenames:
        originstr.set(filenames[0])


def search_filepath():
    """ 获取目录下的所有文件名 """
    # 输入了路径进行搜索，没输入则弹提示
    if filepath.get():
        # 添加所有文列表
        put_filename_list(get_filename_list(filepath.get()))

    else:
        alert('提示', '路径为空，请输入目录路径')


def change_file_name():
    """ 批量修改文件名 """
    # 目录路径不能为空
    if filepath.get():

        # 原内容不能为空
        if originstr.get():
            origin_str = originstr.get()
            target_str = ''
            if targetstr.get():
                target_str = targetstr.get()

            # 给路径末尾拼上'/'
            path = add_sep(filepath.get())

            # 便利目录下的文件名，判断并改名
            for filename in os.listdir(filepath.get()):
                if filename.find(origin_str) >= 0:
                    new_filename = filename.replace(origin_str, target_str)
                    os.rename(path + filename, path + new_filename)

            # 添加文件名列表
            put_filename_list(get_filename_list(path))

        else:
            alert('提示', '请输入原内容')

    else:
        alert('提示', '路径为空，请输入目录路径')


# ==================== 界面 ====================
root = Tk()

# 标题
root.title('批量修改文件名')

# 窗口参数
root.geometry(center_window(root, 600, 500))

# 说明
Label(root, text='请先输入目录路径，再输入要修改的内容').pack(pady=10)

# 主框架
frm = Frame(root)

# 顶部框架
frm_top = Frame(frm)
# 目录路径输入框
Label(frm_top, text='文件目录路径：').pack(side=LEFT)
filepath = StringVar()
Entry(frm_top, textvariable=filepath, font=('Courier New', 12), width=30).pack(side=LEFT, ipady=1)

# 确认按钮
Button(frm_top, text='确认', width=10, command=search_filepath).pack(side=LEFT, padx=10)
frm_top.pack(pady=15)

# 中部框架
frm_mid = Frame(frm)

# 标题，当前目录文件列表：
Label(frm_mid, text='当前目录文件列表：').grid(row=0, column=0, sticky=W, padx=10)

# 列表内滚动条
# 横向
scroll_hor = Scrollbar(frm_mid, orient=HORIZONTAL)
scroll_hor.grid(row=8, column=0, sticky=EW)
# 纵向
scroll_ver = Scrollbar(frm_mid, orient=VERTICAL)
scroll_ver.grid(row=1, rowspan=6, column=1, sticky=NS)

# 目录内文件列表
filename_list = StringVar()
listbox = Listbox(frm_mid, selectmode=BROWSE, listvariable=filename_list, width=30, height=15)
listbox.grid(row=1, rowspan=6, column=0, ipadx=5, ipady=2, sticky=NSEW)

# 绑定列表与滚动条
listbox.config(xscrollcommand=scroll_hor.set)
listbox.config(yscrollcommand=scroll_ver.set)
scroll_hor.config(command=listbox.xview)
scroll_ver.config(command=listbox.yview)

# 标题，文件名批量修改
Label(frm_mid, text='文件名批量修改').grid(row=0, column=2, columnspan=2)

# 原内容
Label(frm_mid, text='   原内容：').grid(row=1, column=2, padx=10)
originstr = StringVar()
Entry(frm_mid, textvariable=originstr, width=25).grid(row=1, column=3)

# 替换内容
Label(frm_mid, text='替换内容：').grid(row=2, column=2, padx=10)
targetstr = StringVar()
Entry(frm_mid, textvariable=targetstr, width=25).grid(row=2, column=3)

# 修改
Button(frm_mid, text='修改', width=10, command=change_file_name).grid(row=3, column=3)
frm_mid.pack(pady=15)

frm.pack()

root.mainloop()