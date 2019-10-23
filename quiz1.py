f = open('/home/ubuntu/environment/files/relative_data.txt', 'r')
lines = f.read() #instead of readlines - splits at new line to create line of strings
f.close()
print(lines)