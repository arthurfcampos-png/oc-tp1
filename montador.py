#dicionario de dicionarios para facilitar a organização e acesso às informações das instruções
mapa_instrucoes = {
    'add': {'tipo': 'R', 'funct3': '000', 'funct7': '0000000', 'opcode': '0110011'},
    'sub': {'tipo': 'R', 'funct3': '000', 'funct7': '0100000', 'opcode': '0110011'},
    'and': {'tipo': 'R', 'funct3': '111', 'funct7': '0000000', 'opcode': '0110011'},
    'or':  {'tipo': 'R', 'funct3': '110', 'funct7': '0000000', 'opcode': '0110011'},
    'xor': {'tipo': 'R', 'funct3': '100', 'funct7': '0000000', 'opcode': '0110011'},
    'sll': {'tipo': 'R', 'funct3': '001', 'funct7': '0000000', 'opcode': '0110011'},
    'srl': {'tipo': 'R', 'funct3': '101', 'funct7': '0000000', 'opcode': '0110011'},

    'addi': {'tipo': 'I', 'funct3': '000', 'opcode': '0010011'},
    'andi': {'tipo': 'I', 'funct3': '111', 'opcode': '0010011'},
    'ori':  {'tipo': 'I', 'funct3': '110', 'opcode': '0010011'},
    
    'lb':   {'tipo': 'I', 'funct3': '000', 'opcode': '0000011'},
    'lh':   {'tipo': 'I', 'funct3': '001', 'opcode': '0000011'},
    'lw':   {'tipo': 'I', 'funct3': '010', 'opcode': '0000011'},

    'sb':   {'tipo': 'S', 'funct3': '000', 'opcode': '0100011'},
    'sh':   {'tipo': 'S', 'funct3': '001', 'opcode': '0100011'},
    'sw':   {'tipo': 'S', 'funct3': '010', 'opcode': '0100011'},

    'beq':  {'tipo': 'B', 'funct3': '000', 'opcode': '1100011'},
    'bne':  {'tipo': 'B', 'funct3': '001', 'opcode': '1100011'}
}


#converte um registrador (Ex x2) para binário
def registrador_para_binario(registrador):
    return format(int(registrador[1:]), '05b')


#converte um imediato pra binário de forma correta
def imediato_para_binario(imediato, bits=12):
    numero = int(imediato, 0)

    binario = format(numero & ((1 << bits)-1), f'0{bits}b')
    return binario