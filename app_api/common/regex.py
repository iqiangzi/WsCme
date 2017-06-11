import re

class ReplaceTagItemToListItem(object):

    def __init__(self,*args,**kwargs):
        """

        :type regex: 正则表达式
        :type context: 带标签的正文字符串
        """
        args = list(args)
        if not args:
            raise Exception("第一个参数是被替换的正文文本，必须提供")

        self.context = args[0]
        self.regexstr = kwargs.pop("regex",u"\$(?P<name>[A-Z0-9]+)\$")
        self.replaceitem = list(kwargs.pop("replaceitem",None))
        self.replacedict = {}

        if not self.replaceitem:
            raise Exception("参数replaceitem为要替换的文本列表，必须提供")

    def __replace(self,m):
        return "{tag}://{path}".format(tag=m.group(1), path=self.replacedict[m.group(1)])

    def getcontext(self):
        regex = re.compile(self.regexstr)
        taglen = regex.findall(self.context).__len__()
        replacelen = self.replaceitem.__len__()

        if taglen != replacelen:
            raise Exception("正文文本标签[{tag}]与替换列表[{item}]不匹配"
                            .format(tag=regex.findall(self.context).__str__(),
                                    item=self.replaceitem.__str__()))
        taglist = regex.findall(self.context)
        self.replacedict = dict(zip(taglist,self.replaceitem))

        return regex.sub(self.__replace,self.context)

# if __name__ == "__main__":
#     l = ["12","34"]
#     tools = ReplaceTagItemToListItem("请观看这幅图片$GIF$，找出$MP3$里面不通的地方是？",replaceitem=[1,2])
#     print(tools.getcontext())
#     # tools.getcontext()