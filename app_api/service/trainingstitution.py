from app_api.entity.examination.training_institution import TrainingInstitution,\
    TrainingInstitutionCategory,TrainingInstitutionAccount
from app_api.common.db import add,db_session
from passlib.apps import custom_app_context as pwd_context
from flask import abort
from app_api.common.exception_custom import ArgumentException

class TrainingstitutionService(object):
    def create(self,data,**kwargs):
        """
        新建一个培训点
        :type data: 培训点数据
        """
        db_session.begin_nested()
        addkey_training = add(TrainingInstitutionCategory,object)


        account_name = kwargs.pop("accountname",None)
        apply_name = kwargs.pop("applyname",None)

        if "applyname" in kwargs and not apply_name:
            raise ArgumentException("考点名称不能为空")


        if not account_name:
            raise ArgumentException("培训点账号必须提供")

        account_info = {
            "Name":account_name,
            "PassWordHash":pwd_context.encrypt("123456"),
            "TrainingInstitutionId":addkey_training,
            "ApplyName":apply_name
        }
        addkey_account = add(TrainingInstitutionAccount,account_name)
        db_session.commit()
