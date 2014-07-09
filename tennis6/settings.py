# Scrapy settings for tennis6 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tennis6'

SPIDER_MODULES = ['tennis6.spiders']
NEWSPIDER_MODULE = 'tennis6.spiders'

ITEM_PIPELINES = [
                  
                  'tennis6.pipelines.MySQLStorePipeline'
                  ]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tennis6 (+http://www.yourdomain.com)'
