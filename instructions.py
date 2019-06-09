from memory import Memory

### instrucao MOVE ###
def MOVE(memory, operando1, operando2, PC):
    op1 = operando1
    mem = memory.memory
    if operando1 in memory.registers:
        if operando1[0] == 'd':
            operando1 = memory.registers[operando1]
        elif operando1[0] == 'a':
            operando1 = int(memory.memory[int(memory.registers[operando1])])
    elif operando1 == 'address':
        operando1 = int(mem[int(mem[PC + 2])])
    elif operando1 == 'constant':
        operando1 = int(mem[PC + 2])

    if operando2 in memory.registers:
        if operando2[0] == 'd':
            memory.registers[operando2] = operando1
        elif operando2[0] == 'a':
            memory.memory[memory.registers[operando2]] = operando1
        if op1 == 'address' or op1 == 'constant':
            memory.PC = memory.PC + 3
        else:
            memory.PC += 2
    elif operando2 == 'address' and op1 in memory.registers:
        memory.memory[int(memory.memory[PC + 2])] = operando1
        memory.PC = memory.PC + 3
    elif operando2 == 'address' and op1 == 'address':
        memory.memory[int(memory.memory[PC + 3])] = operando1
        memory.PC = memory.PC + 4
    return memory
### -------------- ###

### instrucao ADD ###
def ADD(memory, operando1, operando2, PC):
    op1 = operando1
    mem = memory.memory
    if operando1 in memory.registers:
        if operando1[0] == 'd':
            operando1 = memory.registers[operando1]
        elif operando1[0] == 'a':
            operando1 = int(memory.memory[int(memory.registers[operando1])])
    elif operando1 == 'address':
        operando1 = int(mem[int(mem[PC + 2])])
    elif operando1 == 'constant':
        operando1 = int(mem[PC + 2])

    if operando2 in memory.registers:
        if operando2[0] == 'd':
            memory.registers[operando2] += operando1
        elif operando2[0] == 'a':
            memory.memory[memory.registers[operando2]] += operando1
        if op1 == 'address' or op1 == 'constant':
            memory.PC = memory.PC + 3
        else:
            memory.PC += 2
    elif operando2 == 'address' and op1 in memory.registers:
        memory.memory[int(memory.memory[PC + 2])] += operando1
        memory.PC = memory.PC + 3
    elif operando2 == 'address' and op1 == 'address':
        memory.memory[int(memory.memory[PC + 3])] += operando1
        memory.PC = memory.PC + 4
    return memory
### ------------- ###


### instrucao SUB ###
def SUB(memory, operando1, operando2, PC):
    op1 = operando1
    mem = memory.memory
    if operando1 in memory.registers:
        if operando1[0] == 'd':
            operando1 = memory.registers[operando1]
        elif operando1[0] == 'a':
            operando1 = int(memory.memory[int(memory.registers[operando1])])
    elif operando1 == 'address':
        operando1 = int(mem[int(mem[PC + 2])])
    elif operando1 == 'constant':
        operando1 = int(mem[PC + 2])

    if operando2 in memory.registers:
        if operando2[0] == 'd':
            memory.registers[operando2] -= operando1
        elif operando2[0] == 'a':
            memory.memory[memory.registers[operando2]] -= operando1
        if op1 == 'address' or op1 == 'constant':
            memory.PC = memory.PC + 3
        else:
            memory.PC += 2
    elif operando2 == 'address' and op1 in memory.registers:
        memory.memory[int(memory.memory[PC + 2])] -= operando1
        memory.PC = memory.PC + 3
    elif operando2 == 'address' and op1 == 'address':
        memory.memory[int(memory.memory[PC + 3])] -= operando1
        memory.PC = memory.PC + 4
    return memory
### ------------- ###

### instrucao JUMP ###
def JUMP(memory, PC):
    memory.PC = int(memory.memory[PC + 1])
    return memory
### -------------- ###

