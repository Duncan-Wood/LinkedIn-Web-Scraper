# import scrapy
# import json


# class LinkedInJobsSpider(scrapy.Spider):
#     name = "linkedin_jobs"
#     api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&start='

#     def start_requests(self):
#         first_job_on_page = 0
#         first_url = self.api_url + str(first_job_on_page)
#         yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

#     def parse_job(self, response):
#         first_job_on_page = response.meta['first_job_on_page']

#         job_item = {}
#         jobs = response.css("li")

#         num_jobs_returned = len(jobs)
#         print("******* Num Jobs Returned *******")
#         print(num_jobs_returned)
#         print('*****')

#         for job in jobs:
#             job_item['job_title'] = job.css(
#                 "h3::text").get(default='not-found').strip()
#             # can use job detail url later to get the full description of the job
#             job_item['job_detail_url'] = job.css(
#                 ".base-card__full-link::attr(href)").get(default='not-found').strip()
#             job_item['job_listed'] = job.css(
#                 'time::text').get(default='not-found').strip()

#             job_item['company_name'] = job.css(
#                 'h4 a::text').get(default='not-found').strip()
#             job_item['company_link'] = job.css(
#                 'h4 a::attr(href)').get(default='not-found')
#             job_item['company_location'] = job.css(
#                 '.job-search-card__location::text').get(default='not-found').strip()
#             yield job_item

#         if num_jobs_returned > 0:
#             first_job_on_page = int(first_job_on_page) + 25
#             next_url = self.api_url + str(first_job_on_page)
#             yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

import scrapy
import json
from scrapy.loader import ItemLoader
from  ..items import LinkedInJobItem

class LinkedInJobsSpider(scrapy.Spider):
    name = "linkedin_jobs"
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&start='

    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

    def parse_job(self, response):
        first_job_on_page = response.meta['first_job_on_page']

        jobs = response.css("li")
        num_jobs_returned = len(jobs)

        for index, job in enumerate(jobs):
            loader = ItemLoader(item=LinkedInJobItem(), selector=job)
            loader.add_css('job_title', 'h3::text')
            loader.add_css('job_detail_url', '.base-card__full-link::attr(href)')
            loader.add_css('job_listed', 'time::text')
            loader.add_css('company_name', 'h4 a::text')
            loader.add_css('company_link', 'h4 a::attr(href)')
            loader.add_css('company_location', '.job-search-card__location::text')
            loader.add_value('index', index)  # Assign the index

            yield loader.load_item()

        if num_jobs_returned > 0:
            first_job_on_page = int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})
