

def two_dates(date_first, date_last):

    file_ = open("processList.txt","r")
    file = file_.readlines()
    file_.close()
    date1 = date_first
    date2 = date_last
    list_one = []
    list_two = []
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
        for k in range(len(list_two)):
            print list_two[k] , " at " , date_last
        return -1
    elif not list_two and list_one:
        for l in range(len(list_one)):
            print list_one[l] , " at " , date_first , "  *****" , l
        return -2
    else:
        for l in range(len(list_one)):
            if list_one[l] not in list_two:
                print list_one[l] , " at " , date_first , "  *****" , l

        for k in range(len(list_two)):
            if list_two[k] not in list_one:
                print list_two[k] , " at " , date_last


def printing(list_one, list_two,date_first, date_last):
        for l in range(len(list_one)):
            if list_one[l] not in list_two:
                print list_one[l] , " at " , date_first , "  *****" , l

        for k in range(len(list_two)):
            if list_two[k] not in list_one:
                print list_two[k] , " at " , date_last
