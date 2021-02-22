#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
服务端
"""

import socket
import select
import time

def uploadfile():
    """
    上传文件
    :return:
    """
    upload_path = "./upload/"
    print("进入函数成功")
    # 接收要上传文件的大小
    file_size = int(str(conn.recv(10240),encoding="utf-8"))
    print("用户要上传的文件大小：", file_size)

    #已接受客户端发来的文件大小，返回确认信息，防止粘包
    conn.sendall(bytes("AYC",encoding="utf-8"))

    #已接收文件大小
    has_size = 0

    #接收文件并存入upload文件夹
    filename = time.time()
    f = open(upload_path+str(filename)+".jpg","wb")
    while True:

        #文件上传完成跳出
        if has_size == file_size:
            break
        data = conn.recv(1024)
        f.write(data)

        has_size += len(data)
    #关闭文件
    print("文件上传完毕")
    f.close()

#创建socket
s = socket.socket()
s.bind(('127.0.0.1',8888))
s.listen(5)

#初始化参数
inputs = [s, ] #存放输入的conn及wk对象
outputs = [] #存放输出内容的conn
message_dict = {} #存放客户端发送到信息和conn
inte_time = 1
print("[127.0.0.1：8888]服务已经开启监听")


while True:
    # 利用select构建IO多路复用
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, inte_time)

    print("当前在线人数[%s]: %s" % (len(inputs) -1, r_list))

    #读取客户端，并加入r_list监听
    for s_or_conn in r_list:

        #如果是s服务器对象，则代表有新用户连接
         if s_or_conn == s:

           #将新用户的连接对象加入select监听
            conn, addr = s_or_conn.accept()
            inputs.append(conn)
            message_dict[conn] = []
         # 表示已连接用户已发送消息
         else:
             #防止客户端传空字符串报错使程序崩溃
            try:
                #获取客户端发送的数据
                acc_data_bytes = s_or_conn.recv(1024)
            except Exception as e:
                #显示报错信息，并将出错的客户端连接从inputs中移除
                print(e)
                inputs.remove(s_or_conn)
            else:
                #正常接收用户发送的消息，并存入消息字典
                acc_data_str = str(acc_data_bytes, encoding="utf-8")
                message_dict[s_or_conn].append(acc_data_str)

                #将发过消息的用户放入output，便于回复
                outputs.append(s_or_conn)
    #自动回复发送消息的客户端
    for conn in w_list:
        #获取到客户端发送的数据，放入内存并删除
        recv_data = message_dict[conn][0]
        del message_dict[conn][0]
        conn.sendall(bytes("您说: "+recv_data,encoding="utf-8"))
        outputs.remove(conn)

    #自动移除多socket中出错的对象
    for s in e_list:
        inputs.remove(s)








    #
    # conn, address = s.accept()
    # conn.sendall(bytes("欢迎进入机器人聊天系统",encoding="utf-8"))
    # print(address,"已连接")
    #
    # while True:
    #     ret_bytes = conn.recv(1024)
    #     ret_str = str(ret_bytes,encoding="utf-8")
    #     if ret_str =="q":
    #         break
    #     elif ret_str =="cd":
    #         conn.sendall(bytes(
    #             """
    #             ======菜单======
    #             1.查询
    #             2.激活
    #             3.退订
    #             4.预览
    #             5.上传文件
    #             ===回复序号选择===
    #             """,encoding="utf-8"
    #         )
    #         )
    #     elif ret_str == "5":
    #         uploadfile()
    #     conn.send(bytes("[用户]" + ret_str,encoding="utf-8"))
    #
    #






















