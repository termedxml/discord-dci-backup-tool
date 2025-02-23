from main import colours

class prnt():
    def __init__(self) -> None:
        pass
    
    def success(self, content, end="\n", indent=0):
        ind = ""
        for _ in range(indent): ind += " "
        print(f"{ind}{colours['green']}>{colours['white']} {content}", end=end)
    
    def info(self, content, end="\n", indent=0):
        ind = ""
        for _ in range(indent): ind += " "
        print(f"{ind}{colours['white']}> {content}", end=end)
    
    def fail(self, content, end="\n", indent=0):
        ind = ""
        for _ in range(indent): ind += " "
        print(f"{ind}{colours['light_red']}>{colours['white']} {content}", end=end)
    
    def inp(self, content, end="\n", indent=0):
        ind = ""
        for _ in range(indent): ind += " "
        print(f"{ind}{colours['light_blue']}>{colours['white']} {content}", end=end)
    
    def warn(self, content, end="\n", indent=0):
        ind = ""
        for _ in range(indent): ind += " "
        print(f"{ind}{colours['yellow']}>{colours['white']} {content}", end=end)