import unittest
import uuid


def addUUID(*arg):
    for c in arg:
        c.update(Id=uuid.uuid4().hex)


class TestDB(unittest.TestCase):
    """
    数据库操作测试用例
    """

    def setUp(self):
        """
        测试前准备环境的搭建
        """

    def test_insertrow(self):
        """测试批量插入 - 初始化培训点分类、类别字典"""
        print(self.test_insertrow.__doc__.strip())
        from app_api.common.db import insert_rows, add,get_row,db_session
        from app_api.entity.examination.training_institution import TrainingInstitutionCategory,\
            TrainingInstitutionType,TrainingInstitution,TrainingInstitutionAccount
        from app_api.entity.manytomany import TrainingInstitutionAndCategory
        categorylist = [
            {"Name": "公共科目培训"},
            {"Name": "专业协会"}
        ]
        addUUID(*categorylist)
        rowcount_category = insert_rows(TrainingInstitutionCategory, categorylist)
        assert rowcount_category >= 0

        typelist = [
            {"Name": "专业技术人员"},
            {"Name": "公务员"}
        ]
        addUUID(*typelist)
        rowcount_type = insert_rows(TrainingInstitutionType, typelist)
        assert rowcount_type >= 0

        librarycategory = {"Name": "2017年继续教育试题"}
        from app_api.entity.examination.testlibrary import LibraryCategory

        addkey_librarycategory = add(LibraryCategory, librarycategory)
        assert len(addkey_librarycategory) == 32

        trainginstitution_category = get_row(TrainingInstitutionCategory, Name="公共科目培训")
        if not trainginstitution_category:
            raise Exception("未找到培训点")
        trainginstitutionlist = [
            {"Name": "市直·继续教育·淄博市人事培训中心"},
            {"Name": "市直·继续教育·淄博市卫生人才中心"},
            {"Name": "张店区·继续教育·淄博职业学院"},
            {"Name": "淄川区·继续教育·淄博理工学校"},
            {"Name": "博山区·继续教育·博山一职专"},
            {"Name": "临淄区·继续教育·淄博工业学校"},
            {"Name": "周村区·继续教育·周村职业中等专业学校"},
            {"Name": "桓台县·继续教育·桓台县人社局"},
            {"Name": "高青县·继续教育·高青县人社局"},
            {"Name": "沂源县·继续教育·淄博职业学院"},
            {"Name": "高新区组织人事部"},
            {"Name": "市直·继续教育·淄博市教师教育办公室"},
            {"Name": "张店区教育局培训点"},
            {"Name": "淄川区教育中心培训点"},
            {"Name": "博山区教研室培训点"},
            {"Name": "周村区教体局培训点"},
            {"Name": "临淄区教育局培训点"},
            {"Name": "桓台县教体局培训点"},
            {"Name": "沂源县教体局培训点"},
            {"Name": "高青县教育局报名点"},
            {"Name": "高新区教研室报名点"},
            {"Name": "测试培训点"},
            {"Name": "全市·公务员培训·系统测试点"},
            {"Name": "全市·继续教育·系统测试点"},
            {"Name": "农业系统竞赛"},
            {"Name": "市直·公务员培训·淄博市人社局"},
            {"Name": "张店区·公务员培训·张店区人社局"},
            {"Name": "淄川区·公务员培训·淄川区人社局"},
            {"Name": "博山区·公务员培训·博山区人社局"},
            {"Name": "临淄区·公务员培训·临淄区人社局"},
            {"Name": "周村区·公务员培训·周村区人社局"},
            {"Name": "桓台县·公务员培训·桓台县人社局"},
            {"Name": "高青县·公务员培训·高青县人社局"},
            {"Name": "沂源县·公务员培训·沂源县人社局"},
            {"Name": "高新区·公务员培训·高新区人社局"},
            {"Name": "文昌湖·继续教育·文昌湖人社局"},
            {"Name": "市直·继续教育·淄博职业学院"},
            {"Name": "淄博市人才市场"},
            {"Name": "文昌湖·公务员培训·文昌湖人社局"},
            {"Name": "市直·继续教育·淄博师范高等专科学校"}
        ]
        addUUID(*trainginstitutionlist)
        traing_category = []

        for c in trainginstitutionlist:
            d={}
            d.update(TrainingInstitutionId=c["Id"],CategoryId=trainginstitution_category.Id)
            traing_category.append(d)

        db_session.begin_nested()
        rowcount_traing = insert_rows(TrainingInstitution,trainginstitutionlist)
        rowcount_training_and_category = insert_rows(TrainingInstitutionAndCategory,traing_category)
        db_session.commit()

        assert rowcount_training_and_category == len(traing_category)
        assert rowcount_traing == len(trainginstitutionlist)

        training = get_row(TrainingInstitution, Name="市直·继续教育·淄博市人事培训中心")

        training_account = {
            "Name":"SZJJ_ZBRSPXZX",
            "PassWordHash":"123456",
            "UsbKey":"123123",
            "TrainingInstitutionId":training.Id
        }


        addkey = add(TrainingInstitutionAccount, training_account)
        # addkey = db_session.add(training)
        # db_session.commit()

    def test_Add(self):
        pass


    def tearDown(self):
        """
        测试后环境的还原
        """
        from app_api.common.db import db_session
        db_session.remove()
        pass

    if __name__ == "__main__":
        unittest.main()
