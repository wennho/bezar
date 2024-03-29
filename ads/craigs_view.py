from django.views import generic

from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy import log
from scraper.scraper.spiders.craigslist_spider import CraigslistSpider


class CraigsView( generic.ListView ):
    template_name = 'ads/scraped_index.html'
    context_object_name = 'scraped_ad_list'

    def get_context_data( self, **kwargs ):
        # Call the base implementation first to get a context
        context = super( CraigsView, self ).get_context_data( **kwargs )
        if 'q' in self.request.GET:
            context['search'] = self.request.GET['q']
        return context

    def get_queryset( self ):
        if 'q' in self.request.GET:
            return crawler.crawl( self.request.GET['q'] )
        else:
            return crawler.crawl()

class CrawlerScript():
    def __init__( self ):
        self.crawler = CrawlerProcess( Settings() )
        self.crawler.install()
        self.crawler.configure()
    def _crawl( self, queue, search ):
        log.start( loglevel = log.DEBUG )
        current_spider = CraigslistSpider()
        if search:
            current_spider.set_search_url( search )
        self.crawler.crawl( current_spider )
        self.crawler.start()
        self.crawler.stop()
        queue.put( current_spider.get_object_list() )
    def crawl( self, search = "" ):
        q = Queue()
        p = Process( target = self._crawl, args = ( q, search ) )
        p.start()
        p.join()
        return q.get()

crawler = CrawlerScript()
