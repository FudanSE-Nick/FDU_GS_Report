from scrapy import cmdline
#cmdline.execute('scrapy crawl fdu_gs'.split())

#导出csv文件
cmdline.execute("scrapy crawl fdu_gs -o info.csv".split())