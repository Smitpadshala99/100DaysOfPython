f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)

lines = ['line 4', 'line 5', 'line 6']
for line in lines:
    f.write(line + '\n')
f.close()