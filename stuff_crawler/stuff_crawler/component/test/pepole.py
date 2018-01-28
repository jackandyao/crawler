# result=5>3?1:0 1 if True else 0
total = 50
pagesize = 200
print(total/pagesize)
print(total%pagesize)

totalpage = total/pagesize if total%pagesize==0 else int(total/pagesize) +1



# skip = (n-1)*pagesize
skip =0
# limit = pagesize
limit =0

num = 1

while num <= totalpage:

    print(num,(num-1)*pagesize,pagesize)
    num += 1