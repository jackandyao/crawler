# this is use python script!
# -*- coding: UTF-8 -*-
import urllib
import urllib.request
#下载验证码
class DwlImage:
    imgurl =''
    path =''
    def __init__(self,imgurl,path):
        self.imgurl=imgurl
        self.path = path

    #下载图片
    def dwlImg(self):
        request = urllib.request.Request(self.imgurl)
        response = urllib.request.urlopen(request)
        dwl_img = response.read()
        with open('../image/'+self.path+"/"+".jpg",'wb') as fp:
            fp.write(dwl_img)
            print('验证码图片下载完成!!')
        return


# url = ''
# path ='001'
# dwl = DwlImage(url,path)
# dwl.dwlImg()