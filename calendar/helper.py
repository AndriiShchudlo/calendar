import datetime

class helper(object):
    """description of class"""
    def __init__(self):
        pass
  
    def readDateFromKeyboard():
        lenght_date = 1
        lenght_date1 = 2
        month_of_year = 12
        emty_elementt = ''
        while 1:
               try:
                     inputDate = input("Please, input date (YYYY-MM or just MM  ) or press Enter (will be use current month): ") 
                     temp = inputDate
                     if inputDate == "":
                        return helper.getCurrentDate() 
                     else :  
                         temp = temp.split("-")
                         if len(temp)> lenght_date1:
                             continue
                         if len(temp) == lenght_date:
                             if int(temp[0])>month_of_year or int( temp[0])<lenght_date:
                                 continue
                         if len(temp)==lenght_date1:
                             if int(temp[1])>month_of_year or int(temp[1])<lenght_date or int(temp[0]) == emty_elementt:
                                continue
                     #return temp     
                     break    
               except ValueError:
                     pass
        if temp == '':
                return helper.getCurrentDate()
            # if user input only one number then means the month
        if len(temp) == 1 :
                return datetime.datetime.today().year, int(temp[0]), datetime.datetime.today().day
        elif len(temp) == 2 : # user input year and month
                return int(temp[0]), int(temp[1]), datetime.datetime.today().day
           
    def getCurrentDate() :
         return datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day       
     
    def checkIfCurrentDay(year, month, date):
        currentDate = helper.getCurrentDate()
        if(currentDate[0] == year and currentDate[1] == month and currentDate[2] == date) : 
            return True
        return False


