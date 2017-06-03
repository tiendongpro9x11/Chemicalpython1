def retCacbHi(variable):
    if variable[7] == 0:
        return "C"
    elif variable[7] == 1:
        return "CH"
    return "CH_{"+str(variable[7])+"}"
#display 1 mach Hidrocacbon
def convert2Latex(variable,styleof):
    result = ""
    if styleof=="ankan": ##su dung cho ca mach no co Cl
        if len(variable) == 1:
            result = "CH_{4}"
        elif len(variable) < 3:
            for x in variable:
                result += "CH_{" + str(x[7]) +"}"
                # s = ""
                if x[2] == "Clor":
                    result+="([:90]-Cl)"
                elif x[2] == "OH":
                    result+="([:90]-OH)"
                if x[3] == "Clor":
                    result+="([:-90]-Cl)"
                elif x[3] == "OH":
                    result+="([:-90]-OH)"
                if not x[6]:
                    result += '-'
        #truong hop co nhieu dong phan
        else:
            for q in variable:
                if q[4]:
                    s = retCacbHi(q)
                    if isinstance(q[2],int):
                        #neu la top
                        s+="([:90]-"+retCacbHi(variable[q[2]])+")"
                    elif q[2] == "Clor":
                        s+="([:90]-Cl)"
                    elif q[2] == "OH":
                        s+="([:90]-OH)"
                    if isinstance(q[3],int):
                        #ney la bottom
                        s+="([:-90]-"+retCacbHi(variable[q[3]])
                        if isinstance(variable[q[3]][3],int): #truong hop dac biet voi bot co -CH2-CH3
                            s+="-"+retCacbHi(variable[variable[q[3]][3]])
                        s+=")"
                    elif q[3] == "Clor":
                        s+="([:-90]-Cl)"
                    elif q[3] == "OH":
                        s+="([:-90]-OH)"
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
                    s = retCacbHi(q)
                    if isinstance(q[2],int):
                        #neu la top
                        s+="([:90]-"+retCacbHi(variable[q[2]])+")"
                    if isinstance(q[3],int):
                        #ney la bottom
                        s+="([:-90]-"+retCacbHi(variable[q[3]])
                        if isinstance(variable[q[3]][3],int):
                            s+="-"+retCacbHi(variable[variable[q[3]][3]])
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