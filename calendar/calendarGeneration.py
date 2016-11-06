
from itertools import zip_longest
class calendarGeneration(object):
   
      def monthIndex(month):
          year_month = [6,2,2,5,0,3,5,1,4,6,2,4]
          month_index = year_month[month - 1]
          return month_index

      def centuryIndex(year):
          IXst1 = 1900
          IXst2 = 1999
          if year >= IXst1 and year <= IXst2:
              century_index = 1
              return century_index
          else :
              century_index = 0
              return century_index
     
      def yearIndex(year):
          month_of_year = 12
          statiл_number = 4
          piece_of_number = calendarGeneration.seperayteNumber(year)
          first_term = int(piece_of_number) / month_of_year       # float
          second_term = int(piece_of_number) % month_of_year      
          third_term = int(second_term) / statiл_number             #float
          year_index = int(first_term) + second_term + int(third_term)
          return year_index
     
      def leapYearIndex(year, month):
          intercalary = 4
          piece_of_number = calendarGeneration.seperayteNumber(year)
          if month == 1 or month == 2 :
              if int(piece_of_number) % intercalary == 0:
                  leap_year_index = 1
              else:
                 leap_year_index = 0
          else:
              leap_year_index = 0
          return leap_year_index

      def seperayteNumber(year):
          year_array = []
          last_two_number = []
          piece_of_number = ''

          for i in str(year):
              year_array.append(i)
          len_year = len(year_array)
          
          if len_year < 2:
               last_two_number.append(year_array[len_year - 1])
          else:  
                last_two_number.append(year_array[len_year - 2])
                last_two_number.append(year_array[len_year - 1])
          
          for i in last_two_number:
                piece_of_number = piece_of_number + (i)
          return piece_of_number

      def group(iterable, count):
            return [iterable[i:i + count] for i in range(0, len(iterable), count)]

      
      def generation(year,month):
          month_array = []                                 
          month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
          day = 1
          empty_zero = 0
          specific_month = 0
          february = 2
          leap_february = 29
          less_week = 7 
          day_five_weeks = 35
          day_six_weeks = 42
          year_index = calendarGeneration.yearIndex(year)
          month_index = calendarGeneration.monthIndex(month)
          century_index = calendarGeneration.centuryIndex(year)
          leap_year_index = calendarGeneration.leapYearIndex(year, month)
          weekday = (year_index + month_index + century_index + day - leap_year_index) % 7 #determine the day of the month which begins
          i = 0
          if month == february:
              piece_of_number = calendarGeneration.seperayteNumber(year)
              if int(piece_of_number) % 4 == 0:  # Determines whether a leap year
                  month_day[1] = leap_february
          if weekday == 0:
              weekday = less_week
          while i <= less_week:
            if i < weekday - 1:
                 month_array.append(empty_zero)  # zero on the start array
                 i +=1
            else:
                 break
          specific_month = month_day[month - 1]
          i = 1
          while i <= specific_month:
              month_array.append(i)
              i+=1
          i = len(month_array)
          if i<=35:
              while i <= day_five_weeks:
                  month_array.append(empty_zero)
                  i+=1
          else:
              while i <day_six_weeks:
                  month_array.append(empty_zero)
                  i+=1
          calendar_now = calendarGeneration.group(month_array, less_week)  #division on the block list  (7)
          return calendar_now
          
      