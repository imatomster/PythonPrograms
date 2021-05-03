years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
for y in years:
    a = y%19
    b = y//100
    c = y%100
    d = b//4
    e = b%4
    g = (8*b + 13)//25
    h = (19*a+b-d-g+15)%30
    j = c//4
    k = c%4
    m = (a+11*h)//319
    r = (2*e+2*j-k-h+m+32)%7
    n = (h-m+r+90)//25
    p = (h-m+r+n+19)%32
    print("Easter falls on", n, end="")
    print("/", end="")
    print(p, "in", y)

