# -*- coding: utf-8 -*-
import os

from convertLatex import convert2Latex
class ankan:
    def __init__(self):
        self.main = []
    def display(self,cacbonlist):
        if len(cacbonlist) == 1:
            #CH4 ~ co tinh chat rieng
            content = r"a) Phản ứng thế với $Cl_{2}, Br_{2}$\\"+"\n"
            content += r"\tab $CH_{4} + Cl_{2} \xrightarrow[\text{}]{\text{ánh sáng}} CH_{3}Cl + HCl$\\"+"\n"
            content += r"b) Phản ứng phân hủy \\"+"\n"
            content += r"\tab $CH_{4} \xrightarrow[\text{}]{\text{$t^{o} cao$}} C + 2H_{2}$\\"+"\n"
            content += r"c) Phản ứng cháy\\"+"\n"
            content += r"\tab $CH_{4} + 2O_{2} \xrightarrow[\text{}]{\text{$t^{o}$}} CO_{2} + 2H_{2}O$\\"+"\n"
            content += r"d) Oxi hóa không hoàn toàn \\"+"\n"
            content += r"\tab $2CH_{4} + O_{2} \xrightarrow[\text{100atm}]{\text{$200^{o}C$}} CH_{3}-OH$\\"+"\n"
            content += r"\tab $CH_{4} + O_{2} \xrightarrow[\text{$V_{2}O_{5}$}]{\text{$300^{o}C$}} \chemfig{H-C([1]=O)([-1]-H)} + H_{2}O$\\"+"\n"
            return content
        
        else:
            tempList = []
            n = len(cacbonlist)

            for x in cacbonlist:
                tempList.append(x[:])
            for x in tempList:
                if x[6]: #phan tu right
                    x[1] = "Clor"
                    x[7]-=1
            content = r"a) Phản ứng thế với $Cl_{2}, Br_{2}$\\"+"\n"
            temp = convert2Latex(tempList,"ankan")
            content += r"$"+convert2Latex(cacbonlist,"ankan")+r"+Cl_{2}\xrightarrow[\text{}]{\text{ánh sáng}}"+temp[:-1]+r"-Cl}+HCl$\\"+"\n"
            content += r"b) Phản ứng phân hủy \\"+"\n"
            content += r"\tab $C_{"+str(n)+r"}H_{"+str(2*n+2)+r"} \xrightarrow[\text{}]{\text{$t^{o} cao$}} "+str(n)+r"C + "+str(n+1)+r"H_{2}$\\"+"\n"
            content += r"c) Phản ứng dehidro \\"+"\n"
            # content += r"\\"+"\n"
            content += r"\tab $C_{"+str(n)+r"}H_{"+str(2*n+2)+r"} \xrightarrow[\text{}]{\text{$450^{o} C$}} C_{"+str(n)+r"}H_{"+str(2*n)+r"} + H_{2}$\\"+"\n"
            content += r"d) Phản ứng cháy \\"+"\n"
            if (3*n+1)%2==0:
                a = str((3*n+1)/2)
            else:
                a = r"\frac{"+str(3*n+1)+r"}{2}"
            content += r"\tab $C_{"+str(n)+r"}H_{"+str(2*n+2)+r"}+"+a+r"O_{2} \xrightarrow[\text{}]{\text{$t^{o}$}}" +str(n)+r"CO_{2} +"+ str(n+1)+r"H_{2}O$\\"+"\n"
            content += r"f) Oxi hóa tạo ra Axit\\"+"\n"
            content += r"\chemfig{R-CH_{2}-CH_{2}-R'} $\xrightarrow[\text{muối $Mn^{2+}$}]{\text{$O_{2}$ kk}}$  \chemfig{R-C([1]=O)([-1]-OH)}+ \chemfig{R'-C([1]=O)([-1]-OH)}\\"+"\n"
            if n>=3:
                content += r"e) Phản ứng cracking (skip)\\"+"\n"
            # with open(os.getcwd()+"/logfile.log","w") as F:
            #     F.write(content)
            return content
