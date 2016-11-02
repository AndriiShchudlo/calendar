import calendar
import time
import datetime
import colorama
import myCalendar
from helper import *
colorama.init()

#get Date from keybord
selectedDate = helper.readDateFromKeyboard()
#display calendar
testCalendar = myCalendar.myCalendar(selectedDate[0], selectedDate[1], selectedDate[2])
testCalendar.displayCalendar()