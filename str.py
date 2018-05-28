s=''
str1 ="hello world"
str2="안녕 세상"

print(str1)
print(str2)
print(type(s),type(str1),type(str2),sep=", ")
print(isinstance(str1, str))

print("hello")
print("world")
print("hello\nworld")


str3="""ab fdsa da

fdsaasdfasdfaf
fdsadfjklhkljhk"""

str4="I'm a boy"

print(str3)
print(str4)


print('Hello world I\'d say "hello world"')
print("Hello world I'd say \"hello world\"")
print("Hello\rWorld")
print("Hello\bWorld")


print("=====================================================")

str1 = "FirstString"
str2 = "SecondString"

print(str1+str2)


#print("제 나이는"+ 25+"살 입니다.")


print(str1[5])
print(str1[-6])
print(str1[2:5])
#2번째부터 끝까지
print(str1[2:])
print(str1[:5])  #print()

print(str1[1:5])
print(str1[5:])


print(str1[:])

print(str1[-6:-2])

print(str1[-6:])
print(str1[:-6])

print(str1[0:8:2])
print(str1[0:8:3])

print("=====================================================")

do=38

str1 = "현재 온도는 %d도 입니다." %do
print(str1)

str2="오늘은 %d년 %s월 %d일 입니다." %(2018,"오월",15)
print(str2)

age=26
print("제 나이는 %10d살 입니다." %age)


age=123456789012
print("제 나이는 %10d살 입니다."%age)


area=76.483
print("원의 넓이는 %10.3f입니다." %area)
print("원의 넓이는 %10.1f입니다." %area)
print("원의 넓이는 %-10.3f입니다." %area)



#print("수수료는 %d입니다." %20)

print("=============================")
print("=============================")
print("=============================")

age=35
print("제 나이는 {0}살 입니다.".format(35))
print("제 나이는 {0}살 입니다.".format("서른 다섯"))

print("오늘은 {0}년 {1}월 {2}일 입니다.".format("2018","05",17))
print("오늘은 {year}년 {month}월 {day}일 입니다.".format(year="2018", month=5, day=17))
print("오늘은 {month}월 {day}일 {year}년 입니다.".format(year="2018", month=5, day=17))

print("오늘은 {0:10}년 {1:10}월 {2:10}일 입니다.").format("2018",5,17)



