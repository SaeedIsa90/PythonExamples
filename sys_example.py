import sys

print("Python version", sys.version)

# stdin, stdout, stderr (input, output and error channels) control
sys.stdout.write('Hello\n')

# control channel
fd = open('my_stdout.txt', 'w')
sys.stdout = fd
print('Helllllllloooooooo')
sys.stdout.close()

sys.stdout = sys.__stdout__
print('Hello again')

# Max int size
print('Max int size:', sys.maxsize)

# Command line arguments
print('Sys args:', sys.argv)
print('Args[1]', sys.argv[1])

# Path
print('PYTHONPATH', sys.path)
for i in sys.path:
    print('Path: ', i)

# Exit
sys.exit()
