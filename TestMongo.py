# import pymongo
#
#
# myclient=pymongo.MongoClient('mongodb://localhost:27017/')
#
# myGoods=myclient["Goods"]
# myBooks=myGoods['Books']

#插入
#willBook={"name":"亲热天堂","price":180,"repertory":32}
# willBook=[{"name":"英雄联盟","price":1,"repertory":143},
#           {"name":"起凡三国","price":2,"repertory":23},
#           {"name":"三国战记","price":10,"repertory":33},
#           {"name":"斗破苍穹","price":200,"repertory":43},
#           {"name":"绝地求生","price":3,"repertory":44},
#           {"name":"新魂斗罗","price":5,"repertory":55},
#           {"name":"父亲养成","price":1000,"repertory":66},
#           {"name":"奇迹暖暖","price":4,"repertory":77},
#           {"name":"爱的供养","price":6,"repertory":99}]
#
# id=myBooks.insert_many(willBook)

#查询
# for i in myBooks.find():
#     print(i)

# res=myBooks.find({"name":"三国战记"})
# print(res[0])

#修改
#myBooks.update_one({"name":"三国战记"},{"$set":{"name":"奇迹三国"}})

#删除
# myBooks.delete_one({"name":"奇迹三国"})
# for i in myBooks.find():
#     print(i)

#排序
# a=myBooks.find().sort('price',-1)
# for i in a:
#     print(i)