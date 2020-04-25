y = [1,2,3,4,5,6,7,8,9]
def bubble_sort(y):
    for i in range(len(y)-1,0,-1):#將數列的長度來算出數列中的位子編號
        for j in range(i):#將編號排序成一批,再將這批編號分開丟入式子中
            if y[j]>y[j+1]:
                temp = y[j]
                y[j]=y[j+1]
                y[j+1] = temp




def selection_sort(y):
    x=0
    x1=len(y)
    while x<x1:
        for i in range(len(y),1,-1):
            for j in range(i):
                if y[x]<y[j]:
                    temp = y[x]
                else:temp = y[j]
        for z in range(temp):
            print()

        x=x+1

selection_sort(y)
print(y)