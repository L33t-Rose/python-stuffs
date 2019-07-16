myfile=open("hello.txt")
content=myfile.read()


#New Method
with open('hello.txt') as mynewfile:
    content=mynewfile.read()


#You can write to files also when you are opening it
with open('hello.txt',mode='r') as myn:
    c=myn.read()
    myn.seek(0)


#modes -> w for write, a for append, r+ is reading and writing, w+ is writing and reading creates a new file
#Using append
with open('test.txt',mode='a') as f:
    f.write('5')

#Using write
with open('anotherone.txt',mode='w') as write:
    write.write("I'm sorry phil, I'm afraid I can't let you do that")
