mystr = "ashutosh is good boy"
# length-->20
print(len(mystr))
#20

print(mystr[0:9])
#ashutosh



print(mystr[0:9:2])  # miss 2 1 characters
#ahts 


print(mystr[::])  # in this case [0:string_len:by defallt it will be 1]
#ashutosh is good boy



print(mystr[0:20])
#ashutosh is good boy



print(mystr[0:])  # in this case [0:string_len]
#ashutosh is good boy



print(mystr[:20])  # in this case [0:string_len]
#ashutosh is good boy




print(mystr[0:70])
#ashutosh is good boy




print(mystr[::567])
#a




print(mystr[::-1])  # for reverse of string
#yob doog si hsotuhsa




print(mystr[::-2])  # for reverse of string and 1 gap character
#ybdo ihous




print(mystr[-4:-1])
# bo
