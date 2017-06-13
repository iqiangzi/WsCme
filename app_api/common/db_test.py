import unittest


class TestDB(unittest.TestCase):
    """
    数据库操作测试用例
    """

    def setUp(self):
        """
        测试前准备环境的搭建
        """
        # from app_api.database import init_db
        # init_db()

    def test_cud(self):
        """测试增删改"""
        print(self.test_cud.__doc__.strip())
        from app_api.common.db import add, edit, delete
        from app_api.entity.examination.training_institution import TrainingInstitutionCategory
        category_info = {
            "Desc": 0,
            "Name": "公共科目培训"
        }
        addid = add(TrainingInstitutionCategory, category_info)
        edit_success_count = edit(TrainingInstitutionCategory, addid, {"Name": "sss","Desc":1})
        # del_success_count = delete(TrainingInstitutionCategory, addid)

        assert len(addid) == 32
        assert edit_success_count == 1
        # assert del_success_count == None

    def tearDown(self):
        """
        测试后环境的还原
        """
        from app_api.common.db import db_session
        db_session.remove()
        pass


if __name__ == "__main__":
    unittest.main()
