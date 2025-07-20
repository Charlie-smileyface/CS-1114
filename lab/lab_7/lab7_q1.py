## Q1
#1.
name="Grace Hopper"
name[name.find('r')]
name[len(name)-1]
name[:5]

#2.
name = 'alan turing'
name1 = name[:4]
name.capitalize()
name2 = name[5:]
name2.capitalize()

#3.
s = 'Computer Science'
name1 = s[:s.find(' ')]
name2 = s[s.find('S'):]
print(name1)
print(name2)
print(name1[::2] + ' ' + name2[1::2])
print(s[:4] + ' ' + name2[:3])

#4.
place='Bletchley Park, Englend'
print(place[place.find(',')+2:])
print(place[place.find('y')::-1])
