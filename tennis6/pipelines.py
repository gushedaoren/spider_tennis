#coding utf8
from datetime import datetime
from hashlib import md5
from scrapy import log
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import time
import MySQLdb
import MySQLdb.cursors
import MySQLdb as mysql
import re

class MySQLStorePipeline(object):
    """A pipeline to store the item in a MySQL database.

    This implementation uses Twisted's asynchronous database API.
    """

    """docstring for MySQLstor"""
    def __init__(self):

        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'tennis',
            user = 'root',
            passwd = 'root',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
        )
    def process_item(self, item, spider):
        print spider
        # run db query in thread pool
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)

        return item
    def _conditional_insert(self, tx, item):
            print "start insert..............."

            title=""
            des=""
            province=""
            city=""
            district=""
            level=""
            courtNumber=""
            price=""
            phone=""
            address=""
        #try:
            print "***************************"

            if(len(item["title"])>=1):
                title= item['title'][0].strip()
                print title
            else:
                title=""

            if(len(item["des"])>=1):
                des= item['des'][0].strip()
                print des
            else:
                des=""

            if(len(item["city"])>=1):
                city=item['city'][0].strip()
                print city
                cityAndDistrict= re.split(' ',city)
               
                if(len(cityAndDistrict)>=3):


                  province=cityAndDistrict[0]
                  city=cityAndDistrict[1]
                  district=cityAndDistrict[2]
                  print province
                  print city
                  print district

            else:
                province=""
                city=""
                district=""

             
            if(len(item["level"])>=1):
                level= item['level'][0].strip()
                print level
            else:
                level=""

            if(len(item["courtNumber"])>=1):
            
                courtNumber= item['courtNumber'][0].strip()
                print courtNumber
            else:
                courtNumber=""


            
                

            if((len(item["priceStart"])>=1) and (len(item["priceEnd"])>=1)):
                priceStart= item['priceStart'][0].strip()
                priceEnd= item['priceEnd'][0].strip()
                price=priceStart+"-"+priceEnd;
                print priceStart
                print priceEnd
                print price
            else:
                price=""

            if(len(item["phone"])>=1):
                phone= item['phone'][0].strip()
                print phone
            else:
                phone=""

            if(len(item["address"])>=1):
                address= item['address'][0].strip()
                print address
            else:
                address=""


           
            print "***************************"

        # except Exception, e:
        #     print Exception,":",e
        #     raise
        # else:
        #     pass
        # finally:
        #     pass
        



        
              
            tx.execute(\
                "insert into spider (title, description,province, city, district, phone, address,level,court_number,price)\
                values (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)",

                (title,
                 des,
                 province,
                 city,
                 district,
                 phone,
                 address,
                 level,
                 courtNumber,
                 price)
                )


      

           

    def handle_error(self, e):
        log.err(e)


    