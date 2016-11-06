from color import textColor

class printer(object):
    """description of class"""
    
    def __init__(self):
        pass
    def printCell(self,day,space):
        print(day, end = space), textColor.stop_color(), print(self.vertical_line,end = self.space)

    def printDayName(self):
        
        print(self.line)
        print(self.day_week, end = self.empty),textColor.start_red(), print(self.day_weekend, end=''),textColor.stop_color(),print(self.vertical_line)
        print(self.line)
