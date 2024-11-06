a=[]

a.append(10)

# print('a value is',a)

a.insert(2,20)

# print('insert',a)

a.extend([1,2,3])

# print('extend',a)

a[0],a[1]=4,5

# print('replace using index',a)

a.extend([4,5])

# print('extended',a)

a.remove(4)

# print('remove - first occurance',a)

a.pop()

# print('pops last element',a)

a.pop(0)
#similar to del a[0]

# print('pop at index',a)

del a[3]
# print('del at index',a)

# [print(i) for i in a]



a.append(4)
# print('operations starts',a)


a[0],a[3]=a[3],a[0]
# print('swapped',a)

temp=a[0]
a[0]=a[3]
a[3]=temp
# print('temporary variable swap',a)

str_list=['Gfg', 'is', 'best', 'for', 'Geeks']

res = [ st.replace('G','-').replace('e','G').replace('-','e') for st in str_list]

# print('replace for string list',res)


str_list2=['Gfg', 'is', 'best', 'for', 'Geeks']

res2 = ','.join(str_list2)

res2=res2.replace('G','-').replace('e','G').replace('-','e').split(',')

# print(res2, type(res2))

str_list3 = ['Gfg', 'is', 'best', 'for', 'Geeks']

import re
res3 = [re.sub('-','e',re.sub('e','G',re.sub('G','-',sub))) for sub in str_list3]

# print(res3,type(res3))

a=[1, 2, 3, 4, 5]

length = len(a)

# print('length of list',length)

count = sum([1 for i in a])

add=sum(a)
# add=sum([i for i in a])

# print('counter and sum function of list',count,add)


from functools import reduce
a=[1, 2, 3, 4, 5]
i=0
add=reduce(lambda x, y: x + y, a)

# print('reduce function add',add)


max_num=max(a)
# print('max using max',max_num)

first = a[0]
second = a[2]
# print('list',a)
# print('max using ternary',first if first > second else second)

max_num = lambda x, y:x if x > y else y
# print(f'max using lambda {max_num(a[0],a[2])}')

max_num = [x for x in a if all(x>=y for y in a)][0]
# print(f'using list comprehension {max_num}')

a.sort()
# print(a[-1])

min_num=min(a)
# print('minimum in a using min()',min_num)

min_num=lambda x,y:x if x < y else y
# print(f'minimum in a using reduce and lambda',reduce(min_num, a))

# print('min num using sort',a[0])

# if 2 in a:
#     print('2 is at', a.index(2))

# if (any(x == 2 for x in a)):
#     print('is present',a.count(0)) 

# if(a.count(2)):
#     print('2 is present') 

a = [1, 2, 2, 3, 4, 4, 5]

a=list(set(a))

# print('a is',a)

a = [1, 2, 2, 3, 4, 4, 5]

a_list=[]

# for i in a:
#     if i not in a_list:
#         a_list.append(i)

# print(a_list)

[a_list.append(val) for val in a if val not in a_list]

# print('using list comprehension',a_list)

a = [1, 2, 2, 3, 4, 4, 5]
a_list= list(dict.fromkeys(a))
print('from dictionary', a_list)