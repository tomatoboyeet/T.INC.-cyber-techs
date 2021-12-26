import subprocess,datetime,io,time
def clean(x):
    while '  'in x:x=x.replace('  ',' ')
    x,g=x.lower().replace('static','static\n').replace("b'",'').replace("'",'').replace(r'\r\n',''),False
    x=x.replace('dynamic','dynamic\n').replace('interface:','').replace(' 38-9d-92-cc-58-eb dynamic','').replace('\n ','\n')
    x,result=x.replace('--- 0x12 internet address physical address type',','),''
    for i in x:
        if not g==False:result+=i
        if i=='\n':g=True
    return result.replace('\n ','\n').removeprefix(' ').removesuffix('\n255.255.255.255 ff-ff-ff-ff-ff-ff static\n').replace('-','')
def r(x,t):
    if t==True:
        with open('IPlogs.txt','r')as z:
            x,result=io.StringIO(x),''
            for i in x.readlines():result+=str(datetime.datetime.now())+'\n'+i if not i in z.read()else print('')
            return result
    else:
        with open('IPdata.txt','r')as z:
            x,result=io.StringIO(x),''
            for i in x.readlines():result+=i if not i in z.read()else print('')
            return result
def main():
    x=clean(str(subprocess.check_output('arp -a', stderr=subprocess.STDOUT)))
    with open('IPdata.txt','a')as z3:y=z3.read()
    if not x==y and not x in y:
        with open('IPdata.txt','a')as z1:z1.write(r(x,False))
        with open('IPlogs,txt','a')as z2:z2.write(r(x,True))
