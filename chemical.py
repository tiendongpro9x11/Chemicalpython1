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
                if x[6]:
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
    def display(self,cacbonlist):
        print "1"