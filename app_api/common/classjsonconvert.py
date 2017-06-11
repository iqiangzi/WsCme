import json

def obj2dict(o):
    d={}
    d["__class__"]= o.__class__.__name__
    d["__module__"] = o.__module__
    d.update(o.__dict__)
    return d


def dict2obj(d):
    if "__class__" in d:
        class_name = d.pop("__class__")
        module_name = d.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode("UTF-8"),value) for key,value in d.items())
        instance = class_(args)
        # for k,v in args.items():
        #     print(getattr(instance,str(k)))
            # print(k)
            # if hasattr(instance,str(k)):
            #     print(k)
        # instance = class_()
    else:
        instance = d
    return instance