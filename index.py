print("Skvělý den!")
x = input("Abychom začali,zadejte proměnou x: ")
y = input("Teď zadejte proměnou y: ")

x = int(x)
y = int(y)

print("Pro operátory musíte zadat jeden z daných znamének: ")
print(" Pro sčítání +")
print(" Pro odčítání -")
print(" Pro násobení *")
print(" Pro dělení /")
print(" Pro mocnění **, (x = mocněnec a y = mocnitel)")
print(" A pro odmocnění /*, (x = odmocninec a y dmocnitel)")

znamenko = input("Zadejte vaší volbu operátoru: ")

if znamenko == "+":
  print(x+y)
  print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
elif znamenko == "-":
  print(x-y)
  print("Du bist sehr tolle,Freund :D (to nebudu překládat)")
elif znamenko == "/":
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
