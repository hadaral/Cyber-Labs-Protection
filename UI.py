import psutil
import part2
import pro_obj
import Files_Handler
import monitor
import datetime
import time

choose_bet = raw_input("please enter 1 to monitor or 2 to ")
ch = False
while ch == False:
    if choose_bet == "1":
        monitor.monitor_func()
        ch = True

    elif choose_bet == "2":
        def start_monitor():
            observer = Files_Handler.Observer()
            observer.schedule(Files_Handler.MyHandler(), '.')
            observer.start()

        isValid = False
        while not isValid:
            date1 = raw_input("please enter the first date in format : yyyy-mm-dd hh:mm ")  # check the format
            try:  # strptime throws an exception if the input doesn't match the pattern
                datetime.datetime.strptime(date1, "%Y-%m-%d %H-%M")
                isValid = True
            except:
                print "Input doesn't match the pattern, try again!\n"
        isValid = False

        date1 = date1+":00"

        date2 = raw_input("please enter the second date in format : yyyy-mm-dd hh:mm")  #check the format
        date2 = date2+":00"
        if part2.two_dates(date1,date2) == 0 :
            print "both date doesn't exist or invalid format please try agaim\n"
        elif part2.two_dates(date1,date2) == -1 :
            print "the first date doesn't exist or invalid format please try again\n"
        elif part2.two_dates(date1,date2) == -2 :
            print "the second date doesn't exist or invalid format please try again\n"
        else:

            ch = True
    else:
        choose_bet = raw_input("*wrong choose*. please enter 1 to monitor or 2 to ")









