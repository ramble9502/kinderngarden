from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.jktree import Jktree
#from conf.config import DBSession, log_format, log_file, log_path, log_open, img_save_path
from spiders.mmready import Mmready
from spiders.mombaby import Mombaby
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
import logging
from datetime import datetime


def run_spider():
    settings = Settings()
    settings.set("COOKIES_ENABLES", False)  # 禁止cookies追踪
    settings.set("ITEM_PIPELINES", {
        'pipelines.ImgPipline': 150,  # 保存图片到本地
        'pipelines.SaveCommonPipline': 200,  # 保存数据库
    })
    settings.set("DOWNLOADER_MIDDLEWARES", {
        'downloaderMiddlewareSet.IngoreHttpRequestMiddleware': 1,  # redis去重
        #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 自动useragent
        #'downloaderMiddlewareSet.SetUserAgentMiddleware': 400,  # 设置useragent
        #'downloaderMiddlewareSet.SetProxyMiddleware': 750,  # 设置代理
        'homework3.pipelines.Homework3Pipeline': 2,
        'homework3.pipelines.OnePipeline': 3,
        'homework3.pipelines.TwoPipeline': 4,
    })
    settings.set("LOG_STDOUT ", False)
    settings.set("COOKIES_ENABLED", False)
    settings.set("RETRY_ENABLED", False)
    settings.set("REDIRECT_ENABLED", False)
    settings.set("DOWNLOAD_DELAY", 3)
    settings.set("DOWNLOAD_TIMEOUT", 15)
    settings.set("TELNETCONSOLE_ENABLED", False)
    configure_logging(install_root_handler=False)
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(Mmready)
    process.crawl(Jktree)
    process.crawl(Mombaby)
    process.start()


if __name__ == '__main__':
    run_spider()
