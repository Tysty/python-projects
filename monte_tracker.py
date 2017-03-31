#do dolars and quarters for this program
debug = False
m = input("how much money do you want? ")
money = int ( m )
do = int (money / 100)
if debug == True:
    print("do: " + str(do))
mr = money % 100
print("mr: " + str(mr))
q = int(mr / 25)
print("q: " + str(q))
mr = mr % 25
print("mr: " + str(mr))
d = int ( mr / 10 )
print(d)
mr = mr % 10
print(mr)
n = int(mr / 5)
print(n)
mr = mr % 5
print(mr)
p = int(mr / 1)
print(p)
mr = mr % 1
print(money)
#do the nickels and dimes for homework
if p > 1:
    str_p = " pennys. "

else:
    str_p = " penny. "
if n > 1:
    str_n = " nickels, and "
else:
    str_n = " nickel, and "
if d > 1:
    str_d = " dimes, "

else:
    str_d = " dime, "
if q > 1:
    str_q = " quarters, "

else:
    str_q = " quarter, "
if do > 1:
    str_do = " dollars, "

else:
    str_do = " dollar, "
print("you have " + str(do) + str_do + str(q) + str_q + str(d) + str_d + str(n) + str_n + str(p) + str_p)
