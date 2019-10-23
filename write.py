f = open('newfile.txt', 'a') # 'w' for write or 'a' for append or 'r' for read
lines = ['Hello', 'World', 'Welcome', 'To', 'File I/O']
text = '\n'.join(lines)
f.writelines(text)
#f.write("Hello\n")
f.close()