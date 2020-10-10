Print "Pythonapp-v1.2"
name=raw_input("enter ur name: ")
gender=raw_input("are u F/M: ")
status=raw_input("married/unmarried: ")
if gender=="F" or "f" or "female" or "Female" or "FEMALE":
    if status=="unmarried" or "Unmarried" or "UNMARRIED":
        print "Miss.",name
    else:
        print "Mrs,",name
else:
    print "Mr.",name
