text = 'hello world'

def solve(s):
    s_list = s.split(' ')
    comp_ = list(map(lambda x: x.capitalize(), s_list))
    str_ = ''
    for i in comp_:
        #print(i)
        str_ += i
        str_ += ' '
    return str_

print(solve(text))