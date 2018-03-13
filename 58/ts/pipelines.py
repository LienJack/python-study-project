# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):
    #def __init__(self):
        #self.fh=open("G:/Python/study/result/1.txt","a")
    def process_item(self, item, spider):
        #print(item["title"])
        #print(item["money"])
        #print(item["stu"][0].encode("gbk"))

        for c in item["title"]:
            print(c.encode("gbk"))

        #for s in item["money"]:
            #print(s.encode("gbk"))

        print("---------")
        #self.fh.write(item["content"][0]+"\n"+item["stu"][0]+"\n"+item["link"][0]+"\n"+"--------------"+"\n")
        #self.fh.write(item["content"][0].encode("utf-8")+"\n")
        return item
    #def close_spider(self):
        #self.fh.close()