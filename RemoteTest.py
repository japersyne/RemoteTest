# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#第一題
def reverse(string):
    string = string[::-1]
    print (string)

def reverse2(string):
    str3 = ''
    for word in string:
        str2 = string.split(' ')
    for i in str2:
        i = i[::-1]
        str3 += i
        str3 += ' '
        print(str3)    

#第二題
x = input("input:")
x = int(x)
x = x + 1
count = 0
for i in range(x):
    if i == 0:
        continue
    if i%3 != 0:
        if i%5 != 0:
            count +=1
    if i%15 == 0:
        count +=1    
print(count)
'''
第三題：
step1:挑標示為混合的袋子，此袋子拿出鉛筆的話此袋子就可以確定是全為鉛筆，
      此袋子拿出原子筆的話此袋子就可以確定是全為原子筆。
step2:(1)拿出為鉛筆的情況：標示為原子筆的袋子為混合袋子，因為標示為原子筆的袋子
         不可能是全鉛筆袋（step1找出來了），因為標示的是錯的，也不可能是原子筆袋
         所以此標示為原子筆的袋子必為混合袋。
      (2)拿出為原子筆的情況：標示為鉛筆的袋子為混合袋子，因為標示為鉛筆的袋子
         不可能是全原子筆袋（step1找出來了），因為標示的是錯的，也不可能是鉛筆袋
         所以此標示為鉛筆的袋子必為混合袋。
第四題：
假設A,B,C三人原本每人有300元，服務生有0元。
round1:三人各出300，服務生得900。
A,B,C:0,0,0元
服務生:900元

round2:服務生返還30元給A,B,C
A,B,C:30,30,30元
服務生:810元

也就是說服務生的810元包含了自己暗槓的60元，所以810元應再加上3人的30元
也就是810+3*30=900元，這樣就合理了。
'''