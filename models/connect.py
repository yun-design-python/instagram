#连接数据库

from sqlalchemy import create_engine  #create_engine创造引擎
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#接下来设定连接数据库（以MySQL为例）所需要的信息，
# 包括用户名、密码、端口号、IP以及要使用的数据库名字等信息，例如：
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'instagram'#数据库名称
USERNAME = 'root'
PASSWORD = 'qwe123'
#然后设置一个字符串的格式：
db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE
)
#创建一个引擎：
engine = create_engine(db_url)

#将引擎作为参数导入declarative_base()方法，返回一个类

Base = declarative_base(engine)


# 同时需要创建一个会话窗，即映射：
#增删改查时需要

Session = sessionmaker(engine)
session = Session()

#验证是否成功可以在尾端进行如下操作：
# if __name__=='__main__':
#     print(dir(Base))
#     print(dir(session))