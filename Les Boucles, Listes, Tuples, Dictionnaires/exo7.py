import datetime
year=datetime.date.today().year
list_year=[]

for i in range(1980, year+1):
    list_year.append(i)

print(list_year)