import sys
print(sys.path);
tf= 'infrastructure_configuration.txt'
f = open(tf,'r')
readed_lines = f.readlines()
for line in readed_lines:
    line_items = line.strip().split('=')
    print(line)
    print(line_items[0]+' '+line_items[1])
