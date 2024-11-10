import requests,time
from loguru import logger

class BM:
    def init(self,config):
        self.config = config

    def get_dynamic(self):
        url="https://mall.bilibili.com/mall-c-search/items/info"
        params = {
            'itemsId': self.config['item_id'],
            'shopId': '',
            'itemsVersion': '',
            'v': time.time()*1000,  # 13位时间戳
            }
        try:
            response=requests.get(url,params=params,headers=self.config['headers'])
        except (requests.exceptions.Timeout,
            requests.exceptions.ReadTimeout,
            requests.exceptions.ConnectionError
            ) as e:
            logger.error(" 服务器无响应")