# this is use python script!
# -*- coding: UTF-8 -*-
#自定义常量
import sys
class CrawlerConstant:
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.ConstError('Can not change const.{0}'.format(name))
        if not name.isupper():
            raise self.ConstCaseError(
                'const name {0} is not all uppercase.'.format(name))
        self.__dict__[name] = value
sys.modules[__name__] = CrawlerConstant()