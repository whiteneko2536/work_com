N = int(input())
list_1 = []
list_cmd=[]
for i in range(0,N):
    # print(i)
    stm_ = str(input())
    cmd_ = str(stm_.split(' ')[0])
    if cmd_ in ['insert', 'remove', 'append', 'pop', 'reverse', 'sort']:
        if len(stm_.split(' ')) == 3:
            value_1 = int(stm_.split(' ')[1])
            value_2 = int(stm_.split(' ')[2])
            real_cmd = "list_1.{0}({1},{2})".format(cmd_, value_1, value_2)
        elif len(stm_.split(' ')) == 2:
            value_1 = int(stm_.split(' ')[1])
            real_cmd = "list_1.{0}({1})".format(cmd_, value_1)
        elif len(stm_.split(' ')) == 1:
            real_cmd = "list_1.{0}()".format(cmd_)
        list_cmd.append(real_cmd)
    elif cmd_ == 'print':
        real_cmd = "print(list_1)"
        list_cmd.append(real_cmd)
print(list_cmd)
for i in list_cmd:
    eval(i)


# cmd = "print('5555')"
# eval(cmd)
