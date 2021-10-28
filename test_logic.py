# n=5
# print('Guntapong') if n==2 else None
#
# stm_="insert"
# value_1=1
# value_2=2
#
# if stm_ in ['insert']:
#     list_1=[]
#     real_cmd="list_1.{0}({1},{2})".format(stm_,value_1,value_2)
#     print(real_cmd)
#     eval((real_cmd))
#     print(list_1)
#
# text='print'
# text.split(' ')[1]

#
# integer_list = tuple(map(int, input().split()))
# print(hash(integer_list))
#
# text='A'
# print(len(text))
# print(text.upper())
# n_p=5
# n=4
# def b_gen_dash(n):
#     print('-'*n*2,end='')
#
# def a_gen_dash(n):
#     print('-'*n*2,end='\n')
#
# def gen_alp(n):
#     loop_ = n_p-n
#     for i in range(0,loop_):
#         print()
#
#
#
# b_gen_dash(n)
# a_gen_dash(n)

def gen_alp(n,big_n):
    alp_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    minus=big_n-n
    for i_,i in enumerate(range((minus*-1)+1,minus)):
        #print(i)
        abs_ = abs(i)
        #print(n+abs_)
        pos=n+abs_
        print(alp_[pos],end='')
        #print('-', end='')

        #print((minus-1)*2)
        if i_ != (minus-1)*2:
            print('-', end='')

gen_alp(1,5)

text='A'
print(text[-1])
