import calendar
from helper import helper
from color import textColor
#from colorama import Back
class myCalendar(object):
    """description of class"""
    year = None
    month = None
    day = None
    day_week = "Mo  Tu  We  Th  Fr" 
    day_weekend = "  St  Su"
    saturday = 5
    sunday = 6
    days = 10
    blank = 0
    line = "---------------------------"
    vertical_line = "|"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def displayCalendar(self):
       
        print(self.line)
        print(self.day_week, end=''),textColor.start_red(), print(self.day_weekend, end=''),textColor.stop_color(),print(self.vertical_line)
        print(self.line)
        
        calendar_now = calendar.monthcalendar(self.year, self.month)
        
        for i in range(len(calendar_now)):
             for j in range(len(calendar_now[i])):
               if j == self.saturday or j == self.sunday:
                    textColor.start_red()
               if helper.checkIfCurrentDay(self.year, self.month, calendar_now[i][j]):
                             textColor.start_green()
                             
               if calendar_now[i][j] < self.days:
                     if calendar_now[i][j] == self.blank:
                         print(' ' ,end=' '), textColor.stop_color(), print(self.vertical_line,end = ' ')
                     else:
                        print(calendar_now[i][j],end=' '),textColor.stop_color(), print(self.vertical_line,end = " ")
               else:
                     print(calendar_now[i][j],end=''), textColor.stop_color(), print(self.vertical_line,end = ' ')
               textColor.stop_color()
              
             print()  
        print(self.line)
      
