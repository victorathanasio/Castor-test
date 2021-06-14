import scrapy
from scrapy_splash import SplashRequest
import pandas as pd


class sales_force_page_spyder(scrapy.Spider):
    name = 'sales_force_page'
    start_urls = [
        'https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_acceptedeventrelation.htm']

    def start_requests(self):
        # url = 'http://localhost:8050/render.html?url='
        url = 'https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_acceptedeventrelation.htm'

        yield SplashRequest(url)

    def parse(self, response):

        table_name = response.xpath("string(//h1[@class='helpHead1']/span)")[0].get()
        table_description = response.xpath("string(//span[@id='summary'])")[0].get()
        columns = response.css('table').getall()
        df = pd.read_html(columns[0])[0]

        df['Table Name'] = table_name
        df['Table Description'] = table_description
        df = df.rename(columns={'Details': 'Column Description',
                                'Field Name': ' Column Name'})

        cols = df.columns.tolist()
        cols = cols[-2:] + cols[:-2]

        df = df[cols]

        df.to_csv('sales_force.csv')
