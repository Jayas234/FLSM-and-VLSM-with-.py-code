def FLSM(ip_num,k):
    defaultsubnet=['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.255']
    subnet={'255.0.0.0':'11111111.0.0.0','255.255.0.0':'11111111.11111111.0.0','255.255.255.0':'11111111.11111111.11111111.0','255.255.255.255':'11111111.11111111.11111111.1111111'}
    k=1
    while True:
            #print(k)
            c=2**k
            #print(c)
            if c>=ip_num:
                break
            else:
                k+=1
        #print("The nearest value of the given ip's range is :",c)
    if c<255:
            l=defaultsubnet[2]
            print("The Default Subnet Mask of Class C:",defaultsubnet[2])
    elif c<65025:
            l=defaultsubnet[1]
            print("The Default Subnet Mask of Class B:",defaultsubnet[1])
    elif c<16581375:
            l=defaultsubnet[0]
            print("The Default Subnet Mask of Class A:",defaultsubnet[0])
    e=(32-k)*"1"
    f=k*'0'
    g=e+f
    i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
    j=subnet[l]
    print("The Binary Representation Of New Subnet Mask is:",g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::]))
    h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
    print("The New Subnet Mask Value is",'.'.join(h))
    print("The Prefix Length of New SubnetMask is:",i.count('1'))
    z=i.count('1')-j.count('1')
    print("No of Networks :",int(2**(z)))
    print("No of Hosts :",c)
def VLSM(ip_num):#Variable Length Subnet Mask
      for i in range(len(ip_num)):
        k=1
        print("The Details of",ip_num[i],"Hosts are:")
        a=0
        a=int(ip_num[i])
        while True:
            c=2**k
            if c>=a:
                break
            else:
                k+=1
        #print("The nearest value of the given ip's range is :",c)
        if c<255:
            l=defaultsubnet[2]
            print("The Default Subnet Mask of Class C:",defaultsubnet[2])
        elif c<65025:
            l=defaultsubnet[1]
            print("The Default Subnet Mask of Class B:",defaultsubnet[1])
        elif c<16581375:
            l=defaultsubnet[0]
            print("The Default Subnet Mask of Class A:",defaultsubnet[0])
        e=(32-k)*"1"
        f=k*'0'
        g=e+f
        i=str(g[0:8])+str(g[8:16])+str(g[16:24])+str(g[24::])
        j=subnet[l]
        print("The Binary Representation Of New Subnet Mask is:",g[0:8]+"."+str(g[8:16])+"."+str(g[16:24])+"."+str(g[24::]))
        h=[(str(int(g[0:8],2))),(str(int(g[8:16],2))),(str(int(g[16:24],2))),(str(int(g[24::],2)))]
        print("The New Subnet Mask Value is",'.'.join(h))
        print("The Prefix Length of New SubnetMask is:",i.count('1'))
        z=i.count('1')-j.count('1')
        print("No of Networks :",int(2**(z)))
        print("No of Hosts :",c)

print("Which type of subnetting method do you want to choose either FLSM or VLSM ?")
method=input()
k=1
A='255.0.0.0'
B='255.255.0.0'
C='255.255.255.0'
defaultsubnet=['255.0.0.0','255.255.0.0','255.255.255.0','255.255.255.255']
subnet={'255.0.0.0':'11111111.0.0.0','255.255.0.0':'11111111.11111111.0.0','255.255.255.0':'11111111.11111111.11111111.0','255.255.255.255':'11111111.11111111.11111111.1111111'}
if method=='FLSM':
    print("How many IP's you required ?")
    ip_num=int(input())
    FLSM(ip_num,k)
elif method=='VLSM':
    print("Enter the Number Of Hosts You need ..?")
    ip_num=list(map(int,input().split()))
    VLSM(ip_num,defaultsubnet,subnet)
elif method=='Manual IP':
    print("GOODBYE...!!!Its A Wrong Input!!!")
