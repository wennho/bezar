# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from ads.models import ScrapedAd

# Need to extract the string from the list returned
def delist( selector_list ):
    if selector_list:
        return selector_list[0]
    else:
        return ''

class ScraperItem( DjangoItem ):

    django_model = ScrapedAd

    def __setitem__( self, key, value ):
        super( ScraperItem, self ).__setitem__( key, delist( value ) )
