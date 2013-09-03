from django.views import generic
from ads.models import ScrapedAd


from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scraper.scraper.spiders.craigslist_spider import CraigslistSpider
from scrapy.xlib.pydispatch import dispatcher

def stop_reactor():
    reactor.stop()

class CraigsView(generic.ListView):
    template_name = 'ads/scraped_index.html'
    context_object_name = 'scraped_ad_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CraigsView, self).get_context_data(**kwargs)
        if 'q' in self.request.GET:
            context['search'] = self.request.GET['q']
        return context


    def get_queryset(self):
        spider = CraigslistSpider()
        crawler = Crawler(Settings())
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start(loglevel=log.DEBUG)
        log.msg('Running reactor...')
        reactor.run(installSignalHandlers=0)  # the script will block here until the spider is closed
        log.msg('Reactor stopped.')



        if 'q' in self.request.GET:
            search_words = self.request.GET['q'].strip().split()
            for word in search_words:
                queryset = queryset.filter(title__icontains=word)
        return spider.get_object_list()
