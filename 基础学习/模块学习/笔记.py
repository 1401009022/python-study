# 什么是模块？
#     一个.py文件就可以成为一个模块
# 模块的好处
#     1.避免函数名、变量名冲突
#     a.py
#         def sayhi()
#     b.py
#         def sayhi()
#
#
# 模块分类：
#     1.标准模块（内置模块）| 标准库   约300个   python自带
#       External Libraries/<Python 3.8>/py38 libirary root
#     2.第三方模块   pip install安装            30W个左右了..
#     3.自定义模块（自己写的）
#
#     一个文件夹是一个包

# 导入方式
#     1.import xxx,xxx
#     可以加逗号，一次导入多个
#     2.from xxx import xxx,xxx,xxx
#       只想用一些单独的功能
#       不用加模块名了，
#       * 引入所有（不建议使用. 万一有重名之类的、 万一自己不小心命名了一个相同的名的，会覆盖
#     3.from module.xx.xx import xxx
#
#     4.from xxx import xxx as xxx
#       进行一个重命名

#   自定义模块 （不要用中文
#       导入的时候注意路径

#       python模块查找路径
#           根据python模块的路径列表
#           可以将自己写的放入标准库路径下（不建议  可以放在第三方库下
import sys
print(sys.path) # 查看路径

# 空的话代表当前目录
# ['D:\\Tools\\universal\\GitStore\\python-study\\基础学习\\模块学习',
# 'D:\\Tools\\universal\\GitStore\\python-study',
# 'D:\\CTFstu\\tools\\py38\\python38.zip',
# 'D:\\CTFstu\\tools\\py38\\DLLs',
# 'D:\\CTFstu\\tools\\py38\\lib',            标准库？？？
# 'D:\\CTFstu\\tools\\py38',
# 'D:\\CTFstu\\tools\\py38\\lib\\site-packages',  第三方
# 'D:\\CTFstu\\tools\\py38\\lib\\site-packages\\shodan-1.24.0-py3.8.egg',
# 'D:\\CTFstu\\tools\\py38\\lib\\site-packages\\xlsxwriter-1.3.7-py3.8.egg',
# 'D:\\CTFstu\\tools\\py38\\lib\\site-packages\\colorama-0.4.4-py3.8.egg',
# 'D:\\CTFstu\\tools\\py38\\lib\\site-packages\\click_plugins-1.1.1-py3.8.egg',
# 'D:\\CTFstu\\tools\\py38\\lib\\site-packages\\click-8.0.0a1-py3.8.egg']


# 第三方
# pypi.org   可以自己贡献代码！！！！！
# 下载后要进行安装
# 1.编译源码，安装源码 (现在用的比较少了
#   python setup.py build    比如可能会有依赖系统的环境等
#   python setup.py install
# 2.直接安装 pip install 模块名
#   一般不从国外下载 太慢了， 在国内有镜像网站，
#   豆瓣源 -i 指定源  --trust-host 通过网站https验证

#   卸载
#   pip freeze列出版本  pip list








