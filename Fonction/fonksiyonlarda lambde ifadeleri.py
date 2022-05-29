ikiyleçarp= lambda x : x*2#burada def fonksiyonu yazmaya gerek kalmadı...
print(ikiyleçarp(3))
total = lambda x,y,z : x+y+z#def fonksiyonu yazmadan list compherension gibi lambda değeri yazılarak tanımlanabilir
print(total(3,5,13))
tersçevirme = lambda x : x[::-1]
print(tersçevirme("Python"))
print(tersçevirme("Tolgahan"))