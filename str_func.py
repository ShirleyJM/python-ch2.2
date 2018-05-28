#대소문자 관련 메소드

s ="i like python "

print(s.upper())
print(s.lower())
print(s)
print(s.capitalize())
print(s.title())
print(s*3)


#검색 관련 메서드

s='I Like Python. I Like Java Also'
print(s.find("Like"))
print(s.find("Like",5))
print(s.find("JS"))
print(s.rfind("a"))

print(s.count("Like"))
#print(s.index("to"))

print("===============================")
print(s.index("Like"))
print(s.rfind("Like"))
print("================================")
print(s.startswith("i Like"))
print(s.startswith("Like",2))
print(s.endswith("Also"))
print(s.endswith("Java", 0, 26))
print(s.endswith("Java",0,25))  #Java

#분리와 결합 메소드

s="spam and ham"


s.split()
t= s.split()
print(t)
print(s)


t=s.split(" and ")
print(t)

s2= ":".join(t)
print(s2)
s3="one:two:three:four:five"
print(s3.split(":"))
print(s3.split(":", 2))
print(s3.rsplit(":", 2))

print("===============================")
lines = """ 1st line
            2nd line
            3rd line
            4th line
"""

print(lines.splitlines())
print(lines.splitlines("\n"))
print("===============================")
#판별 메소드
print('1234aa'.isdigit())
print("abcd".isalpha())

print("abcd".islower())
print("ABCD".isupper())
print("\n\n".isspace())
print("    ".isspace())
print("".isspace())


# 0으로 채우기
print("20".zfill(10))
print("12345".zfill(10))






