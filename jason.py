#將python dump 成 jason
import encodings
import json
#一個字典檔
persons = [
    {
    'username':'wei'
    ,
    'age':'17'
    ,
    'country':'taiwang'


},
    {
    'username':'chan'
    ,
    'age':'12'
    ,
    'country':'china'

}
]
#將python檔轉成json檔
#可以在json.cn網站中確認是否轉檔成功
#jason_str=json.dumps(persons)
#print(type(jason_str))
#底下顯示的內容從單引號變成雙引號說明轉檔成功,因為json格式是雙引號來著,所以勁量用單引號來寫python格式
#print(jason_str)


                        #開啟utf-8將文字帶碼以encode刑事傳道json檔中,他原本帶有ascii轉文字記得在底下要關閉
with open('person','w',encoding='utf-8') as fp :
    fp.write('jason_str')
    #將上面字典轉成json然後存在fp內並將原本自帶的ascii碼關閉,
    # 如果上面字典當中有中文關閉了ascii就會將它翻譯讓他在文檔中也保持中文,
    # 將它關閉就會以代碼形式出現
    #asciii碼根decode不一樣的形式但功用是一樣的
    json.dump(persons,fp,ensure_ascii=False)#用dump函式來將python變成json
