from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.config import config

engine = create_engine(getattr(config["default"], "SQLALCHEMY_DATABASE_URI"), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    # import yourapplication.models
    print("导入数据库模型......success")
    import app_api.entity.examination as exam
    print("清空数据库......success")
    Base.metadata.drop_all(bind=engine)
    print("创建数据库......success")
    Base.metadata.create_all(bind=engine)
    print("创建数据库完成......success")
