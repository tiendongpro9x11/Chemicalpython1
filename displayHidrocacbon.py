import os

class DisplayHidro:
    def __init__(self):
        self.mainlist = []
        self.mainlistanken = []
        self.mainlistdien = []
    def initC(self):
        #define (0:left) (1:right) (2:top) (3:bottom) (4: main) (5:left main) (6:right main) (7:count{Hidro})
        #(8:link pi) (9:link gamar) 
        return ["NULL","NULL","NULL","NULL",False,False,False,0,False,False]
    def initStyle2(self): #create C-C-C
        with open(os.getcwd()+"/logfile.log","w") as F:
            F.write("line 13: Cuoc song ma anh em\n")
        l = []
        C = self.initC()
        l.append(C)

        l[0][1] = 1
        l[0][4] = True
        l[0][5] = True

        C = self.initC()
        l.append(C)

        l[1][0] = 0
        l[1][1] = 2
        l[1][4] = True

        C = self.initC()
        l.append(C)

        l[2][0] = 1
        l[2][4] = True
        l[2][6] = True
        return l
    def HidroCacbon2tex(self,n,styleof):
        l = []
        if styleof == "ankan":
            #voi n <= 3 khong co dong phan
            if n==1: #Metan
                C = self.initC()
                C[0] = "Hidro"
                C[1] = "Hidro"
                C[2] = "Hidro"
                C[3] = "Hidro"
                C[4] = True
                C[5] = True
                C[6] = True
                C[7] = 4
                l.append(C)
                self.mainlist.append(l[:])
                return self.convert2Latex(l,styleof)
            elif n==2: #etan
                C = self.initC()
                C[0] = "Hidro"
                C[1] = 1
                C[2] = "Hidro"
                C[3] = "Hidro"
                C[4] = True
                C[5] = True
                C[6] = False
                C[7] = 3
                l.append(C[:])
                C[0] = 0
                C[1] = "Hidro"
                C[5] = False
                C[6] = True
                l.append(C[:])
                self.mainlist.append(l[:])
                return self.convert2Latex(l,styleof)

            l = self.initStyle2() #create C-C-C
            self.addCacbon(l,n)
            #step 3 remove loop
            self.removeLoop()

            #gan Hidro cho cac phan tu NULL
            for x in self.mainlist:
                for t in x:
                    for z in range(len(t)):
                        if t[z] == "NULL":
                            t[z] = "Hidro"
            #dem so luong Hidro
            for x in self.mainlist:
                for t in x:
                    for z in t:
                        if z== "Hidro":
                            t[7] +=1
            #them vao latex
            s = ""
            flag = False
            i = 0
            for x in self.mainlist:
                s += self.convert2Latex(x,styleof) 
                if flag:
                    s += "("+str(i)+")\\\\\n"
                    flag = True
                else:
                    s +="("+str(i)+")\\tab"
                    flag = True
                i+=1
            return s
        elif styleof=="anken" or styleof=="ankin" or styleof=="ankadien":
            if n == 2: #Etilen
                if styleof=="anken":
                    c = self.initC()
                    c[0] = "Hidro"
                    c[1] = 1
                    c[2] = "None"
                    c[3] = "Hidro"
                    c[4] = True
                    c[5] = True
                    c[6] = False
                    c[7] = 2
                    c[8] = "right"
                    l.append(c[:])
                    c[0] = 0
                    c[1] = "Hidro"
                    c[5] = False
                    c[6] = True
                    c[8] = "left"
                    l.append(c[:])
                else:
                    c = self.initC()
                    c[0] = "Hidro"
                    c[1] = 1
                    c[2] = "None"
                    c[3] = "None"
                    c[4] = True
                    c[5] = True
                    c[6] = False
                    c[7] = 1
                    c[8] = "right"
                    c[9] = "left"
                    l.append(c[:])
                    c[0] = 0
                    c[1] = "Hidro"
                    c[5] = False
                    c[6] = True
                    c[8] = "left"
                    c[9] = "right"
                    l.append(c[:])
                self.mainlistanken.append(l[:])
                return self.convert2Latex(l,styleof)
            #like ankan
            l =self.initStyle2()
            self.addCacbon(l,n)
            self.removeLoop()
            if styleof=="anken":
                self.addLink()
            elif styleof=="ankin":
                self.addLink(2)
            elif styleof=="ankadien":
                self.addLink()
                self.addLink(3)
            if styleof != "ankadien":
                tempmainlist = self.mainlistanken
            else:
                self.removeAkandien()
                tempmainlist = self.mainlistdien
            with open(os.getcwd()+"/logfile.log","a") as F:
                for x in tempmainlist:
                    F.write("line 160 "+str(x)+"\n")

            for x in tempmainlist:
                for t in x:
                    for z in range(len(t)):
                        if t[z] == "NULL":
                            t[z] = "Hidro"
            #dem so luong Hidro
            
            for x in tempmainlist:
                for t in x:
                    for z in t:
                        if z== "Hidro":
                            t[7] +=1
            #end for
            s = ""
            flag = False
            i = 0
            for x in tempmainlist:
                s += self.convert2Latex(x,styleof) 
                if flag:
                    s +="("+str(i)+")\\\\\n"
                    flag = True
                else:
                    s +="("+str(i)+")\\tab"
                    flag = True
                i+=1
            
            return s

    #return Cacbon Hidro
    def retCacbHi(self,variable):
        if variable[7] == 0:
            return "C"
        elif variable[7] == 1:
            return "CH"
        return "CH_{"+str(variable[7])+"}"
    def convert2Latex(self,variable,styleof):
        result = ""
        if styleof=="ankan":
            if len(variable) == 1:
                result = "CH_{4}"
            elif len(variable) < 3:
                for x in variable:
                    result += "CH_{" + str(x[7]) +"}"
                    if not x[6]:
                        result += '-'
            #truong hop co nhieu dong phan
            else:
                for q in variable:
                    if q[4]:
                        s = self.retCacbHi(q)
                        if isinstance(q[2],int):
                            #neu la top
                            s+="([:90]-"+self.retCacbHi(variable[q[2]])+")"
                        if isinstance(q[3],int):
                            #ney la bottom
                            s+="([:-90]-"+self.retCacbHi(variable[q[3]])
                            if isinstance(variable[q[3]][3],int):
                                s+="-"+self.retCacbHi(variable[variable[q[3]][3]])
                            s+=")"
                        result += s
                        if not q[6]:
                            #gan dau noi
                            result += '-'
        elif styleof=="anken" or styleof=="ankin" or styleof=="ankadien":
            if len(variable)==2:
                if styleof=="anken":
                    result = "CH_{2}=CH_{2}"
                else:
                    result = "CH~CH"
            else:
                for q in variable:
                    if q[4]:
                        s = self.retCacbHi(q)
                        if isinstance(q[2],int):
                            #neu la top
                            s+="([:90]-"+self.retCacbHi(variable[q[2]])+")"
                        if isinstance(q[3],int):
                            #ney la bottom
                            s+="([:-90]-"+self.retCacbHi(variable[q[3]])
                            if isinstance(variable[q[3]][3],int):
                                s+="-"+self.retCacbHi(variable[variable[q[3]][3]])
                            s+=")"
                        result += s
                        if not q[6]:
                            #gan dau noi
                            if (variable[q[1]][9]=="left" or variable[q[1]][9]=="leftright") and (q[9]=="right" or q[9]=="leftright"):
                                result += '~'
                            elif (variable[q[1]][8]=="left" or variable[q[1]][8]=="leftright") and (q[8]=="right" or q[8]=="leftright"):
                                result += '='
                            else:
                                result += '-'

        return '\chemfig{' + result +'}'

    #create main_list and add cacbon to main
    def addCacbon(self,listcacbon,n):
        if n<=3:
            self.mainlist.append(listcacbon[:])
            return False
        c = 0
        listoflist = []
        count_main = 1
        lenght_main = self.countMain(listcacbon)
        flag = True#speciel
        while True: #neu khong phai la ben phai
            #tao dia chi moi
            temp = []
            # 
            for x in listcacbon:
                temp.append(x[:])
            #bo qua them ben trai
            if c != 0:
                C = self.initC()
                #gan vao ben phai
                if listcacbon[c][6]:
                    temp[c][6] = False
                    temp[c][1] = len(temp)
                    C[0] = c
                    C[4] = True
                    C[6] = True
                    temp.append(C)
                    listoflist.append(temp[:])
                    break
                elif listcacbon[c][3] == "NULL":
                    #add bottom
                    temp[c][3] = len(temp) #them gia tri moi
                    C[2] = c
                    temp.append(C)
                    listoflist.append(temp[:])
                elif flag and isinstance(listcacbon[c][3],int) and count_main >= 3 and lenght_main-count_main+1>=3 and listcacbon[listcacbon[c][3]][3] == "NULL":
                    temp[temp[c][3]][3] = len(temp)
                    C[2] = temp[c][3]
                    temp.append(C)
                    listoflist.append(temp[:])
                    # with open(os.getcwd()+"/logfile.log","a") as F:
                    #     F.write("line 213 "+str(temp)+"\n")
                    flag = False
                    continue
                #coi chung ko thuc hien elif cuoi
                elif listcacbon[c][2] == "NULL":
                    #add top
                    temp[c][2] = len(temp) #them gia tri moi
                    C[3] = c
                    temp.append(C)
                    listoflist.append(temp[:])
                
            c = listcacbon[c][1]
            count_main +=1
        #end while

        n -=1
        for x in listoflist:
            #su dung de quy thay the
            res = self.addCacbon(x,n)
            if res:
                x = res
        return listoflist[:]
    
    def removeLoop(self):
        n = len(self.mainlist)
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i==j: #hai phan tu la mot
                    j+=1
                    continue
                else:
                    res = self.compare(self.mainlist[i],self.mainlist[j])
                    if res:
                        del self.mainlist[j]
                        n-=1
                        j-=1
                j+=1
            i+=1
        
    def compare(self,lista,listb,display=False):
        #True if equal, False if not equal
        len_a = self.countMain(lista)
        len_b = self.countMain(listb)
        if len_a != len_b :
            return False
        #TH1 giong nhau
        ta = []
        tb = []
        c1 = 0
        c2 = 0
        for x in lista:
            if x[4]: #mach chinh
                if x[3] != "NULL":
                    ta.append(c1)
                if x[2] != "NULL":
                    ta.append(c1)
                c1+=1
        for x in listb:
            if x[4]: #mach chinh
                if x[3] != "NULL":
                    tb.append(c2)
                if x[2] != "NULL":
                    tb.append(c2)
                c2+=1
        # if display:
        #     with open(os.getcwd()+"/logfile.log","a") as F:
        #         F.write(str(ta)+" "+str(tb)+"\n")
        if len(ta) != len(tb):
            return False
        if set(ta) == set(tb):
            return True
        #TH2 loai bo doi xung
        tc = []
        for i in tb:
            tc.append(len_a-1-i)
        if set(ta) == set(tc):
            return True
        return False

    def countMain(self,lista):
        count_main = 0
        for x in lista:
            if x[4]:
                count_main+=1
        return count_main
    def addLink(self,flag=1): #flag = True #ankin
        with open(os.getcwd()+"/logfile.log","a") as F:
            if flag != 3:
                tempmainlist = self.mainlist
            else:
                tempmainlist = self.mainlistanken
            for x in tempmainlist:
                if flag!=3:
                    F.write("line 391 "+str(self.checkmirror(x))+"\n")
                else:
                    F.write("line 393* "+str(x)+"\n")
                if flag==3:
                    chec =self.checkmirror(x,False)
                else:
                    chec = self.checkmirror(x)
                if chec:
                    #doi xung chi can them 1 ben
                    c = 0
                    leng = self.countMain(x)
                    while c < leng/2:
                        if (x[c][2] == "NULL" and x[x[c][1]][2] == "NULL") or (flag==3 and (not x[c][8] or not x[x[c][1]][8]) and (x[c][2]=="NULL" or x[c][3]=="NULL") and (x[x[c][1]][2] == "NULL" or x[x[c][1]][3]=="NULL")):
                            temp = []
                            for t in x:
                                temp.append(t[:])
                            if flag != 3:
                                temp[c][2] = "None"
                                if not temp[c][8]:
                                    temp[c][8] = "right"
                                else:
                                    temp[c][8] = "leftright"

                                temp[temp[c][1]][2] = "None"
                                if not temp[temp[c][1]][8]:
                                    temp[temp[c][1]][8] = "left"
                                else:
                                    temp[temp[c][1]][8] = "leftright"
                            else:
                                if x[c][2] == "NULL":
                                    temp[c][2] = "None"
                                    temp[c][8] = "right"
                                else:
                                    temp[c][3] = "None"
                                    temp[c][8] = "right"
                                if x[x[c][1]][2] == "NULL":
                                    temp[temp[c][1]][2] = "None"
                                    if not temp[temp[c][1]][8]:
                                        temp[temp[c][1]][8] = "right"
                                    else:
                                        temp[temp[c][1]][8] = "leftright"
                                else:
                                    temp[temp[c][1]][3] = "None"
                                    if not temp[temp[c][1]][8]:
                                        temp[temp[c][1]][8] = "left"
                                    else:
                                        temp[temp[c][1]][8] = "leftright"
                            if flag==1:
                                self.mainlistanken.append(temp[:])
                            elif flag==3:
                                self.mainlistdien.append(temp[:])
                            elif flag == 2 and x[c][3] == "NULL" and x[x[c][1]][3] == "NULL":
                                #khong co truong hop leftright voi lien ket garmar
                                temp[c][3] = "None"
                                temp[c][9] = "right"

                                temp[temp[c][1]][3] = "None"
                                temp[temp[c][1]][9] = "left"
                                self.mainlistanken.append(temp[:])

                        c = x[c][1]
                else:
                    #them tat ca
                    for k in range(len(x)): #moi k la mot cacbon
                        #manh chinh and not right
                        if x[k][4] and not x[k][6] and ((x[k][2] == "NULL" and x[x[k][1]][2] == "NULL") or (flag==3 and (not x[k][8] or not x[x[k][1]][8]) and (x[k][2] == "NULL" or x[k][3] == "NULL") and (x[x[k][1]][2] == "NULL" or x[x[k][1]][3] == "NULL"))) : 
                        #dieu kien them neu no va con tro ben phai
                            #create new list
                            temp = []
                            for t in x:
                                temp.append(t[:]) 
                            #tuong duong temp = x. khong vi pham vung nho
                            if flag != 3:
                                temp[k][2] = "None" #top None
                                if not temp[k][8]:
                                    temp[k][8] = "right"
                                else:
                                    temp[k][8] = "leftright"

                                temp[temp[k][1]][2] = "None"
                                if not temp[temp[k][1]][8]:
                                    temp[temp[k][1]][8] = "left"
                                else:
                                    temp[temp[k][1]][8] = "leftright"
                            else:
                                if x[k][2] == "NULL":
                                    temp[k][2] = "None" #top None
                                    if not temp[k][8]:
                                        temp[k][8] = "right"
                                    else:
                                        temp[k][8] = "leftright"
                                else:
                                    temp[k][3] = "None" #top None
                                    if not temp[k][8]:
                                        temp[k][8] = "right"
                                    else:
                                        temp[k][8] = "leftright"
                                if x[x[k][1]][2] == "NULL":
                                    temp[temp[k][1]][2] = "None"
                                    if not temp[temp[k][1]][8]:
                                        temp[temp[k][1]][8] = "left"
                                    else:
                                        temp[temp[k][1]][8] = "leftright"
                                else:
                                    temp[temp[k][1]][3] = "None"
                                    if not temp[temp[k][1]][8]:
                                        temp[temp[k][1]][8] = "left"
                                    else:
                                        temp[temp[k][1]][8] = "leftright"

                            if flag==1:
                                self.mainlistanken.append(temp[:])
                            elif flag==3:
                                self.mainlistdien.append(temp[:])
                            elif flag==2 and x[k][3] == "NULL" and x[x[k][1]][3] == "NULL":
                                #khong co truong hop leftright voi lien ket gamar
                                temp[k][3] = "None"
                                temp[k][9] = "right"
                                temp[temp[k][1]][3] = "None"
                                temp[temp[k][1]][9] = "left"
                                self.mainlistanken.append(temp[:])
    def cacbonLevel(self,cacb):
        count = 0
        if isinstance(cacb[0],int):
            count+=1
        if isinstance(cacb[1],int):
            count+=1
        if isinstance(cacb[2],int):
            count+=1
        if isinstance(cacb[3],int):
            count+=1
        return count
    def checkmirror(self,listcacbon,flag=True): #flag kiem tra cho truong hop Akandien
        leng = self.countMain(listcacbon)
        i_lef = -1
        j_rig = -1
        if leng%2==0:
            i_lef = leng/2-1
            j_rig = leng/2
        else:
            if not flag: #neu mach le voi flag danh dau co it nhat lien ket Pi thi co ket qua
                return False
            i_lef = leng/2
            j_rig = leng/2
        c = 0
        t_left = [] #danh dau vi tri ben trai
        t_right = [] #danh dau vi tri ben phai
        t_pi = [] #danh dau vi tri co lien ket pi
        for x in listcacbon: #chia doi mach ra de kiem tra
            if x[4]:
                if x[3] != "NULL":
                    if c <= i_lef:
                        t_left.append(c)
                    if c>= j_rig:
                        t_right.append(c)
                if x[2] != "NULL":
                    if c <= i_lef:
                        t_left.append(c)
                    if c>= j_rig:
                        t_right.append(c)
                if not flag and x[8]:
                    t_pi.append(c)

                c+=1
        #end for
        if len(t_left) != len(t_right):
            return False #khong doi xung
        t_cop = []
        for i in t_right:
            t_cop.append(leng-1-i)
        if set(t_left) == set(t_cop):
            if not flag:
                if  leng/2 in t_pi and leng/2-1 in t_pi:
                    return True
                else:
                    return False
            # voi akandien truong hop doi xung bi thu hep lai vi co lien ket pi
            return True #doi xung
        return False #khong doi xung
    def removeAkandien(self):
        n = len(self.mainlistdien)
        i = 0
        while i < n:
            j = 0
            while j < n:
                if i==j:
                    j+=1
                    continue
                else:
                    res = self.compareAkandien(self.mainlistdien[i],self.mainlistdien[j])
                    if res:
                        del self.mainlistdien[j]
                        n-=1
                        j-=1
                j+=1
            i+=1

    def compareAkandien(self,lista,listb):
        len_a = self.countMain(lista)
        len_b = self.countMain(listb)
        if len_a != len_b:
            return False
        t_a = []
        t_b = []
        c_a = 0
        c_b = 0
        #xoa bo cac phan tu hoan toan giong nhau. Khong can xet truong hop doi xung
        for x in lista:
            if x[4]:#mach chinh
                if x[8]: #neu co lien ket pi
                    t_a.append(str(c_a)+"-"+x[8])
                c_a+=1
        for x in listb:
            if x[4]:
                if x[8]:
                    t_b.append(str(c_b)+"-"+x[8])
                c_b+=1
        if set(t_a)==set(t_b):
            return True
        #doi xung khong gian chay lai voi c_b2 va t_b2
        c_b2 = 0
        t_b2 = []
        for x in listb:
            if x[4]:
                if x[8]=="left":
                    t_b2.append(str(len_a-1-c_b2)+"-right")
                elif x[8]=="right":
                    t_b2.append(str(len_a-1-c_b2)+"-left")
                elif x[8]=="leftright":
                    t_b2.append(str(len_a-1-c_b2)+"-leftright")
                c_b2+=1
        # with open(os.getcwd()+"/logfile.log","a") as F:
        #     F.write("line 623 "+)
        if set(t_a)==set(t_b2):
            return True     
        return False
    def getlist(self,styleof):
        if styleof=="ankan":
            return len(self.mainlist)
        elif styleof=="anken" or styleof=="ankin":
            return len(self.mainlistanken)
        elif styleof=="ankadien":
            return len(self.mainlistdien)
    def getElementList(self,styleof):
        if styleof=="ankan":
            return self.mainlist
        elif styleof=="anken" or styleof=="ankin":
            return self.mainlistanken
        elif styleof=="ankadien":
            return self.mainlistdien
