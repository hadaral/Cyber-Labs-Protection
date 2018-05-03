

def two_dates(list_one, list_two, date1, date2):

    file_ = open("processList.txt","r")
    file = file_.readlines()
    file_.close()
    #list_one = []
    #list_two = []
    for i in range(len(file)):
        if file[i] != "\n":
            file[i].replace("\n","")
            string = file[i].split(",")
            date = string[1].replace("\n","")
            date.replace("\n","")
            if str(date)==str(date1) and string[0]not in list_one:
                list_one.append(string[0])
            elif str(date)==str(date2) and string[0] not in list_two:
                list_two.append(string[0])
    if not list_one and not list_two:
        return 0
    elif not list_one and list_two:
            return -1
    elif not list_two and list_one:
        return -2


def printing(list_one, list_two):
        for l in range(len(list_one)):
            if list_one[l] not in list_two:
                print list_one[l] , " got finished "


        for k in range(len(list_two)):
            if list_two[k] not in list_one:
                print list_two[k] , " got created "
