import colorama
from helper import *
import Calendar
colorama.init()

#get Date from keybord
selectedDate = helper.readDateFromKeyboard()
#display calendar
testCalendar = Calendar.Calendar(selectedDate[0], selectedDate[1], selectedDate[2])
testCalendar.displayCalendar()