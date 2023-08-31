"""This module contains the item class for the LinkedInJobItem"""
import scrapy

class LinkedInJobItem(scrapy.Item):
    """Class Representing a job item scraped from LinkedIn"""

    job_title = scrapy.Field()
    job_detail_url = scrapy.Field()
    job_listed = scrapy.Field()
    company_name = scrapy.Field()
    company_link = scrapy.Field()
    company_location = scrapy.Field()
    index = scrapy.Field()  # Add the index field
