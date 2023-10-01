# Q1
print("Please enter your name,age,street,city and country")
name= 'lama'
age=19
street=159
city='Gaza'
country='Palestine'
Address=city+" "+country
print(f"\"name: " , name,"\"",f"\n\"age: ",age,"\"",f"\n\"Address : ",street ,Address,"\"")
print("\"Hello {%s} Your age is %d Years Old, Your Address is %d, %s\"" %(name,(age-5),street,Address))
print(type(name))
print(type(age))
print(type(city))
print(type(street))
print(type(country))
print(type(Address))
print("\"Hello {%s},How Are You ? \\ \" \" \" Your Age Is \"%d\" \" +And Your country Is : %s "%(name,(age-5),country))
print("\"Hello {%s},How Are You ? \\ \n \" \" \" Your Age Is \"%d\" \" +And \nYour country Is : %s "%(name,(age-5),country))






#Q7
name='ITF Gsg Python'
f1=name[0]
f3=name[2]
f=name[-1]
print(f" First letter is \"",f1,"\"",f" \nThird letter is \"",f3,"\"",f"\n Last letter is \"",f,"\"")
#Q8
print(name[11:14])
print(name[:4])
print(name[:7:2])
print(name[:-7:-1])
#Q9
name="$&$Mohammed$&$"

#name.strip("&")
print(name.strip('$').strip('&').strip('$'))
#Q10
msg="I %7 Python And Although I %7 GSG With Zakaria"
print(msg.replace("%7","Love"))
print(msg.replace("%7","Love",1))


#Q11
num1="4"
num2="56"
num3="963"
num4="385"
num5="8719"
num6="87190"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
print(num6.zfill(4))

#The difference between (title) and (capitalize):
#Ex":"
name1='lama jamal eleiwa'
print(name1.capitalize())
print(name1.title())
#Q14
first_name="Dana"
print("***********" + first_name)
print("***********" + first_name + "***********")
print(first_name + "***********")
name_one="saMER"
name_two="Abed"
name1=name_one[0].lower()+name_one[1:].upper()
name2=name_two[0].lower()+name_two[1:].upper()
print(name1)
print(name2)
print(name_one.lower())
print(name_two.upper())
#Q16 we can use islower and isupper to check it and we can use it in if else statement









