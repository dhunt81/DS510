poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# open for  'w'riting
f = open('poem.txt', 'w')
#write text to file
f.write(poem)
#close text file
f.close()

# read file in 'r'ead mode
f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end="")
f.close()



