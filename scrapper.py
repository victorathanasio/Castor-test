from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sanity_check import sanity_check
from Gdrive import to_gdrive
import schedule
import time

def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl('sales_force_page')
    process.start()


    sanity_check()

    to_gdrive()


if __name__ == '__main__':
    main()


# schedule.every().day.at("10:30").do(main)
#
# while True:
#     schedule.run_pending()
#     time.sleep(60)

