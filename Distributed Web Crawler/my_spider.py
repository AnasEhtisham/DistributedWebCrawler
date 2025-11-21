import scrapy
from scrapy.crawler import CrawlerProcess
import json
import logging

class EnhancedSpider(scrapy.Spider):
    name = 'enhanced'
    start_urls = [
        'https://www.wikipedia.org',
        'https://www.python.org',
        'https://www.stackoverflow.com',
        'https://www.github.com',
        'https://www.bbc.com',
        'https://edition.cnn.com'
    ]
    
    custom_settings = {
        'DEPTH_LIMIT': 2,  # Limit crawl depth to 2 levels
        'LOG_LEVEL': 'ERROR',
        'USER_AGENT': 'Mozilla/5.0',
    }

    def __init__(self):
        self.scraped_data = []

    def parse(self, response):
        # Log non-200 status codes
        if response.status != 200:
            logging.error(f"Failed to fetch {response.url}, Status code: {response.status}")
        
        item = {
            'url': response.url,
            'final_url': response.url,
            'status_code': response.status,
            'content_type': response.headers.get('Content-Type', '').decode('utf-8'),
            'title': response.css('title::text').get(default='No Title'),
            'meta_description': self.get_meta_tag(response, 'description'),
            'meta_keywords': self.get_meta_tag(response, 'keywords'),
            'link_count': len(response.css('a::attr(href)').getall()),
            'links': ", ".join(response.css('a::attr(href)').getall()[:5]),  # Limiting to 5 links
            'image_count': len(response.css('img::attr(src)').getall()),
            'images': ", ".join(response.css('img::attr(src)').getall()[:5]),  # Limiting to 5 images
            'script_count': len(response.css('script::attr(src)').getall()),
            'scripts': ", ".join(response.css('script::attr(src)').getall()[:5])  # Limiting to 5 scripts
        }

        self.scraped_data.append(item)

        # Follow 3 links per page max to avoid deep recursion
        for link in response.css('a::attr(href)').getall()[:3]:
            yield response.follow(link, self.parse, errback=self.handle_error)

    def closed(self, reason):
        # Save to JSON on spider close
        with open("scraped_data.json", "w") as f:
            json.dump(self.scraped_data, f, indent=2)

    def get_meta_tag(self, response, name):
        """ Helper function to extract meta tags like description and keywords """
        meta_tag = response.css(f'head meta[name="{name}"]::attr(content)').get()
        if not meta_tag:
            meta_tag = response.css(f'head meta[property="og:{name}"]::attr(content)').get()
        if not meta_tag:
            logging.warning(f"Meta tag '{name}' not found in {response.url}")
        return meta_tag if meta_tag else ''

    def handle_error(self, failure):
        """ Handle errors during link following """
        logging.error(f"Error occurred while following link: {failure.request.url}, Error: {failure.value}")

# Run the spider
process = CrawlerProcess(settings={
    "LOG_LEVEL": "ERROR",
    "USER_AGENT": "Mozilla/5.0",
    'DEPTH_LIMIT': 2  # Control crawl depth here
})
process.crawl(EnhancedSpider)
process.start()
