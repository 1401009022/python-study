#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Autor:tangzicheng

from http.server import BaseHTTPRequestHandler,HTTPServer
import sys,os

class ServerException(Exception):
    '''异常类'''
    pass

class case_no_file(object):
    '''该路径不存在'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))

class case_existing_file(object):
    '''该路径是文件'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handler_file(handler.full_path)

class case_always_fail(object):
    '''所有情况都不符合时的默认处理类'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))

class case_directory_index_file(object):

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    # 判断目标路径是否是目录&&目录下是否有index.html
    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
            os.path.isfile(self.index_path(handler))

    # 响应index.html的内容
    def act(self, handler):
        handler.handler_file(self.index_path(handler))





class RequestHandler(BaseHTTPRequestHandler):
    '''处理请求并返回页面'''

    #页面模板
    Page = '''\
    <html>
    <body>
    <table>
    <tr>  <td>Header</td>         <td>Value</td>          </tr>
    <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
    <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    </table>
    </body>
    </html>'''

    # 所有可能的情况
    Cases = [
        case_no_file(),
        case_existing_file(),
        case_directory_index_file(),
        case_always_fail()
    ]



    # 处理get请求
    def do_GET(self):

        try:

            # 文件完整路径
            self.full_path = os.getcwd() + self.path

            # 遍历所有可能的情况
            for case in self.Cases:
                # 如果满足该类情况
                if case.test(self):
                    # 调用相应的act函数
                    case.act(self)
                    break

        except Exception as msg:
            self.handle_error(msg)

        #
        #     # 如果路径不存在
        #     if not os.path.exists(full_path):
        #         # 抛出异常，文件未找到
        #         raise ServerException("'{0}' not found".format(self.path))
        #
        #     # 如果该路径是一个文件
        #     elif os.path.isfile(full_path):
        #         # 调用handle_file 处理该文件
        #         self.handle_file(full_path)
        #
        #     # 如果该路径不是一个文件
        #     else:
        #         # 抛出异常，该路径为不知名对象
        #         raise ServerException("Unknown object '{0}'".format(self.path))
        # # 处理异常
        # except Exception as msg:
        #     self.handle_error(msg)

    # def create_page(self):
    #     values = {
    #         'date_time' : self.date_time_string(),
    #         'client_host' : self.client_address[0],
    #         'client_port' : self.client_address[1],
    #         'command' : self.command,
    #         'path' : self.path
    #     }
    #     page = self.Page.format(**values)
    #     return page

    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.send_header("content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode('utf-8'), 404)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
















