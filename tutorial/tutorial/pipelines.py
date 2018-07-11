# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def __init__(self):
        self.file = open('music.csv', 'a')
        self.csv_writer = csv.writer(self.file)
        self.csv_writer.writerow(["song_name", "singer_name","year", "class_", "rating_nums"])
    def process_item(self, item, spider):
        line = [item["song_name"], item["singer_name"], item["year"], item["class_"], item["rating_nums"]]
        self.csv_writer.writerow(line)
        return item
