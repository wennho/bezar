from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ..items import ScraperItem
from copy import deepcopy

class CraigslistSpider( BaseSpider ):
    name = "craigs"
    allowed_domains = ["seattle.craigslist.org"]

    start_urls = [
        "http://seattle.craigslist.org/sss/",
    ]
    django_list = []
    domain = [
        "http://seattle.craigslist.org",
    ]

    def get_object_list( self ):
        return self.django_list

    def parse( self, response ):
        hxs = HtmlXPathSelector( response )
        rows = hxs.select( '//p[@class="row"]' )
        items = []
        for row in rows:
            item = ScraperItem()
            item['title'] = row.select( './/a[not(@class)]/text()' ).extract()
            item['create_datetime'] = row.select( './/span[@class="date"]/text()' ).extract()
            item['price'] = row.select( './/span[@class="price"]/text()' ).extract()
            item['location'] = row.select( './/span[@class="pnr"]/small/text()' ).extract()
            item['url'] = row.select( './/a[not(@class)]/@href' ).extract()
            item['domain'] = self.domain

            # hack for now to return objects
            self.django_list.append( item.save( commit = False ) )

            items.append( item )
        return items
