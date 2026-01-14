
print("kalkulator sederhana")

angka1 = float(input("masukan angka 1 ="))
operator = input("+,-,X,/ = " )
angka2= float(input("masukan angka 2 = "))

if operator == "+":
    hasil = angka1 +  angka2
    print("hasil nya adalah",hasil)
    
elif operator == "-":
    hasil = angka1 -  angka2
    print("hasil nya adalah",hasil)
    
elif operator == "X":
    hasil = angka1 *  angka2
    print("hasil nya adalah",hasil)
    
elif operator == "/":
    hasil = angka1 /  angka2
    print("hasil nya adalah",hasil)
    