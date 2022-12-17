import csv


def analyze_log(path_to_file):
    if file_type(path_to_file) != 'csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            content = [[i[0], i[1], i[2]] for i in csv.reader(file)]
            a = marias_most_requested_dish(content)
            b = how_many_times_did_arnaldo_order_a_hamburger(content)
            c = which_dishes_joao_never_ordered(content)
            d = what_days_did_joao_never_go_to_the_cafeteria(content)
            with open('data/mkt_campaign.txt', mode='w') as file:
                file.write(f'{a}\n{b}\n{c}\n{d}')
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def file_type(path):
    type = (path[len(path) - 3], path[len(path) - 2], path[len(path) - 1])
    return ''.join(type)


def get_bigger(dishes):
    compare, max = 0, ''
    for key in dishes:
        if dishes[key] > compare:
            compare = dishes[key]
            max = key
    return max


def generic(content, n, name):
    v = [line[n] for line in content if line[0] == name]
    v_n = [line[n] for line in content if line[n] not in v]
    v_d = '{'
    for i in v_n:
        if i not in v_d:
            v_d += f"'{i}', "
    r = v_d[:-len(', ')]
    r += '}'
    return r


# Qual o prato mais pedido por 'maria'?
def marias_most_requested_dish(content):
    dishes = dict()
    for line in content:
        if line[0] == 'maria':
            if line[1] in dishes:
                dishes[line[1]] += 1
            else:
                dishes[line[1]] = 1
    return get_bigger(dishes)


# Quantas vezes 'arnaldo' pediu 'hamburguer'?
def how_many_times_did_arnaldo_order_a_hamburger(content):
    times = 0
    for line in content:
        if line[0] == 'arnaldo' and line[1] == 'hamburguer':
            times += 1
    return times


# Quais pratos 'joao' nunca pediu?
def which_dishes_joao_never_ordered(content):
    return generic(content, 1, 'joao')


# Quais dias 'joao' nunca foi à lanchonete?
def what_days_did_joao_never_go_to_the_cafeteria(content):
    return generic(content, 2, 'joao')
