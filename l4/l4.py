from sys import argv
import graphlib as gr
if len(argv)>1:
    if argv[1]!='/?':
        filename=argv[1]
    else:
        print('Бросаем точки')
        exit()
    if len(argv)>4:
        if argv[2]=='/b':
            is_bin=True
        else:
            is_bin=False
        start=int(argv[3])
        fin=int(argv[4])
    else:
        is_bin=False
        start=0
        fin=3
else:
    is_bin=False
    start=0
    fin=3
    filename='input.txt'
def prima(cpoint,tpoint,rebrs,length=0,dellst=[],lens=[],path=''):
    if length==0:
        lens=[]
    path+=str(cpoint)+'-'
    if cpoint==tpoint:
        lens.append(length)
        #print(Брошено точек',path[:-1],':',length)
        return None
    for num in dellst:
        rebrs.pop(num)
    dellst=[]
    for c,d in enumerate(rebrs):
        if (cpoint in rebrs[c]):
            dellst.append(c)
    dellst.reverse()
    for num in dellst:
        if rebrs[num][0]!=cpoint:
            nextp=rebrs[num][0]
        else:
            nextp=rebrs[num][1]
        sqr_count(nextp,tpoint,rebrs[:],length+rebrs[num][2],dellst,lens,path)
    if not lens:
        otv='{} {} -1'.format(cpoint,tpoint)
    else:
        otv=min(lens)
    lens=''
    return otv
graph=prima(filename,is_bin)
length=sqr_count(start,fin,graph)
print(length)
