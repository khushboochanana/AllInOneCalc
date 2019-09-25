from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import re 

def index(request):
    print(request.GET)
    if 'equation' in request.GET:
        equation=request.GET['equation'] 
    else: 
        equation =''

    if 'resultInput' in request.GET:
        resultInput=request.GET['resultInput'] 
    else: 
        resultInput =''

    if 'output' in request.GET:
        output=request.GET['output'] 
    else: 
        output =''
    if 'numval' in request.GET:
        numVal=request.GET['numval'] 
        if numVal == 'clear':
            resultInput=""
            equation=""
            output=""
        else :
            resultInput +=numVal
            equation += (numVal +' ')

    if 'sym' in request.GET:
        nextEq='0'
        symList=['+','-','/','*']
        sym= request.GET['sym']

        if sym == 'del':
            resultInput=resultInput[0:len(resultInput)-1]
            equation=equation[0:len(equation)-1]
        else:
            subparts= resultInput.split(sym)
            
            if(subparts and len(subparts)):
                subparts.append(sym)
                if len(subparts[0]) :
                    if(subparts[0][0] in symList):
                        part1= subparts[0]
                        nextEq= str(part1[0])+ str(float(part1[1:len(part1)]))
                        print(nextEq,">nextEq")
                    else:   
                        print (subparts[0]) 
                        nextEq= str(float(subparts[0]))
                    print (nextEq,">?>?>?>?")
                elif (len(subparts[1])):
                    nextEq= sym + str(float(subparts[1]))

                output  = eval(output +  nextEq)

            if(sym != '='):
                resultInput=sym
                equation += (sym +' ')
            else: 
                resultInput ='' 
    
   
    print({'resultInput':resultInput,'output':output, 'equation': equation})

    return render(request, 'index.html', {'resultInput':resultInput,'output':output, 'equation': equation})
