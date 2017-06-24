from app_api.database import db_session
from sqlalchemy.inspection import inspect
from sqlalchemy.sql.schema import Table

def get_row_by_id(model_name, pk_id):
    """
    通过id获取信息
    :type pk_id: object
    :type model_name: object
    :return None/object
    """
    row = db_session.query(model_name).get(pk_id)
    return row


def get_rows_by_ids(model_name, pk_ids):
    """
    通过一组 ids 获取信息列表
    :param model_name:
    :param pk_ids:
    :return: list
    """
    model_pk = inspect(model_name).primary_key[0]
    rows = db_session.query(model_name).filter(model_pk.in_(pk_ids)).all()
    return rows


def get_limit_rows_by_last_id(model_name, last_pk_id, limit_num, *args, **kwargs):
    """
    通过最后一个主键 id 获取最新信息列表
    适用场景：
    1、动态加载
    2、快速定位
    :param model_name:
    :param last_pk_id:
    :param limit_num:
    :param args:
    :param kwargs:
    :return: list
    """
    model_pk = inspect(model_name).primary_key[0]
    rows = db_session.query(model_name).filter(model_pk > last_pk_id, *args).filter_by(**kwargs).limit(limit_num).all()
    return rows


def get_row(model_name, *args, **kwargs):
    """
    获取信息
    Usage:
        # 方式一
        get_row(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_row(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/object
    """
    row = db_session.query(model_name).filter(*args).filter_by(**kwargs).first()
    return row


def get_lists(model_name, *args, **kwargs):
    """
    获取列表信息
    Usage:
        # 方式一
        get_lists(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        get_lists(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: None/list
    """
    lists = db_session.query(model_name).filter(*args).filter_by(**kwargs).all()
    return lists


def count(model_name, *args, **kwargs):
    """
    计数
    Usage:
        # 方式一
        count(User, User.id > 1)
        # 方式二
        test_condition = {
            'name': "Larry"
        }
        count(User, **test_condition)
    :param model_name:
    :param args:
    :param kwargs:
    :return: 0/Number（int）
    """
    result_count = db_session.query(model_name).filter(*args).filter_by(**kwargs).count()
    return result_count


def add(model_name, data):
    """
    添加信息
    :type data: object
    :type model_name: object
    :return None/Value of model_obj.PK
    """
    model_obj = model_name(**data)
    try:
        db_session.add(model_obj)
        db_session.commit()
        return inspect(model_obj).identity[0]
    except Exception as e:
        db_session.rollback()
        raise e


def edit(model_name, pk_id, data):
    """
    编辑信息
    :param model_name: 编辑的模型
    :param pk_id: 编辑数据的主键
    :type data: 编辑的数据
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db_session.query(model_name).filter(model_pk == pk_id)
        result = model_obj.update(data)
        db_session.commit()
        return result
    except Exception as e:
        db_session.rollback()
        raise e

def merge(model_name):
    try:
        db_session.merge(model_name)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        raise e


def delete(model_name, pk_id):
    """
    删除信息
    :param model_name: 删除的模型
    :type pk_id: 删除的主键
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db_session.query(model_name).filter(model_pk == pk_id)
        result = model_obj.delete()
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        raise e


def get_rows(model_name, page=1, per_page=10, *args, **kwargs):
    """
    获取信息列表（分页）
    Usage:
        items: 信息列表
        has_next: 如果本页之后还有超过一个分页，则返回True
        has_prev: 如果本页之前还有超过一个分页，则返回True
        next_num: 返回下一页的页码
        prev_num: 返回上一页的页码
        iter_pages(): 页码列表
        iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2) 页码列表默认参数
    :param model_name:
    :param page:
    :param per_page:
    :param args:
    :param kwargs:
    :return: None/object
    """
    rows = model_name.query. \
        filter(*args). \
        filter_by(**kwargs). \
        order_by(inspect(model_name).primary_key[0].desc()). \
        paginate(page, per_page, False)
    return rows


def insert_rows(model_name, data_list):
    """
    批量插入数据（遇到主键/唯一索引重复，忽略报错，继续执行下一条插入任务）
    注意：
    Warning: Duplicate entry
    警告有可能会提示：
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 17-20: ordinal not in range(128)
    处理：
    import sys

    reload(sys)
    sys.setdefaultencoding('utf8')

    sql 语句大小限制
    show VARIABLES like '%max_allowed_packet%';
    参考：http://dev.mysql.com/doc/refman/5.7/en/packet-too-large.html

    :param model_name:
    :param data_list:
    :return:
    """
    try:
        # result = db_session.execute(model_name.__table__.insert().prefix_with('IGNORE'), data_list)
        result = None
        if isinstance(model_name,Table):
            result = db_session.execute(model_name.insert(),data_list)
        else:
            result = db_session.execute(model_name.__table__.insert(), data_list)
        db_session.commit()
        return result.rowcount
    except Exception as e:
        db_session.rollback()
        raise e


def update_rows(model_name, data, *args, **kwargs):
    """
    批量修改数据
    :param model_name:
    :param data:
    :param args:
    :param kwargs:
    :return:
    """
    try:
        model_obj = db_session.query(model_name).filter(*args).filter_by(**kwargs)
        result = model_obj.update(data, synchronize_session=False)
        db_session.commit()
        return result
    except Exception as e:
        db_session.rollback()
        raise e


def update_rows_by_ids(model_name, pk_ids, data):
    """
    根据一组主键id 批量修改数据
    """
    model_pk = inspect(model_name).primary_key[0]
    try:
        model_obj = db_session.query(model_name).filter(model_pk.in_(pk_ids))
        result = model_obj.update(data, synchronize_session=False)
        db_session.commit()
        return result
    except Exception as e:
        db_session.rollback()
        raise e
