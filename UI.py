import psutil
import part2
import pro_obj
import Files_Handler
import monitor
import datetime
import time

choose_bet = raw_input("please enter 1 to monitor or 2 to see differences between two dates ")
ch = False
while ch == False:
    if choose_bet == "1":
        monitor.monitor_func()
        ch = True

    elif choose_bet == "2":
        observer = Files_Handler.Observer()
        observer.schedule(Files_Handler.MyHandler(), '.')
        observer.start()

        isValid = False
        while not isValid:
            date1 = raw_input("please enter the first date in format : yyyy-mm-dd hh:mm ")  # check the format
            try:  # strptime throws an exception if the input doesn't match the pattern
                datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M")
                isValid = True
            except:
                print "Input doesn't match the pattern, try again!\n"
        isValid = False
        date1 = date1+":00"

        while not isValid:
            date2 = raw_input("please enter the second date in format : yyyy-mm-dd hh:mm")  #check the format
            try:  # strptime throws an exception if the input doesn't match the pattern
                datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M")
                isValid = True
            except:
                print "Input doesn't match the pattern, try again!\n"
        #isValid = False
        date2 = date2+":00"
        if date1 > date2 :
            ch = False
            print "last date earlyer then the first. try again."
            continue
        if date1 == date2:
            ch = False
            print "same date. try again."
            continue
        list_one = []
        list_two = []
        if part2.two_dates(list_one,list_two,date1,date2) == -1:
            print "first date doesn'n exist please try again."
        elif part2.two_dates(list_one,list_two,date1,date2) == -2:
            print "last date doesn'n exist please try again."
        elif part2.two_dates(list_one,list_two,date1,date2) == 0:
            print "both dates doesn'n exist please try again."
        else:
            part2.printing(list_one,list_two)
            ch = True

    else:
        choose_bet = raw_input("*wrong choose*. please enter 1 to monitor or 2 to see differences between two dates ")









