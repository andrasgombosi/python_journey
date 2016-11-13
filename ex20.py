from sys import argv
script, input_file = argv


def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line (line_count,f):
    print line_count, f.readline(),
#---------------------

print(input_file)

current_file = open(input_file)

print("First print the entire file")

print_all(current_file)


print("rewind then")
rewind(current_file)

print"Now handpick hte lines"

for i in range(0,3):
    print_a_line(i,current_file)
