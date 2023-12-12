print("Skvělý den!")
x = input("Abychom začali,zadejte proměnou x: ") #input = vstup(ptá se uživatele,co má do x vložit)
y = input("Teď zadejte proměnou y: ")

#přetypovává na integer(číslo)
x = int(x)
y = int(y)

print("Pro operátory musíte zadat jeden z daných znamének: ")
print(" Pro sčítání +")
print(" Pro odčítání -")
print(" Pro násobení *")
print(" Pro dělení /")
print(" Pro mocnění **, (x = mocněnec a y = mocnitel)")                             #komentáře (hashtagy) se dělají pravým altem a x
print(" A pro odmocnění /*, (x = odmocninec a y dmocnitel)")

znamenko = input("Zadejte vaší volbu operátoru: ")

#podmínky se dělají oříkazem if
if znamenko == "+":
  print(x+y)
  print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
elif znamenko == "-":
  print(x-y)
  print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
#pokud chci v podmínce pokračovat, nedávám if, ale elif
elif znamenko == "/":
  #jestliže chci dále něco kontrolovat, mohu podmínky vnořovat jako tady if
  if y == 0:
    print("TY KOKOS NÉÉÉÉÉ")
  else:
    print(x/y)
    print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
elif znamenko == "*":
  print(x*y)
  print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
elif znamenko == "**":
  print(x**y)
  print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
elif znamenko == "/*":
  if y < 0:
    print("AJ JÁ ŤA UŽ PACNU PO PAPULI")
  else:
    print(x**(1/y))
    print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
