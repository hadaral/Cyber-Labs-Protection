import psutil
import time
import Files_Handler
from datetime import datetime
import os
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import pro_obj



def monitor_func():
    __last_modified1 = None
    __last_modified2 = None

    name_file_1 = "processList.txt"
    name_file_2 = "Status_Log.txt"
    X = input("enter the time that you want the monitor to scan the process: ")
    observer = Files_Handler.Observer()
    observer.schedule(Files_Handler.MyHandler(), '.')
    observer.start()
    list_process = []
    while 1:
        if os.path.isfile(name_file_1):
            if __last_modified1 != os.stat(name_file_1).st_mtime:
                print("worrning!! the file processList.txt was change outside the program")
            os.chmod(name_file_1, S_IWUSR | S_IREAD)
        file = open(name_file_1, "a")
        for p in psutil.process_iter():
            proce = pro_obj.pro(p.name(),str(p.pid))
            file.write(proce.to_string())
            file.write(","+str(datetime.now().replace(second=0, microsecond=0))+"\n")
            list_process.append(proce.to_string())
        file.write("\n")
        file.close()
        os.chmod(name_file_1, S_IREAD | S_IRGRP | S_IROTH)  # readonly
        __last_modified1 = os.stat(name_file_1).st_mtime

        if os.path.isfile(name_file_2):
            if __last_modified2 != os.stat(name_file_2).st_mtime:
                print("worrning!! the file Status_Log.txt was change outside the program")
            os.chmod(name_file_2, S_IWUSR | S_IREAD)
        log_new = open(name_file_2, "a")
        list_now = []
        for p in psutil.process_iter():
            proce = pro_obj.pro(p.name(), str(p.pid))
            list_now.append(proce.to_string())
            if(proce.to_string() not in list_process):
                log_new.write(proce.to_string())
                log_new.write("\t,"+str(datetime.now().replace(second=0, microsecond=0))+"\n")
                print proce.to_string() , "got change at ", str(datetime.now())

        for l in range(len(list_process)):
            if list_process[l] not in list_now :
                log_new.write(list_process[l])
                log_new.write("\t," + str(datetime.now().replace(second=0, microsecond=0)))
                log_new.write("\n")
                print list_process[l] , " got changed at ", str(datetime.now().replace(second=0, microsecond=0))
        list_process = list_now
        log_new.close()
        os.chmod(name_file_2, S_IREAD | S_IRGRP | S_IROTH)  # readonly
        __last_modified2 = os.stat(name_file_2).st_mtime

        time.sleep( X)

class pro:
    def __init__(self, name,pid):
        self.name = name
        self.pid = pid

    def to_string(self):
        return "pid: "+ self.pid + "\tname: " + self.name;


__last_modified1 = None
__last_modified2 = None

def start_monitor():
    observer = Files_Handler.Observer()
    observer.schedule(Files_Handler.MyHandler(), '.')
    observer.start()


X = input("enter the time that you want the monitor to scan the process: ")
observer = Files_Handler.Observer()
observer.schedule(Files_Handler.MyHandler(), '.')
observer.start()
list_process = []
while 1:
    if os.path.isfile('processList.txt'):
        if __last_modified1 != os.stat('processList.txt').st_mtime:
            print("worrning!! the file processList.txt was change outside the program")
        os.chmod('processList.txt', S_IWUSR | S_IREAD)
    file = open("processList.txt", "a")
    file.write(str(datetime.now()))
    file.write("\n")
    for p in psutil.process_iter():
        proce = pro(p.name(),str(p.pid))
        file.write(proce.to_string())
        file.write("\n")
        list_process.append(proce.to_string())
    file.write("\n")
    file.close()
    os.chmod('processList.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
    __last_modified1 = os.stat('processList.txt').st_mtime


    if os.path.isfile('Status_Log.txt'):
        if __last_modified2 != os.stat('Status_Log.txt').st_mtime:
            print("worrning!! the file Status_Log.txt was change outside the program")
        os.chmod('Status_Log.txt', S_IWUSR | S_IREAD)
    log_new = open("Status_Log.txt", "a")
    #the_file = open("processList","r+")
    #w1 = the_file.read()
    list_now = []
    for p in psutil.process_iter():
        proce = pro(p.name(), str(p.pid))
        list_now.append(proce.to_string())
        if(proce.to_string() not in list_process):
            log_new.write(proce.to_string())
            log_new.write("\t"+str(datetime.now()))
            log_new.write("\n")
            print proce.to_string() , "got change at ", str(datetime.now())

    for l in range(len(list_process)):
        if list_process[l] not in list_now :
            log_new.write(list_process[l])
            log_new.write("\t"+str(datetime.now()))
            log_new.write("\n")
            print list_process[l] , " got changed at ", str(datetime.now())
    list_process = list_now
    log_new.close()
    os.chmod('Status_Log.txt', S_IREAD | S_IRGRP | S_IROTH)  # readonly
    __last_modified2 = os.stat('Status_Log.txt').st_mtime

    time.sleep( X)

