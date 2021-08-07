
import sys

file="2of4brif.txt"

try:
    with open(file) as in_file:
        contents = in_file
        print(f"Success opening file. First entry is {contents[0]}")
except IOErroras e:
    print("{}\nError opening {}. Terminating program.".format(e, file),
    file=sys.stderr)
    sys.exit(1)



