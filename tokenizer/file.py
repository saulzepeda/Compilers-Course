res_words = ['if', 'for', 'while', 'else', 'int', 'float', 'bool', '#include', '#define', '<iostream>', 
'cout', 'cin', 'return', 'main', 'using', 'namespace', 'std', '<<', '>>']
op_arith = ['+', '-', '/', '*', '^']
op_relat = ['<', '>', '<=', '>=']
op_logic = ['&&', '||']
op_grouping = ['(', ')', '[', ']', '{', '}']

with open('src3.txt', 'r') as file:
    lines = file.readlines()

f_res = open("res_words.txt", "w")
f_arith = open("op_arith.txt", "w")
f_relat = open("op_relat.txt", "w")
f_logic = open('op_logic.txt', 'w')
f_grouping = open('op_grouping.txt', 'w')
f_ids = open('ids.txt', 'w')
f_nums = open('nums.txt', 'w')
f_strs = open('strs.txt', 'w')
f_comments = open('comms.txt', 'w')

for line in lines:
    line = line[:-1]
    comm_id = line.find('//')
    if comm_id >= 0:
        f_comments.write(line + '\n')
        continue
    start_id = line.find('\"')
    if start_id >= 0:
        line = line[0 : start_id] + line[start_id + 1:]
        end_id = line.find('\"')
        str_to_remove = line[start_id:end_id]
        f_strs.write(str_to_remove + '\n')
        line = line[0 : start_id] + line[end_id + 1:]

    words = line.split(' ')
    for word in words:
        print(word)
        if word.endswith(';'):
            word = word[:-1]
            print(word)
        if word.endswith(','):
            word = word[:-1]
        elif word in res_words:
            f_res.write(word + '\n')
        elif word in op_arith:
            f_arith.write(word + '\n')
        elif word in op_relat:
            f_relat.write(word + '\n')
        elif word in op_logic:
            f_logic.write(word + '\n')
        elif word in op_grouping:
            f_grouping.write(word + '\n')
        elif word.isnumeric():
            f_nums.write(word + '\n')
        elif len(word) > 0:
            f_ids.write(word + '\n')

f_res.close()
f_arith.close()
f_relat.close()
f_logic.close()
f_grouping.close()
f_ids.close()
f_nums.close()
f_strs.close()
f_comments.close()