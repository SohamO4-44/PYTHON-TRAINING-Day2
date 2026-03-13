mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])
mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
mylist.append('harsh')
mylist.append("laxman")
print(mylist)


mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
mylist.insert(1,"sanket")
print(mylist)


mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
mylist.remove("sandip")
print(mylist)


mylist = ["poorvi","Ashish","sandip","pankaj","shweta"]
newlist = mylist.copy() #cloning
print(mylist)
print(newlist)


mylist = [['prashant','jha'],['85.56'],[440022,'yyy']]
print("Example of multidimensional list:")
print(mylist)
