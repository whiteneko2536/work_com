n = 26
def b_gen_dash(n):
    print('-'*n*2,end='')
def a_gen_dash(n):
    print('-'*n*2,end='\n')
def gen_alp(n,big_n):
    alp_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    minus=big_n-n
    for i_,i in enumerate(range((minus*-1)+1,minus)):
        abs_ = abs(i)
        pos=n+abs_
        print(alp_[pos],end='')
        if i_ != (minus-1)*2:
            print('-', end='')
loop_num=(n*2)-1
start_num=(n-1)*-1
for i in range(0,loop_num):
    abs_ = abs(start_num)
    b_gen_dash(abs_)
    gen_alp(abs_,n)
    a_gen_dash(abs_)
    start_num+=1