class DisplayAren:
    def __init__(self):
        self.l = []
        self.mainlist = []
    # def init
    def initC(self):
        
        #define (0:NULL) (1:NULL) (2:NULL) (3:NULL) (4:NULL) (5:NULL)
        #define cacbon (0:left) (1:right) (2:top) (3:bot) (4:count Hidro) (5:link pi) (6:pos in bezen)
        return ["NULL","NULL","NULL","NULL",0,False,1]
    def initTou(self):
        return ["Benzen","Hidro","Hidro","Hidro",3,False,1]
    def Aren2tex(self,n):
        if n==6:
            return self.convert2Latex(n,self.l)
        if n==7:
            C = self.initTou()
            self.l.append(C)
            return self.convert2Latex(n,self.l)
        if n==8:
            C = self.initTou()
            C[1] = 1
            C[4] = 2
            self.l.append(C)
            C = self.initTou()
            C[0] = 0
            C[6] = -1
            self.l.append(C)
            self.mainlist.append(self.l)
            #xong dong phan 1 
            C = self.initTou()
            self.l = []
            self.l.append(C)
            C = self.initTou()
            C[6] = 2
            self.l.append(C)
            self.mainlist.append(self.l)
            #xong dong phan 2
            C = self.initTou()
            self.l = []
            self.l.append(C)
            C = self.initTou()
            C[6] = 3
            self.l.append(C)
            self.mainlist.append(self.l)
            #xong dong phan 3
            C = self.initTou()
            self.l = []
            self.l.append(C)
            C = self.initTou()
            C[6] = 4
            self.l.append(C)
            self.mainlist.append(self.l)
            #xong dong phan 4
            s = ""
            flag = False
            for x in self.mainlist:
                s += self.convert2Latex(n,x)
                s +="\\tab"
                # if flag:
                #     s += "\\\\\n"
                #     flag = True
                # else:
                #     s +="\\tab"
                #     flag = True
            return s

    def retCacbHi(self,variable):
        if variable[4] == 0:
            return "C"
        elif variable[4] == 1:
            return "CH"
        return "CH_{"+str(variable[4])+"}"
    def convert2Latex(self,n,x):
        result = ""
        if n==6:
            result = "*6(-=-=-=)"
        if n==7:
            result = "*6(-=-=(-" +self.retCacbHi(self.l[0]) + ")-=)"
        if n==8:
            if x[1][6] == -1: 
                result = "*6(-=-=(-" +self.retCacbHi(x[0])+"-"+self.retCacbHi(x[1]) + ")-=)"
            elif x[1][6] == 2:
                result = "*6(-=-(-"+self.retCacbHi(x[1])+")=(-"+self.retCacbHi(x[0])+")-=)"
            elif x[1][6] == 3:
                result = "*6(-=(-"+self.retCacbHi(x[1])+")-=(-" +self.retCacbHi(self.l[0]) + ")-=)"
            elif x[1][6] == 4:
                result = "*6(-(-"+self.retCacbHi(x[1])+")=-=(-" +self.retCacbHi(self.l[0]) + ")-=)"

        return '\chemfig{' + result +'}'