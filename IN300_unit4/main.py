# mySet = set({100,200,300,400,500})
#
# print(mySet)
#
# mySet.add(150)
# mySet.add(250)
# mySet.add(350)
# mySet.add(400)
#
# print(mySet)
#
# mySet.remove(150)
# mySet.remove(250)
# mySet.remove(350)
#
# print(mySet)


protocol = {'source_ip':'222.22.22.222','dest_id':'111.11.11.111','protocol':'UDP','info':'LEN=1068'}

print(protocol.keys())

for i in protocol.keys():
    print('Key: ' + i + ' - Value: ' + protocol.get(i))