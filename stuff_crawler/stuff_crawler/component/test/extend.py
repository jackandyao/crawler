class CommonUtil:
    def add(self,a,b):
        return a+b



class TbUtil(CommonUtil):
    def show(self,a,b):
        print('tb...')
        # return self.add(a,b)
        return super(TbUtil,self).add(a,b)


class JDUtil(CommonUtil):
    def show(self,a,b):
        print('jd...')
        # return self.add(a,b)
        return super(JDUtil,self).add(a,b)

#条件工厂
class ConditionFactory:
    CONDITION_TYPE_TB ="TB"
    CONDITION_TYPE_JD = "JD"

    def getCondtionInstance(self,type):
        if (type == self.CONDITION_TYPE_TB):
            return TbUtil
        elif (type == self.CONDITION_TYPE_JD):
            return JDUtil
        else:
            return None


if __name__ == '__main__':
   cf =  ConditionFactory
   # taobaoInstance = cf().getCondtionInstance("TB")()
   # result = taobaoInstance.show(3,5)

   jdInstance = cf().getCondtionInstance("JD")()
   print('result',jdInstance.show(22,9))