#before running this script, make 2 files: IPlogs.txt and IPdata.txt, both are essential for this to work.
import subprocess,datetime,io,time
def r(x,t):
    x,result=io.StringIO(x),''
    if t==True:
        with open('IPlogs.txt','r')as z:
            for i in x.readlines():result+=str(datetime.datetime.now())+'\n'+i if not i in z.read()else time.sleep(0.000000001)
            return result
    else:
        with open('IPdata.txt','r')as z:
            for i in x.readlines():result+=i if not i in z.read()else time.sleep(0.000000001)
            return result
def main():
    x=str(subprocess.check_output('arp -a', stderr=subprocess.STDOUT))
    while '  'in x:x=x.replace('  ',' ')
    x,result=x.lower().replace('static','static\n').replace("b'",'').replace("'",'').replace(r'\r\n','').replace('dynamic','dynamic\n').replace('interface:','').replace(' 38-9d-92-cc-58-eb dynamic','').replace('\n ','\n').replace('--- 0x12 internet address physical address type',','),''
    for i in x:
        if i=='\n':break
        else:result+=i    
    x=result.replace('\n ','\n').removeprefix(' ').removesuffix('\n255.255.255.255 ff-ff-ff-ff-ff-ff static\n').replace('-','')
    with open('IPdata.txt','r')as z3:y=z3.read()
    if not x==y and not x in y:
        with open('IPdata.txt','a')as z1:z1.write(r(x,False))
        with open('IPlogs.txt','a')as z2:z2.write(r(x,True))
