marks1=int(input("Enter marks 1: "))
marks2=int(input("Enter marks 2: "))
marks3=int(input("Enter marks 3: "))
# check for total percentage
total_percentage =(100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("you are passed;",total_percentage)
else:
    print("you failed,try again next year!",total_percentage)