import requests,time,json
from loguru import logger

class BM:
    def __init__(self,config):
        self.config = config

    def get_dynamic(self):
        url="https://mall.bilibili.com/mall-c-search/items/info"
        params = {
            'itemsId': self.config['item_id'],
            'shopId': '',
            'itemsVersion': '',
            'v': int(time.time()*1000),  # 13位时间戳
            }
        try:
            response=requests.get(url,params=params,headers=self.config['headers'])
            return response
        except (requests.exceptions.Timeout,
            requests.exceptions.ReadTimeout,
            requests.exceptions.ConnectionError
            ) as e:
            logger.error("服务器无响应")
    
    def save_config(self,config):
       with open("config.json","w") as f:
           json.dump(config,f)
       self.config=config