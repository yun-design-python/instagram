from sqlalchemy import Column,Integer,String,DateTime,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 把当前项目路径加入到path中
from models.connect import Base,session

class BaseModels:#不需要继承Base 继承了会创建表
    is_delete = Column(Boolean, default=False)  #逻辑删除，改变Boolean值。不是真正的删除
    update_time = Column(DateTime, default=datetime.now) #修改时间
    create_time = Column(DateTime, default=datetime.now) #创建时间

#创建用户名模型
class User(Base,BaseModels):#提交到数据库   通过base类
    __tablename__ = 'users'  #表格名字
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(200))  #这里应该是int类型
    activation = Column(Boolean, default=False) #激活
    email = Column(String(100))
    phone = Column(String(30))

    @classmethod
    def add_user(cls, username, password, **kwargs):
        user = User(username=username, password=password, **kwargs)
        session.add(user)
        session.commit()

    # classmethod 修饰符对应的函数不需要实例化，不需要self参数，但第一个参数需要是表示自身类的cls参数，
    # 可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def check_username(cls, username):
        return session.query(cls).filter_by(username=username).first()

    def __repr__(self):
        return "<User:username=%s,password=%s>" % (self.username, self.password)


#创建图片模型
class Post(Base,BaseModels):#提交到数据库   通过base类
    __tablename__ = 'posts'  #表格名字
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(200)) #图片地址
    user_id = Column(Integer, ForeignKey("users.id"))
    # 通过图片实例查找到用户
    #图片实例.user===>>拿到对应的user实例
    # 通过用户实例查找到图片
    #用户实例.posts===>>拿到对应的图片实例
    #relationship正反向查询
    user = relationship("User", backref="posts", uselist=False, cascade="all")
    def __repr__(self):
        return "Post:user_id=%s" % self.user_id









