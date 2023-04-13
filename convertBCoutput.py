import sys

def attrName(attr):
    if attr == 1:
        return 'setor_nome'
    elif attr == 2:
        return 'departamento_nome'
    elif attr == 3:
        return 'curso_nome'
    elif attr == 4:
        return 'bloco_nome'
    elif attr == 5:
        return 'disciplina_nome'
    elif attr == 6:
        return 'tipo_de_sala'
    elif attr == 7:
        return 'turma_codigo'
    elif attr == 8:
        return 'vagas_oferecidas'
    elif attr == 9:
        return 'dia_semana'
    elif attr == 10:
        return 'hr_inicio'
    elif attr == 11:
        return 'hr_fim'
    elif attr == 12:
        return 'periodo'
    else:
        return ''

with open(sys.argv[1], 'r') as f:
    input_string = f.read()

lines = input_string.split('\n')
for line in lines:
    if line:
        line_tuple = tuple(int(numero) for numero in line.strip('()').split(','))
        if line_tuple:
            print("("+", ".join(attrName(attr) for attr in line_tuple)+")")