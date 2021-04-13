#!/usr/bin/env python
# coding: utf-8

# file="text_euc2.txt"

# dat = open(file, "rb").read()
import sys
#
filename=sys.argv[1]
dat = open(filename).read().encode('euc-jp')

dat=bytes(dat)

l=len(dat)
i=0
put_index=0
imgs=[]

print("const int TEXT_LENGTH = %d;" % (int(l/2)+1))
print("byte[] text_data = {")
while(True):
    dh=dat[i]
    i+=1
    if dh<0x80: # ascii
        print("0x00,0x%02x," % dh, end="")
        put_index+=1
    if dh>=0xA0:
        dl=dat[i]
        i+=1
        ku=dh-0xa0
        ten=dl-0xa0
        print("0x%02x,0x%02x," % (ku,ten),end="")
        put_index+=1
    if  put_index%8==0:
        print()
    if i>l-1:
        break
print("};")



