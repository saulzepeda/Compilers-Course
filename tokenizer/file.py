res_words = ['if', 'for', 'while', 'else', 'int', 'float', 'bool', '#include', '#define', '<iostream>', 
'cout', 'cin', 'return', 'main', 'using', 'namespace', 'std', '<<', '>>']
op_arith = ['+', '-', '/', '*', '^']
op_relat = ['<', '>', '<=', '>=']
op_logic = ['&&', '||']
op_grouping = ['(', ')', '[', ']', '{', '}']

with open('src.txt', 'r') as file:
    lines = file.readlines()

f_res = open("res_words.txt", "w")
f_arith = open("op_arith.txt", "w")
f_relat = open("op_relat.txt", "w")
f_logic = open('op_logic.txt', 'w')
f_grouping = open('op_grouping.txt', 'w')
f_ids = open('ids.txt', 'w')
f_nums = open('nums.txt', 'w')

for line in lines:
    line = line[:-1]

    words = line.split(' ')
    for word in words:
        if word.endswith(';'):
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