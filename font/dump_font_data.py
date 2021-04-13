#coding: utf-8
import numpy as np
import cv2
import struct

MISAKI_PATH = "./8x8DotJPFont/misaki_png_2015-04-10/"
MISAKI_HALF_PNG = MISAKI_PATH+"misaki_4x8_jisx0201.png"
MISAKI_PNG      = MISAKI_PATH+"misaki_gothic.png"

class Misaki():
    def __init__(self):
        self.img_half = cv2.imread(MISAKI_HALF_PNG)
        self.img = cv2.imread(MISAKI_PNG)
        self.put_byte=0

        delete_index=np.arange(7,94*8-1,8)[::-1]

        for del_x in delete_index:
            self.img=np.delete(self.img, del_x,1)

    def get(self,ku,ten):
        return self.img[(ku-1)*8:ku*8, (ten-1)*8:(ten)*8]

    def get_half(self,code):
        code=int(code)
        code_h = (code>>4)&0x0f
        code_l = code&0x0f
        return self.img_half[code_h*8:(code_h+1)*8, code_l*4:(code_l+1)*4]

    def byteconv(self,byte=[255,255,255,0,0,255,255,255]):
        ans=0
        for i,b in enumerate(byte):
            if b==0: # 0をbit1に
                ans+= 1<<(7-i)
        return ans

    def put_img_data_range(self, ku_range,ten_range):
        size=(ku_range[1]-ku_range[0]+1)*(ten_range[1]-ten_range[0]+1)
        vbyte=0
        for ku in range(ku_range[0],ku_range[1]): #第一水準漢字は16区から47区
            print("\n//ku: %d"%ku)
            for ten in range(ten_range[0],ten_range[1]): #1-80点
                img=self.get(ku,ten)
                img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 0が黒、255が背景
                for i,byte in enumerate(img[:7,:8]):
                    d=self.byteconv(byte)
                    if i==6:
                        e=",\n"
                    else:
                        e=","
                    print("0x%02X"%d,end=e)

    def put_img_data_range_kana(self, ku_range,ten_range):
        size=(ku_range[1]-ku_range[0]+1)*(ten_range[1]-ten_range[0]+1)
        vbyte=0
        for ku in range(ku_range[0],ku_range[1]): #記号は1区から8区
            print("\n// ku: %d"%ku)
            for ten in range(ten_range[0],ten_range[1]): #1-80点
                img=self.get(ku,ten)
                img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 0が黒、255が背景
                for i,byte in enumerate(img[:7,:8]):
                    d=self.byteconv(byte)
                    if i==6:
                        e=",\n"
                    else:
                        e=","
                    print("0x%02X"%d,end=e)

    def put_img_data(self):

        print("byte[] font_data = {")

        ku_range=[1,2] #1区のみ
        ten_range=[1,83] #94*7/8
        self.put_img_data_range_kana( ku_range,ten_range)

#        ku_range=[1,8] #記号入り
#        ku_range=[1,6] #記号ぬき
        ku_range=[3,6] #記号ぬき
        ten_range=[1,83]
        self.put_img_data_range_kana( ku_range,ten_range)

        ku_range=[16,47]
        ten_range=[1,83]
        self.put_img_data_range( ku_range,ten_range)

        print("};")
        print("int font_data_end;")

    def euc2img(self, dat):

        l=len(dat)
        i=0

        imgs=[]
        while(True):
            dh=dat[i]
            i+=1
            if dh<0x80: # ascii
                print("%x" % dh)
                img=self.get_half(dh)
                if imgs==[]:
                    imgs=img
                else:
                    imgs=np.hstack((imgs,img))
            if dh>=0xA0:
                dl=dat[i]
                i+=1
                ku=dh-0xa0
                ten=dl-0xa0
                print("%x %x" % (ku,ten))
                img=self.get(ku,ten)
                if imgs==[]:
                    imgs=img
                else:
                    imgs=np.hstack((imgs,img))
            if i>l-1:
                break
        return imgs

if __name__ == "__main__":

    misaki = Misaki()
    misaki.put_img_data()

