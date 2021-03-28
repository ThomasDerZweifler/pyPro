# %%
print("start")

y = 1
x = 0
while y < 10 :

    while x < 10 :

        # Berechnung nach continue erzeugt innere Endlosschleife !
        x = x + 1

        # skip all even x
        if x % 2 == 0 : continue 

        # skip from x = 3
        if x == 3 : break

        print("innere Schleife x = {0}, y = {1}".format(x,y))
    
    print("äußere Schleife")
    x = 0
    y = y + 1

print("end")

for i in range(1,10,2):
    pass
    # print(i)
# %%
