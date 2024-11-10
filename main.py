import random
from loguru import logger

from Scripts.init import *
from Scripts.utility import *
from Scripts.api import *

version="1.0.0"

if __name__ == '__main__':
    init(version)
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
        +str(random.randint(1,999))
    }
    if not is_load_config():
        config={}
        config["item_id"]=noneprompt.InputPrompt(
            question="请输入商品id"
        ).prompt()
        config["sleep"]=noneprompt.InputPrompt(
            question="请输入每轮检测间隔时间(秒)，过快可能会触发风控",
            default="60"
        ).prompt()
    config=load_config()
    bm_self=BM(config)
    while True:
      response=bm_self.get_dynamic(config)
      if not response==None:
        if "saleStatus" in response.json()["data"]:
            sale_status=response.json()["data"]["saleStatus"]
            status=response.json()["data"]["status"]
            if "sale_status" and "status" in config["status"]:
                if not sale_status!=config["status"]["sale_status"] and status==config["status"]["status"]:
                    
                    pass #not push
            #push
            config["status"]["sale_status"]=sale_status
            config["status"]["status"]=status


        

    

