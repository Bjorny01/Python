import datetime
from Zoo.Zoo_class import Djur

def load_file(): #Laddar in djurfilen och returnerar en lista med alla djur och deras egenskaper
    fil = open("Zoo.txt", "r").read().splitlines()
    fil = [x.split(",") for x in fil]

    djur_list = []
    i = 0
    for x in fil:
        djur_list.append(Djur(fil[i][0], fil[i][1], fil[i][2], fil[i][3], fil[i][4]))
        i += 1

    return djur_list

def check_date(): #Kollar datum, returnerar månaden för besöket
    answear = input("Skriv in vilket datum du vill komma i format yyyy/mm/dd:")
    today = datetime.date.today()
    try: #Kollar format
        year, month, day = answear.split('/')
        try: #Kollar siffror
            datetime.date(int(year), int(month), int(day))
            if datetime.date(int(year), int(month), int(day)) < today: #Kollar att datum inte passerat
                print("Du har angivit ett datum som redan passerat")
                return check_date()
            if int(month) == 12 and int(day) == 25: #Kollar att inte julafton
                print("Zooet har inte öppet på julafton")
                return check_date()
            else:
                print("Zooet har öppet mellan 08 - 23")
                return month
        except ValueError:
            print("Du har angivit datumet i fel format")
            return check_date()
    except:
        print("Du har angivit datumet i fel format")
        return check_date()

def check_time(): #Kollar tiden, returnerar tiden ankomst/avfärd
    answear_time = input("Mellan vilka tider vill du besöka zooet? (t.ex. 15 - 16)")
    try: #Kollar format
        arrival_time,exit_time = answear_time.split("-")
        if int(arrival_time) >= int(exit_time): #Kollar format
            print("Ankomsttid måste vara före avfärdstid")
            return check_time()
        if int(arrival_time) < 8: #Kollar öppettider
            print("Tiden du vill komma funkar inte, zooet öppnar först klckan 8")
            return check_time()
        if int(exit_time) > 23: #Kollar stängningstider
            print("Tidem du vill åka funkar inte, zooet stänger klockan 20")
            return check_time()
        else:
            return arrival_time,exit_time
    except ValueError:
        print("du måste ange tiden i format med helt klockslag (t.ex. 15 - 16)")
        return check_time()

def creat_season(): #Använder månad för att avgöra om sommar/vinter
    month = check_date()
    season = "vinter"
    if int(month) > 8 or int(month) < 3:
        season = "sommar"
    return season

def main(): #printar ut listan, kollar förutsättningarna
    djur_list = load_file()
    season = creat_season()
    arrival_time, exit_time = check_time()
    for djur in djur_list: #Print djur listan
        if str(season) == str(djur.ide) or str(djur.ide) == "-":
            print(djur.namn, "vaken:",djur.vaknar,"-", djur.somnar,end="")
            if int(djur.matningstid) >= int(arrival_time) and int(djur.matningstid) <= int(exit_time):
                print("        Matningstid: ***",djur.matningstid,"***",'\t')
            else:
                print('\t')

print("WÄLKOMMEN TILL VÅRAT ZOO")
main()









