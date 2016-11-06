import calendarGeneration
import calendar
from helper import helper
from color import textColor
from printer import printer
class Calendar(object):
    """description of class"""
    year = None
    month = None
    day = None
    day_week = "Mo  Tu  We  Th  Fr" 
    day_weekend = "  St  Su"
    saturday = 5
    sunday = 6
    one_digit_days = 10
    blank = 0
    line = "---------------------------"
    vertical_line = "|"
    space = ' '
    empty = ''
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

  
    def displayCalendar(self):
        printer.printDayName(self)   
       
       # calendar_now = calendar.monthcalendar(self.year, self.month)
        calendar_now = calendarGeneration.calendarGeneration.generation(self.year,self.month)     
        for i in range(len(calendar_now)):
             for j in range(len(calendar_now[i])):
               if j == self.saturday or j == self.sunday:
                    textColor.start_red()
               if helper.checkIfCurrentDay(self.year, self.month, calendar_now[i][j]):
                             textColor.start_green()
               if calendar_now[i][j] < self.one_digit_days:
                     if calendar_now[i][j] == self.blank:
                        printer.printCell(self, self.space, self.space)
                     else:
                        printer.printCell(self, calendar_now[i][j],self.space)
               else:
                     printer.printCell(self, calendar_now[i][j],self.empty)
               textColor.stop_color()
             print()  
        print(self.line)
      
