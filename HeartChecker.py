#Patient Information:

print("Please enter patient name:" )
a=input("")
print("Hello", a, )
(int(input("Please enter your age:")))

#Enter patient's different reading taken from external measurement devices:

T=int(input("Please enter your Body Temperature in Fahrenheit:"))
H= int(input("Please enter your Heart Rate:"))
O= int(input("Please enter your Oxygen Level in %:"))
print("Please enter your Blood Pressure:")
BP= int(input("SYSTOLIC:"))
bpd=BP= int(input("DIASTOLIC:"))
S=int(input("Please enter your Sweat Glands Activity from given option-> 1-Normal/2-Low/3-Excess: "))

#Algorithms:

if S==2:
    if T>97 and T<104:
        print("you are suffering from ANHIDROSIS")
    else:
        print("Your Heart is Healthy")
if S==3:
    if T>97 and T<104:
        print("you are suffering from HYPERHIDROSIS")
    else:
        print("Your Heart is Healthy")


elif T>104:
    print("you are suffering from HYPERTHERMIA")
elif H>100:
    print("you are suffering from TACHYCARDIA")
elif T<92:
    print("you are suffering from SEPSIS")
elif O<95:
    print("you are suffering from HYPOEXIMIA")
elif H<40:
    print("you are suffering from BRADYCARDIA")
else:
    print("Your Heart is Healthy")



