import os
import noneprompt,json

def is_load_config():
    if not os.path.exists("config.json"): return True
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

        
    