class anken:
    def __init__(self):
        self.main = []
    # def createtemp(self,cacbonlist):
    #     tempList = []
    def display(self,cacbonlist):
        tempList = []
        n = len(cacbonlist)
        #tao ra truong hop cong H2
        for x in cacbonlist:
            tempList.append(x[:])
        for x in tempList:
            if x[8]:#neu no la lien ket Pi
                x[8] = False
                if x[2] == "None":
                    x[2] = "Hidro"
                elif x[3] == "None":
                    x[3] = "Hidro"
                x[7] +=1
                # with open(os.getcwd()+"/logfile.log","a") as F:
                #     F.write("line 71: "+str(x7)+" "+str(x[2])+" "+str(x[3])+"\n")
        content = r"a) Phản ứng cộng\\"+"\n"
        #phan ung + H2
        content += r"$"+convert2Latex(cacbonlist,"anken")+r"+H_{2}\xrightarrow[\text{}]{\text{Ni $t^o$}}"+convert2Latex(tempList,"ankan")+r"$\\"+"\n"
        ### phan ung + HCl
        del tempList[:]
        for x in cacbonlist:
            tempList.append(x[:])
        t = []
        for x in range(n):
            if tempList[x][8]:
                t.append(x)
        if tempList[t[0]][7] < tempList[t[1]][7]:
            #gan clor vao phan tu it Hidro hon
            tempList[t[0]][8] = False
            if tempList[t[0]][2] == "None":
                tempList[t[0]][2] = "Clor"
            elif tempList[t[0]][3] == "None":
                tempList[t[0]][3] = "Clor"
            #them hidro
            tempList[t[1]][8] = False
            tempList[t[1]][7]+=1
            if tempList[t[1]][2] == "None":
                tempList[t[1]][2] = "Hidro"
            elif tempList[t[1]][3] == "None":
                tempList[t[1]][3] = "Hidro"
        else:
            #gan clor vao phan tu it Hidro hon
            tempList[t[1]][8] = False
            if tempList[t[1]][2] == "None":
                tempList[t[1]][2] = "Clor"
            elif tempList[t[1]][3] == "None":
                tempList[t[1]][3] = "Clor"
            #them Hidro
            tempList[t[0]][8] = False
            tempList[t[0]][7]+=1
            if tempList[t[0]][2] == "None":
                tempList[t[0]][2] = "Hidro"
            elif tempList[t[0]][3] == "None":
                tempList[t[0]][3] = "Hidro"
        ##
        content += r"$"+convert2Latex(cacbonlist,"anken")+r"+HCl\xrightarrow[\text{}]{\text{xt}}"+convert2Latex(tempList,"ankan")+r"$\\"+"\n"
        ##Phan ung + Cl2
        del tempList[:]
        for x in cacbonlist:
            tempList.append(x[:])
        t = []
        for x in range(n):
            if tempList[x][8]:
                t.append(x)
        for x in tempList:
            if x[8]:
                x[8] = False
                if x[2] == "None":
                    x[2] = "Clor"
                elif x[3] == "None":
                    x[3] = "Clor"
        ##
        content += r"$"+convert2Latex(cacbonlist,"anken")+r"+Cl_{2}\xrightarrow[\text{}]{\text{}}"+convert2Latex(tempList,"ankan")+r"$\\"+"\n"
        ##Phan ung + H2O
        del tempList[:]
        for x in cacbonlist:
            tempList.append(x[:])
        t = []
        for x in range(n):
            if tempList[x][8]:
                t.append(x)
        if tempList[t[0]][7] < tempList[t[1]][7]:
            #gan clor vao phan tu it Hidro hon
            tempList[t[0]][8] = False
            if tempList[t[0]][2] == "None":
                tempList[t[0]][2] = "OH"
            elif tempList[t[0]][3] == "None":
                tempList[t[0]][3] = "OH"
            #them hidro
            tempList[t[1]][8] = False
            tempList[t[1]][7]+=1
            if tempList[t[1]][2] == "None":
                tempList[t[1]][2] = "Hidro"
            elif tempList[t[1]][3] == "None":
                tempList[t[1]][3] = "Hidro"
        else:
            #gan clor vao phan tu it Hidro hon
            tempList[t[1]][8] = False
            if tempList[t[1]][2] == "None":
                tempList[t[1]][2] = "OH"
            elif tempList[t[1]][3] == "None":
                tempList[t[1]][3] = "OH"
            #them Hidro
            tempList[t[0]][8] = False
            tempList[t[0]][7]+=1
            if tempList[t[0]][2] == "None":
                tempList[t[0]][2] = "Hidro"
            elif tempList[t[0]][3] == "None":
                tempList[t[0]][3] = "Hidro"
        content += r"$"+convert2Latex(cacbonlist,"anken")+r"+HCl\xrightarrow[\text{$280^{o}C$}]{\text{$H_{3}PO_{4}$}}"+convert2Latex(tempList,"ankan")+r"$\\"+"\n"
        ##Phan ung Oxi hoa
        content += r"b) Phản ứng oxi hóa\\"+"\n"
        del tempList[:]
        for x in cacbonlist:
            tempList.append(x[:])
        t = []
        for x in range(n):
            if tempList[x][8]:
                t.append(x)
        for x in tempList:
            if x[8]:
                x[8] = False
                if x[2] == "None":
                    x[2] = "OH"
                elif x[3] == "None":
                    x[3] = "OH"
        content += r"$"+convert2Latex(cacbonlist,"anken")+r"+[O]+H_{2}O\xrightarrow[\text{}]{\text{$KMnO_{4}$}}"+convert2Latex(tempList,"ankan")+r"$\\"+"\n"
        #Phan ung chay
        content += r"c) Phản ứng cháy\\"+"\n"
        if (3*n)%2==0:
            a = str((3*n)/2)
        else:
            a = r"\frac{"+str(3*n)+r"}{2}"
        content += r"\tab $C_{"+str(n)+r"}H_{"+str(2*n)+r"}+"+a+r"O_{2} \xrightarrow[\text{}]{\text{$t^{o}$}}" +str(n)+r"CO_{2} +"+ str(n)+r"H_{2}O$\\"+"\n"
        #Phan ung trung hop
        content += r"d) Phản ứng trùng hợp\\"+"\n"
        return content
