import msvcrt
import sys

memsize = 2048

try:
    programfile = open(sys.argv[1],"r")
except:
    print("Please give a valid file name.")
    quit()
    
program = programfile.read()
programfile.close()


programposition = 0
loopstart = 0
readhead = 0
mem = []
for x in range(memsize):
    mem.append(0)


while 1:
    instruction = program[programposition]
    if instruction == "+":
        mem[readhead] = mem[readhead]+1
    if instruction == "-":
        mem[readhead] = mem[readhead]-1
    if instruction == ">":
        readhead = readhead+1
    if instruction == "<":
        readhead = readhead-1
    if instruction == "[":
        loopstart = programposition
    if instruction == "]":
        if mem[readhead] != 0:
            programposition = loopstart
    if instruction == ".":
        print(chr(mem[readhead]),end="")
    if instruction == ",":
        mem[readhead] = ord(msvcrt.getch())
        
    programposition+=1
    if programposition == len(program):
        break
