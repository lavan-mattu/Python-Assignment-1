name=input("Name  ")
cls=input("Class  ")
sec=input("Section  ")
e=int(input("English  "))
h=int(input("Hindi  "))
p=int(input("Punjabi  "))
s=int(input("SST  "))
c=int(input("Computers"))
totalMarks=e+h+p+s+c
avg=totalMarks/5

if avg>=60 and avg<80:
    grade="Good"
    print("Name        ", name)
    print("Class       ", cls)
    print("Section     ", sec)
    print("Total       ", totalMarks)
    print("Average     ", avg)
    print("Grade       ", grade)
elif avg>=90:
    grade="Outstanding"
    print("Name        ", name)
    print("Class       ", cls)
    print("Section     ", sec)
    print("Total       ", totalMarks)
    print("Average     ", avg)
    print("Grade       ", grade)
elif avg>=80 and avg<90:
    grade="Very Good"
    print("Name        ", name)
    print("Class       ", cls)
    print("Section     ", sec)
    print("Total       ", totalMarks)
    print("Average     ", avg)
    print("Grade       ", grade)
elif avg<60 and avg>=50:
    grade="Fair"
    print("Name        ", name)
    print("Class       ", cls)
    print("Section     ", sec)
    print("Total       ", totalMarks)
    print("Average     ", avg)
    print("Grade       ", grade)
elif avg<50:
    grade="Participation"
    print("Name        ", name)
    print("Class       ", cls)
    print("Section     ", sec)
    print("Total       ", totalMarks)
    print("Average     ", avg)
    print("Grade       ", grade)
