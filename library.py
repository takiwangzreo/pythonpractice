a = 3
print(a.__abs__())#abs用來返回變數中的值
x1 = ascii("王威騰好帥")#用ascii碼顯示
print(x1)
x2 = bin(1110000000)#bin用來將數字轉成2進制的數字前面加一個0b
print(x2)
x = 11
print(bool(x>12))#bool用來對錯事物
print('==============================================================')
z = (200 ,100 ,10)
print(type(z))
f = x,bytearray#改變元組
print(type(f))#改變值得基本數據類型,strin也可以改變但要有encode碼,範圍是0 <= x < 256,迭代起也可以改變



print(chr(100))#chr返回一個unicode碼所代表的字
def simon(x,y):
    x=x
    y=y
    return (x+y)
print(simon(25,175))
print("========================================================")
class taki :
    x = "handsome"
    y = "brave"
    def health(x,y):
        x = x
        y = y
        return "true"
    @classmethod     #他的type直接就是taki
    def level(self,x,y):
        x = x
        y = y
        return "true"
mikasa = taki.health(2,4)
print(bool(taki.level(22,3)))
print(bool(mikasa))
print('=====================================================================')
y2="王威騰好帥又很聰明還非常乖"
import re
print(re.search("又很聰明",y2))#正則表達式第一種用法
p = "simon ias very handsome and smart"
print(re.search("simon i[ab]s very handsome",p))
print('=========================================================================')
def bubble_sort (x0):
    y = len(x0)
    if x0[0]>x0[1]:
        x0




x0 = [5,4,2,6,8,7,9]

