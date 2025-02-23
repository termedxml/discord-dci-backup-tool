import yaml

class Config():
    "Ex: `config.threads`"
    def __init__(self) -> None:
        data = yaml.safe_load(open("config.yml"))
        
        self.colour = data['colour']
        self.group_chat_msg = data['group_chat_msg']