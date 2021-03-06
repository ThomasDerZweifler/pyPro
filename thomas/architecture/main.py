import strings as s
import numbers as num

print(s.toString())

x = s.toString()

print("x[0] : " + x[0])

print("s.person['name'] : " + s.person["name"])

print("member: " + str(s.Person().x))

print("static member: " + str(s.Person.getSttaticX()))

s.Person.x = 9

h = s.Person()

# print("static member: " + str(h.getClsY()))

print("s.Person().name : " + s.Person().name)

print("s.Person('d').name : " + s.Person("d").name)

o = s.Person(surename = "my surename")

print("s.Person('surename='my surename).name : " + o.name)
print("s.Person('surename='my surename).surename : " + o.surename)

#print("s.Person().toString() : " + s.Person().toString())

#print("num.toString() : " + num.toString())

print( num.toString())

print("str(num.toString()[0]); str(num.toString()[1]) : " + str(num.toString()[0]) + "; " + str(num.toString()[1]))

print(num.n1 + num.n2)

s = {"a"}
s.add("Hello")
s.add("World!")
s.add("same")
s.add("same")

s1 = {"s1_a", "World", "a", "s1_d"}

print(s.intersection(s1))

print("difference: " + str(s.difference(s1)))

print("symmetric_difference: " + str(s.symmetric_difference(s1)))

print("isdisjoint: " + str(s.isdisjoint(s1)))