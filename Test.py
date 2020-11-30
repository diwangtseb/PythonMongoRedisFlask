# import json
# #case 1
# score=input("输入成绩:")
# if score>"60":
#     print("您及格了")
# else:
#     print("不及格")
#
# #case 2
# randNum= input("输入任意三个数（按照空格分开）:").split(' ')
# randNum=list(map(int,randNum))
# randNum.sort()
# print(randNum)
#
# #case 3
# innum=int(input("输入一个整数："))
# if innum%5==0 and innum%7==0:
#     print(f"{innum}能同时被5和7整除")
# else:
#     print(f"{innum}不能同时被5和7整除")
#
# #case 4
# inyear=int(input("输入一个年份："))
# if inyear%4==0:
#     print(f"{inyear}年是闰年")
# else:
#     print(f"{inyear}年不是闰年")
#
# #case 5
# instudentNum=input("输入一个学号：")
# if instudentNum[-1:]=="1" or instudentNum[-1:]=="6":
#     print("赶紧的！上机测试")
# else:
#     print("行了！你挺幸运不用参加上机测试")
#
# #caset 2-1
# weight=input("输入体重Kg(如：80)：")
# height=input("输入身高(如：1.71)：")
# Bmi=float(weight)/(float(height)*float(height))
# if Bmi<18.5:
#     print("偏瘦")
# elif Bmi>=18.5 and Bmi<24:
#     print("正常")
# elif Bmi>=24 and Bmi<28:
#     print("偏胖")
# else:
#     print("肥胖")
#
# dict={"90-100":{"A",4.00},"86-89.9":{"A-",3.67},"83-85.9":{"B+",3.33},"80-82.9":{"B",3.00},
#       "76-79.9":{"B-",2.67},"73-75.9":{"C+",2.33},"70-72.9":{"C",2.00},"66-69.9":{"C-",1.67},
#       "63-65.9":{"D+",1.33},"60-62.9":{"D",1.00}}
# a=input("输入你的成绩：")
#
# for i in dict.keys():
#     if float(i.split('-')[0])<=float(a)<=float(i.split('-')[1]):
#         print(f"您的绩点为：{list(dict[i])[0]}，字母记分制：{list(dict[i])[1]}")
#         break
#     elif float(a)<60:
#         print("您的绩点心里没点数吗没及格：0.00,字母记分制：F")
#         break
import json

# 读取json文件内容,返回字典格式
with open('MSPermissionsClass.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    print(json_data)

myList=[]
for i in json_data:
    myList.append(i['Department'])

myList=list(set(myList))
print(myList)
otherList=[]
for i in json_data:
    if i['Department'] ==myList[0]:
        otherList.append(i['Product']['ProductName'])
otherList=list(set(otherList))



myyylist=[]
for i in myList:
    a=[]
    myyylist.append({'Department': i,'Product':a})
    for j in otherList:
        b = []
        a.append({'ProductName':j,'Roles':b})        
        for k in json_data:
            if k['Department']==i and k['Product']['ProductName']==j:
                b.append(k['Product']['Roles'][0])

print(json.dumps(myyylist,ensure_ascii=False))



