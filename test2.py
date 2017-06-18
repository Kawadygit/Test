#!/usr/bin/python
# coding: shift_jis
import re
from collections import Counter

f = open("20170509-Friend Chat.txt")
textname = "20170509-Friend Chat"
text = f.read()
f.close()

list = [
    ["natch",text.count("(natch)")],
    ["Slide",text.count("(Slide)")],
    ["Miyaichi",text.count("(Miyaichi)")],
    ["suto",text.count("(suto)")],
    ["msk",text.count("(msk)")],
    ["udon",text.count("(udon)")],
    ["monban",text.count("(monban)")],
    ["backlight",text.count("(backlight)")],
    ]

list2 = sorted(list, key=lambda x:x[1],reverse= True)

print " The most chatter Rankings on " + textname + "!"
print ("No1 :" + list2[0][0] +"!  " + str(list2[0][1]) + "times!")
print ("No2 :" + list2[1][0] +"!  " + str(list2[1][1]) + "times!")
print ("No3 :" + list2[2][0] +"!  " + str(list2[2][1]) + "times!")
