import scrapy

class JobSpider(scrapy.Spider):
    name = 'job'
    start_urls = ['https://www.lagou.com/']

    def parse(self, response):
        for job in response.xpath('//ul[@class="clearfix position_list_ul"]/li'):
            yield {
                    'name': job.xpath('.//@data-positionname').extract_first(),
                    'salary': job.xpath('.//@data-salary').extract_first(),
                    'company': job.xpath('.//@data-company').extract_first(),
                    'address': job.xpath('.//div[@class="pli_btm clearfix"]/div[1]/div[@class="industry wordCut"]/span[3]/text()').extract_first()
                    }
