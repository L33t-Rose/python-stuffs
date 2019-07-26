content=None
mylist=None


with open("C:\\Users\\XBBN04G\\Desktop\\stuff.txt") as myfile:
    content=myfile.read()

mylist=content.split(",")

myQuery=input("What do you want to learn about?")

if(myQuery=="Legend Of Zelda Ocarina Of Time"):
    print("The Legend of Zelda: Ocarina of Time is an action-adventure game developed and published by Nintendo for the Nintendo 64. It was released in Japan and North America in November 1998, and in Europe, Australia and New Zealand the following month")
