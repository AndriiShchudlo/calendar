import sys

class textColor:
    
    def write(msg):
        sys.stdout.write(msg)
        sys.stdout.flush()
    #*** R E D ***
    def start_red():
        textColor.write('\x1b[31m')
    #** G R E E N **
    def start_green():
       textColor.write('\x1b[32m')

    def stop_color():
        textColor.write('\x1b[0m')