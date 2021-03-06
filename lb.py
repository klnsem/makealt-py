import sys
import subprocess

filename = sys.argv[1]

"""
how to use:
python3 lb.py filename
and filename is here understood as without the .s, so with a file named falafel.s it would be
python3 lb.py falafel
"""

# links the assembly file.
commandline = subprocess.run(["as", "-o", filename + ".o", filename + ".s"], 
                             stdout=subprocess.PIPE)

print (commandline.stdout.decode("utf-8"))

# builds the assembly file via gcc.
commandline = subprocess.run(["gcc", "-o", filename, filename + ".o"],
                             stdout=subprocess.PIPE)

print ("Standard Output: \n")
print (commandline.stdout.decode("utf-8"))

# runs the file and outputs both the programs output and its error codes.
commandline = subprocess.run(["./first", ";", "echo", "$?"],
                             stdout=subprocess.PIPE, stderr = subprocess.STDOUT)
print ("\nERROR MESSAGES: \n")
print (commandline.returncode)
