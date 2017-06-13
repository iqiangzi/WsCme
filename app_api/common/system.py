import os


def get_memory_usage():
    pid = os.getpid()
    cmd = "ps -p {0} -o rss=".format(pid)
    output = os.popen(cmd)
    result = output.read()
    if result == "":
        memory_usage_value = 0
    else:
        memory_usage_value = int(result.strip())
    memory_usage_format = memory_usage_value / 1024.0
    print("pid:%s内存使用%2fm" % (pid,memory_usage_format))

if __name__ =="__main__":
    get_memory_usage()
