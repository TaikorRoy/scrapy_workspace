# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class TutorialPipeline(object):

    def __init__(self):
        self.file = codecs.open('test_json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item))
        line = line.replace('\\r', '')
        line = line.replace('\\n', '')
        line = line.replace('\\t', '')
        line = line.replace('}', '},')
        self.file.write(line.decode("unicode_escape"))
        return item

    def close_spider(self, spider):
        """
        self.file.close()
        with open(TutorialPipeline.json_file_name, 'r', encoding='utf-8') as f:
            s = f.read()
            s.rstrip(',')
            s = '[' + s + ']'
        with open('MianBuJingHua.json', 'r', encoding='utf-8') as f:
            f.write(s)
        """