### instrucao COMPARE ###
def CMP(memory, operando1, operando2, PC):
    op1 = operando1
    mem = memory.memory
    if operando1 in memory.registers:
        if operando1[0] == 'd':
            operando1 = memory.registers[operando1]
        elif operando1[0] == 'a':
            operando1 = int(memory.memory[int(memory.registers[operando1])])
    elif operando1 == 'address':
        operando1 = int(mem[int(mem[PC + 2])])
    elif operando1 == 'constant':
        operando1 = int(mem[PC + 2])

    if operando2 in memory.registers:
        if operando2[0] == 'd':
            if memory.registers[operando2] - operando1 == 0:
                memory.CR = 1
            else:
                memory.CR = 2
        elif operando2[0] == 'a':
            if memory.memory[memory.registers[operando2]] - operando1 == 0:
                memory.CR = 1
            else:
                memory.CR = 2
        if op1 == 'address' or op1 == 'constant':
            memory.PC = memory.PC + 3
        else:
            memory.PC += 2
    elif operando2 == 'address' and op1 in memory.registers:
        if memory.memory[int(memory.memory[PC + 2])] - operando1 == 0:
            memory.CR = 1
        else:
            memory.CR = 2
        memory.PC = memory.PC + 3
    elif operando2 == 'address' and op1 == 'address':
        if memory.memory[int(memory.memory[PC + 3])] - operando1 == 0:
            memory.CR = 1
        else:
            memory.CR = 2
        memory.PC = memory.PC + 4
    return memory
### ------------------ ###

### instrucao BRANCH ON EQUAL ###
def BEQ(memory, PC):
    if memory.CR == 1:
        memory.PC = int(memory.memory[PC + 1])
        memory.CR = 0
    else:
        memory.PC += 2
    return memory
### -------------- ###

### instrucao BRANCH ON NOT EQUAL ###
def BNE(memory, PC):
    if memory.CR == 2:
        memory.PC = int(memory.memory[PC + 1])
        memory.CR = 0
    else:
        memory.PC += 2
    return memory
### -------------- ###


def operando(code):
    if len(bin(code)[2:]) == 1:
        codigo = '000' + bin(code)[2:]
    elif len(bin(code)[2:]) == 2:
        codigo = '00' + bin(code)[2:]
    elif len(bin(code)[2:]) == 3:
        codigo = '0' + bin(code)[2:]
    else:
        codigo = bin(code)[2:]

    if codigo[0:2] == "00":
        if codigo[2:] == "00":
            return 'd0'
        elif codigo[2:] == "01":
            return 'd1'
        elif codigo[2:] == "10":
            return 'd2'
        elif codigo[2:] == "11":
            return 'd3'
    elif codigo[0:2] == "01":
        if codigo[2:] == "00":
            return 'a0'
        elif codigo[2:] == "01":
            return 'a1'
        elif codigo[2:] == "10":
            return 'a2'
        elif codigo[2:] == "11":
            return 'a3'
    elif codigo[0:2] == "10":
        return 'address'
    elif codigo[0:2] == "11":
        return 'constant'
    else:
        return 'invalido'


def tratar(memory, inicio):
    memory.PC = inicio
    while memory.memory[memory.PC] != 240:
        mem = memory.memory
        PC = memory.PC
        operando1 = operando(int(mem[PC + 1] / 16))
        operando2 = operando(int(mem[PC + 1] % 16))

        print(hex(PC).upper()[2:])
        print(f'$30 = {mem[48]}')

        if mem[PC] == int("10", 16):        #MOVE
            memory = MOVE(memory, operando1, operando2, PC)
        elif mem[PC] == int("20", 16):      #ADD
            memory = ADD(memory, operando1, operando2, PC)
        elif mem[PC] == int("30", 16):      #SUB
            memory = SUB(memory, operando1, operando2, PC)
        elif mem[PC] == int("40", 16):      #JUMP
            memory = JUMP(memory, PC)
        elif mem[PC] == int("50", 16):      #COMPARE
            memory = CMP(memory, operando1, operando2, PC)
        elif mem[PC] == int("61", 16):      #BRANCH ON EQUAL
            memory = BEQ(memory, PC)
        elif mem[PC] == int("62", 16):      #BRANCH ON NOT EQUAL
            memory = BNE(memory, PC)

        memory.showRegisters()

    return memory