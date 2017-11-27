from datetime import date

now=date.today()
s=now.strftime("%m-%d-%y. %d %B %Y is a %A on the %d day of %B.")

birthday=date(1996,8,15)
age=now-birthday
print(age.days/365,'岁')
print(now)
print(s)