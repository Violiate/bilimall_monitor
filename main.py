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
    config={}
    config["headers"]=headers
    sale_status_translate={
        
        "11":"可销售",
        "14":"有人下单，未付款",
        "13":"已售罄"
    }
    if not is_load_config():
        
        config["item_id"]=noneprompt.InputPrompt(
            question="请输入商品id"
        ).prompt()
        config["sleep"]=noneprompt.InputPrompt(
            question="请输入每轮检测间隔时间(秒)，过快可能会触发风控",
            default_text="60"
        ).prompt()
        config["status"]={
            "sale_status":"0",
            "status":"0"
        }
        push_config=push_choice()
        
    else:
        config=load_config()
    bm_self=BM(config)
    while True:
      response=bm_self.get_dynamic()
      if not response==None:
        if "saleStatus" in response.json()["data"]:
            sale_status=response.json()["data"]["saleStatus"]
            status=response.json()["data"]["status"]
            
            if sale_status!=config["status"]["sale_status"] or status!=config["status"]["status"]:
                    config["status"]["sale_status"]=sale_status
                    sale_status_name=sale_status
                    config["status"]["status"]=status
                    config["goods_name"]=response.json()["data"]["name"]
                    if sale_status in sale_status_translate:
                        sale_status_name=sale_status_translate[sale_status]
                    
                    logger.success("商品 "+config["goods_name"]+" 状态发生变化 "+str(sale_status_name))
                    bm_self.save_config(config)
                    #push
                    pass 
        time.sleep(int(config["sleep"]))
                
                


        

    

