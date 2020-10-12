class Repeat:
    def __init__(self):
        self.old = {}     #已有的数字组合
        self.sign = {}       #已有的符号组合
    #检测是否式子重复
    def isRepeat(self,nlist,slist):
        nlist.sort()
        slist.sort()
        if self.old:
            for key,value in self.old.items():
                if value==nlist and self.sign[key]==slist:
                    return False
            self.old[key+1] = nlist
            self.sign[key+1] = slist
        else:
            self.old[0]  = nlist
            self.sign[0] = slist
        return True
