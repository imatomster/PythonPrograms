list = [1,49,50,51,56,199,200,201,202,203,204,205,206]
for n in list:
    buses = n//50
    taxiPeople = n%50
    taxis = taxiPeople//5 + ((taxiPeople%5)+4)//5
    print(n, "people will need", buses, "buses and", taxis, "taxis")
