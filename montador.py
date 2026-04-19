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


#função principal de "montagem" dos binários finais
def montador(instrucao):
    instrucao = instrucao.replace(',', ' ').replace('(', ' ').replace(')', ' ')
    partes = instrucao.split()

    if not partes:
        return 'Erro: Formato inválido ou instrução não fornecida'
    

    tipo_instrucao = partes[0]

    #abaixo vamos mapear pseudo-instruções
    if tipo_instrucao == 'mv':
        tipo_instrucao = 'add'

        partes = ['add', partes[1], partes[2], 'x0']

    elif tipo_instrucao == 'li':
        tipo_instrucao = 'ori'

        partes = ['ori', partes[1], 'x0', partes[2]]

    elif tipo_instrucao == 'bnez':
        tipo_instrucao = 'bne'

        partes = ['bne', partes[1], 'x0', partes[2]]


    #fazemos a identificação dos formatos de instrução e a montagem dos binários finais
    if tipo_instrucao not in mapa_instrucoes:
        return 'Instrução não mapeada ou não suportada'
    
    
    dados = mapa_instrucoes[tipo_instrucao]

    if dados['tipo'] == 'R':
        funct3 = dados['funct3']
        funct7 = dados['funct7']
        opcode = dados['opcode']

        rd = registrador_para_binario(partes[1])
        rs1 = registrador_para_binario(partes[2])
        rs2 = registrador_para_binario(partes[3])

        binario_final = f'{funct7}{rs2}{rs1}{funct3}{rd}{opcode}'


    if dados['tipo'] == 'S':
        funct3 = dados['funct3']
        opcode = dados['opcode']

        rs2 = registrador_para_binario(partes[1])
        
        imm_bin = imediato_para_binario(partes[2], 12) 
        
        rs1 = registrador_para_binario(partes[3])

        imm_1 = imm_bin[0:7] 
        imm_2 = imm_bin[7:12]

        binario_final = f'{imm_1}{rs2}{rs1}{funct3}{imm_2}{opcode}'


    if dados['tipo'] == 'I':
        funct3 = dados['funct3']
        opcode = dados['opcode']
        
        rd = registrador_para_binario(partes[1])
        
        if tipo_instrucao in ['lb', 'lh', 'lw']:
            imm_bin = imediato_para_binario(partes[2])
            rs1 = registrador_para_binario(partes[3])
        else:
            rs1 = registrador_para_binario(partes[2])
            imm_bin = imediato_para_binario(partes[3])
        
        binario_final = f'{imm_bin}{rs1}{funct3}{rd}{opcode}'


    if dados['tipo'] == 'B':
        funct3 = dados['funct3']
        opcode = dados['opcode']
        
        rs1 = registrador_para_binario(partes[1])
        rs2 = registrador_para_binario(partes[2])
        
        imm_bin = imediato_para_binario(partes[3], 13)
        
        imm_1 = imm_bin[0]
        imm_2 = imm_bin[2:8]
        imm_3 = imm_bin[8:12]
        imm_4 = imm_bin[1]
        
        binario_final = f'{imm_1}{imm_2}{rs2}{rs1}{funct3}{imm_3}{imm_4}{opcode}'

    return binario_final