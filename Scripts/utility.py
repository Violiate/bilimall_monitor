import os
import noneprompt,json
from loguru import logger
import pyperclip

def is_load_config():
    if not os.path.exists("config.json"): return False
    reload=noneprompt.ListPrompt(
        question="是否加载上次的配置？",
        choice=[
           noneprompt.Choice(name=x)
            for x in[ "是","否"]
        ],
        default="是"
    ).prompt().name
    if reload=="是":  return True
    return False

def load_config():
    if not os.path.exists("config.json"): return None
    with open("config.json") as f:
        return json.load(f)
    
def push_choice():
    push_config={}
    push_choice=noneprompt.CheckboxPrompt(
                    question="请选择要开启的推送方式，空格为选择，可选择多个",
                    choices=[
                        noneprompt.Choice(
                            x)
                            for x in["bark推送","钉钉机器人推送","企业微信推送","pushplus推送","server酱推送","smtp邮件推送"] 
                     
                    ],
        ).prompt()
    for choice in push_choice:
        if choice.name=="bark推送":
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            bark_token=noneprompt.InputPrompt("请输入bark推送的token：",default_text=clip_value).prompt()
            push_config["bark_token"]=bark_token
        elif choice.name=="钉钉机器人推送":
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            dingding_token=noneprompt.InputPrompt("请输入钉钉机器人推送的token：",default_text=clip_value).prompt()
            push_config["dingding_token"]=dingding_token
        elif choice.name=="企业微信推送":
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            wx_token=noneprompt.InputPrompt("请输入企业微信推送的token：",default_text=clip_value).prompt()
            push_config["wx_token"]=wx_token
        elif choice.name=="pushplus推送":
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            pushplus_token=noneprompt.InputPrompt("请输入pushplus推送的token：",default_text=clip_value).prompt()
            push_config["pushplus_token"]=pushplus_token
        elif choice.name=="server酱推送":
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            ftqq_token=noneprompt.InputPrompt("请输入server酱推送的token：",default_text=clip_value).prompt()
            push_config["ftqq_token"]=ftqq_token
        elif choice.name=="smtp邮件推送":
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            smtp_mail_host=noneprompt.InputPrompt("请输入smtp邮件推送的host：",default_text=clip_value).prompt()
            push_config["smtp_mail_host"]=smtp_mail_host
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            smtp_mail_user=noneprompt.InputPrompt("请输入smtp邮件推送的用户名：",default_text=clip_value).prompt()
            push_config["smtp_mail_user"]=smtp_mail_user
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            smtp_mail_pass=noneprompt.InputPrompt("请输入smtp邮件推送的密码：",default_text=clip_value).prompt()
            push_config["smtp_mail_pass"]=smtp_mail_pass
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            smtp_sender=noneprompt.InputPrompt("请输入smtp邮件推送的发件人：",default_text=clip_value).prompt()
            push_config["smtp_sender"]=smtp_sender
            try:
                clip_value = pyperclip.paste()
                logger.info("剪贴板复制成功")
            except pyperclip.PyperclipException:
                clip_value = ""
            smtp_receivers=noneprompt.InputPrompt("请输入smtp邮件推送的收件人，多个以英文逗号隔开：",default_text=clip_value).prompt()
            push_config["smtp_receivers"]=smtp_receivers
    return push_config()
            
    


        
    
