import scrapy


class QuotesSpider(scrapy.Spider):
    name = "music"
    start_urls = [
        'https://music.douban.com/top250?start=0',
    ]

    def parse(self, response):
        for mic in response.css('div.pl2'):
            yield {
                'song_name': mic.css('a::text').extract_first(),
                'singer_name': mic.css('p.pl::text').extract_first().split('/')[0],
                'year': mic.css('p.pl::text').extract_first().split('/')[1],
                'class_': mic.css('p.pl::text').extract_first().split('/')[-1],
                'rating_nums': mic.css('span.rating_nums::text').extract_first(),
            }
        next_page = response.css("span.next a::attr(href)").extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)