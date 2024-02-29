# CS2获取BUFF饰品信息

## 需求分析

- 获取各类武器信息
- 信息比较后发送邮箱

## 程序设计

1. cookie访问跳过登录
2. 初始化基本信息
3. 遍历获取信息
   - get请求url
   - json转字典
5. 比较信息发送邮箱

### cookie访问模拟登录

爬取BUFF数据遇到的第一个问题是登陆,可使用登录后的cookie进行访问。

`访问`https://buff.163.com/`登陆BUFF后按`F12`打开开发者工具，选中`网络`+`标头`，刷新页面，找到`Cookie`和`User-Agent`

```python
#请求头参数
headers = {
            'cookie': 'Device-Id=iG9P2xyditYu0kPBM6mX; remember_me=U1103958728|HDsN8zFOkJECNcIDi1R6cGVn43ruvcaO; session=1-xRg3_oUho46brZwAOVjI5ERMCODw5EoilROla19pZ3cV2030275984; Locale-Supported=zh-Hans; game=csgo; csrf_token=IjQ4MTA2YjFlYWU0MzBiYWUxYWVkNTJlNTRhMmUxMjZkMGNkYTY0MjEi.GMBx_A.T31wz74TyCJh1rsU8C1USPjiWuY',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
```

### python requests库

- Requests是Python一个很实用的HTTP客户端，完全满足如今网络爬虫的需求
- urllib库和requests库功能类似，但requests库功能更多更实用

#### 常用方法

| 方法                  | 描述                                       |
| --------------------- | ------------------------------------------ |
| requests.request(url) | 构造一个请求，支持以下各种方法             |
| requests.get()        | 发送一个Get请求，url请求                   |
| requests.post()       | 发送一个Post请求，提交表单，如账户密码提交 |
| requests.head()       | 获取HTML的头部信息                         |
| requests.put()        | 发送Put请求                                |
| requests.patch()      | 提交局部修改的请求                         |
| requests.delete()     | 提交删除请求                               |

#### response对象常用属性

| 属性或方法           | 描述                                           |
| -------------------- | ---------------------------------------------- |
| response.status_code | 响应状态码                                     |
| response.content     | 把response对象转换为二进制数据                 |
| response.text        | 把response对象转换为字符串数据                 |
| response.encoding    | 定义response对象的编码                         |
| response.cookie      | 获取请求后的cookie                             |
| response.url         | 获取请求网址                                   |
| response.json()      | 内置的JSON解码器                               |
| Response.headers     | 以字典对象存储服务器响应头，字典键不区分大小写 |

#### get()请求

```python
requests.get(url=url, headers=headers)
```

https类型网站但是没有经过证书认证机构认证的网站，程序中抛出SSLError异常则考虑使用此参数

```python
requests.get(url=url,headers=headers,verify=False)
```

#### post()请求

```python
url='https://www.xslou.com/login.php'
data={'username':'18600605736', 'password':'57365736', 'action':'login'}
resp = requests.post(url,data)
```

### 后端接口API

一般前端通过url将后端信息以json格式传输到前端

#### python解析json数据

JSON格式是**网站和API使用的通用标准格式，**现在主流的一些数据库（如[PostgreSQL](https://so.csdn.net/so/search?q=PostgreSQL&spm=1001.2101.3001.7020)）都支持JSON格式

Python原生支持JSON数据。Python **json**模块是标准库的一部分。该**json**模块可以将JSON数据从JSON格式转换到等效的Python对象

##### json文件转为python对象

| 方法    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| load()  | 读取文件中的JSON数据。要从文件路径中获取文件对象，可以使用Python的函数**open()** |
| loads() | 读取JSON字符串                                               |

##### python对象转为json对象

| 方法    | 描述                                             |
| ------- | ------------------------------------------------ |
| dumps() | 将Python对象转换为JSON对象也称为序列化或JSON编码 |

##### python对象写入json文件

| 方法   | 描述             |
| ------ | ---------------- |
| dump() | 用于编写JSON文件 |

### 邮箱

#### context换行

`如果邮件格式是文本格式,使用“\r\n”`

`如果件是HTML格式，使用"<br>"`

## 自动化运行脚本

### Windows Task Scheduler

此电脑右键管理---任务计划程序---创建基本任务（若每几小时以下，则创建任务）

- Program/script：填写 Python编译器的名称 python.exe

- Add arguments：打算执行的Python脚本的完整路径，D:\PyCodes\test.py
- Start in： 填写Python编译器的目录，上图中，Python编译器的完整路径是“C:\Python37\\python.exe”