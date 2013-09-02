from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scraper.items import ScraperItem

class CraigslistSpider(BaseSpider):
    name = "craigs"
    allowed_domains = ["seattle.craigslist.org"]
    start_urls = [
        "http://seattle.craigslist.org/sss/",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//p[@class="row"]')
        items = []
        for row in rows:
            item = ScraperItem()
            item['title'] = row.select('.//a[not(@class)]/text()').extract()
            item['create_datetime']  = row.select('.//span[@class="date"]/text()').extract()
            item['price'] = row.select('.//span[@class="price"]/text()').extract()
            item['location'] = row.select('.//span[@class="pnr"]/small/text()').extract()
            item['url'] = row.select('.//a[not(@class)]/@href').extract()
            items.append(item)
        return items