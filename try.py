import scrapy
from banks.banks.spiders.BankSpider import BankspiderSpider
from scrapy.crawler import CrawlerProcess 


if __name__ == "__main__":
    # f = open('bank.', 'w')
    # f.close()
    process = CrawlerProcess({
        "FEEDS": {
        "bank.csv": {"format": "csv"},
        },
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(BankspiderSpider)
    process.start()  

# process.crawl(BankspiderSpider)
# process.start()Pm