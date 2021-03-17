def konversiSuhu (C="", F=""):
    if F == "":
        C1 = float(C*9/5)+32
        return C1        
    elif C == "":
        F1 = float(F-32)*5/9
        return F1
        
print ("h = how to show available option")
print ("1 = convertion from farenheit to celcius (F=...)")
print ("2 = convertion from celcius to farenheit (C=...)")
print ("k = exit\n")

a = 0
while a != "k":
    a = (input("Your option: "))
    if a=="1":
        c = float(input("Enter number for convertion: "))
        print(c, "Celcius =", konversiSuhu(C=c), " Fahrenheit")
        print("-------------------------------\n")
    elif a=="2":
        c = float(input("Enter number for convertion: "))
        print(c, "Fahrenheit =", konversiSuhu(F=c), " Celcius")
        print("-------------------------------\n")
else :
    p=input("Are you sure? Yes(y)/No(n) : ")
    if p=="y":
        print("exit")
    elif p=="n":
        print("You have to begin from the first!")
