import sys
input = lambda: sys.stdin.readline().rstrip()

opcode_dict = {
    'ADD':  '0000',
    'SUB':  '0001',
    'MOV':  '0010',
    'AND':  '0011',
    'OR':   '0100',
    'NOT':  '0101',
    'MULT': '0110',
    'LSFTL':'0111',
    'LSFTR':'1000',
    'ASFTR':'1001',
    'RL':   '1010',
    'RR':   '1011'
}

def convert_string_to_binString(string, length):
    binary = bin(int(string))[2:]
    while len(binary) < length:
        binary = '0' + binary
    return binary

N = int(input())
for _ in range(N):
    opcode, rD, rA, x = input().split()
    result = ''
    if opcode.endswith('C'):
        opcode = opcode[:-1]
        result += opcode_dict[opcode]
        result += '1'
        result += '0'
        result += convert_string_to_binString(rD, 3)
        result += convert_string_to_binString(rA, 3)
        result += convert_string_to_binString(x, 4)
    else:
        result += opcode_dict[opcode]
        result += '0'
        result += '0'
        result += convert_string_to_binString(rD, 3)
        result += convert_string_to_binString(rA, 3)
        result += convert_string_to_binString(x, 3)
        result += '0'
    print(result)