# -*- coding: utf-8 -*-
import scrapy
import xlrd
import xlsxwriter
import xlwt
import os
from scrapy_selenium import SeleniumRequest
from xlutils.copy import copy

class ScrapenamesSpider(scrapy.Spider):
    name = 'scrapenames'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']


    def start_requests(self):
        path=os.path.abspath(os.curdir) + "\crawler3ads.xlsx"
        data_sheets=xlrd.open_workbook(path)
        numbersheets=len((data_sheets.sheet_names()))
        wb = copy(data_sheets)


        # sheet=data_sheets.sheet_by_name('dry cleaning  317')


        # print()
        # print(sheet.cell_value(18,8),numbersheets,sheet.nrows)
        # print()




        for ind in range(numbersheets):
            sheet=data_sheets.sheet_by_index(ind)
            number_of_rows=sheet.nrows
            w_sheet=wb.get_sheet(ind)
            for i in range(1,number_of_rows):

                    yield SeleniumRequest(
                        url="https://"+sheet.cell_value(i,8),
                        wait_time=1000,
                        screenshot=True,
                        callback=self.parse,
                        meta={'sheet_number':ind,'row_number':i,'w_sheet':w_sheet,'wb':wb},
                        dont_filter=True
                    )


    def parse(self, response):
        w_sheet = response.meta['w_sheet']
        sheet_number = response.meta['sheet_number']
        row_number = response.meta['row_number']
        wb = response.meta['wb']
        print()
        print()
        print('check',sheet_number,row_number)
        print(response.request.url)
        w_sheet.write(row_number,9,response.request.url)
        wb.save('check.xls')



