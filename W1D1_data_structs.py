color=["红", "绿", "蓝"]
print(color[-1])
color.append("黄")
color.remove("绿")
print(color)

num=[0,1,2,3,4,5,6,7,8,9]
print(num[2:10:2])

str1="hello"
print(str1[::-1])

drama={"剧名": "虎妈驾到", "热度": 7828, "评分": 9.3}
print(drama["热度"])
drama["题材"]="家庭"
del drama["评分"]
print(drama)

lst=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
new_lst=list(set(lst))
count=len(new_lst)

square=[x**2 for x in range(1,6)]

name_lst=["虎妈驾到", "渐染", "沈小姐她不干了"]
name={name_lst[i]:len(name_lst[i]) for i in range(len(name_lst))}

com=["好看！","太烂了","演技不错","剧情拖沓","好看！"]
num_com=len(set(com))
good_com=[comm for comm in com if '好看' in comm or '不错' in comm]