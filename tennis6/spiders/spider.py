# coding: utf8
from scrapy.spider import Spider
from scrapy.selector import Selector
from tennis6.items import Tennis6Item
from bs4 import BeautifulSoup
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import urllib
import urllib2

def getALLPageURLs(nextURLs):
        urls=[]
        pageSize =180

        for link in nextURLs:
            temp=link
            url=link
            for i in range(pageSize):
                if(i>=2):
                    url=temp+str(i)+".html"
                    


                    
                urls.append(url)
         
        return urls



class Spider(Spider):
    name = "tennis"
    #allowed_domains = ["http://www.6tennis.com/"]
   
   # start_urls = getStartUrls()      #得到所有网球场馆
    

    
    start_urls=["http://www.6tennis.com/court"]  #得到第一页网球场馆

  
    def parse(self, response):

        sel = Selector(response)
        
        open('startPage.html', 'wb').write(response.body)

        
        nextURLs = sel.xpath('//div[@class="city_list"]/a/@href').extract()

       
        
        nextURLs=getALLPageURLs(nextURLs)

        
        print "nextURLs:***************"

        print nextURLs

        
        
        for link in nextURLs:
                
            yield Request(link, self.parseCityURLs) 
       


    



    def parseCityURLs(self, response):

        sel = Selector(response)
        
        

            
        nextURLs = sel.xpath('//div[@class="content_info"]/div/a/@href').extract()

        


        
        for link in nextURLs:
                
            yield Request(link, self.getItem) 





    def getItem(self, response):
      try:
        
        sel = Selector(response)
        

        
       
        item=Tennis6Item()
        item['title'] = sel.xpath('//div[@class="jl_detail_l_name"]/span[1]/text()').extract()
        item['des'] = sel.xpath('//div[@class="jieshao"]/p/text()').extract()
        item['city'] = sel.xpath('//div[@class="detail_content"]/div[1]/text()').extract()
        item['level'] = sel.xpath('//div[@class="detail_content"]/div[2]/text()').extract()
        item['courtNumber'] = sel.xpath('//div[@class="detail_content"]/div[3]/text()').extract()
        item['priceStart'] = sel.xpath('//div[@class="detail_content"]/div[4]/b/text()').extract()
        item['priceEnd'] = sel.xpath('//div[@class="detail_content"]/div[4]/b[2]/text()').extract()
        item['phone'] = sel.xpath('//div[@class="detail_content"]/div[5]/text()').extract()
        item['address'] = sel.xpath('//div[@class="detail_content"]/div[6]/text()').extract()

        # if(len(item['des'])<1):
            
        #     item['des'] = sel.xpath('//div[@class="jieshao"]/text()').extract()
        if(len(item['des'])<1):
            print "%%%%%%%%%%%%%%%%%%"
            print "%%%%%%%%%%%%%%%%%%"
            item['des'] = sel.xpath('//div[@class="jieshao"]').extract()

        if(len(item['des'])<1):
            item['des'] = sel.xpath('//div[@class="jieshao"]/*').extract()
        return item


      except Exception,ex:
            print Exception,":",ex


        
        

        # try:
        #    print "***************************"
           
        #    print item['title'][0]
        #    print item['des'][0]
        #    print item['city'][0]
        #    print item['level'][0]
        #    print item['courtNumber'][0]
        #    print item['priceStart'][0]
        #    print item['priceEnd'][0]
        #    print item['phone'][0]
        #    print item['address'][0]

        #    print "***************************"

        # except Exception,ex:
        #        print Exception,":",ex


        
        
        

        
  





