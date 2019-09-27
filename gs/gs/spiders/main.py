from scrapy import cmdline
#cmdline.execute('scrapy crawl fdu_gs'.split())

cmdline.execute("scrapy crawl fdu_gs -o info.csv".split())