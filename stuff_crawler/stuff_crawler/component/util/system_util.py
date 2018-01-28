import platform
#判断平台操作系统
class SystemUtil:
    def getPlatform(self):
        sysstr = platform.system()
        if (sysstr == "Windows"):
            print("Call Windows tasks")
            return "window"
        elif (sysstr == "Linux"):
            print("Call Linux tasks")
            return "linux"
        else:
            print("Other System tasks")
            return "other"
