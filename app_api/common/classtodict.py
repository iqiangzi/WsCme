import inspect


def to_dict(self):
    # print(self.__dict__["Created"])
    """
    model 对象转 字典
    model_obj.to_dict()
    """
    # print(dir(self))
    # print(dir(self))
    for c in dir(self):
        # if inspect.isbuiltin(getattr(self,c)):
        #         return getattr(self, c.name, None)
        # print(getattr(self, c))
        print(hasattr(self, c))
