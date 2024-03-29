from scrapy.exceptions import DropItem

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ScraperPipeline(object):
    def process_item(self, item, spider):
        if item['price']:
            return item
        else:
            raise DropItem("Missing price in %s" % item)
