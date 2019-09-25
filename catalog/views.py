from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import re 

def index(request):
    print(request.GET)
    if 'equation' in request.GET:
        equation=request.GET['equation'] 
    else: 
        equation ='0'

    if 'resultInput' in request.GET:
        resultInput=request.GET['resultInput'] 
    else: 
        resultInput ='0'

    if 'output' in request.GET:
        output=request.GET['output'] 
    else: 
        output =''
    if 'numval' in request.GET:
        resultInput +=request.GET['numval'] 
        equation += (request.GET['numval'] +' ')

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
                print(resultInput.split(sym) , resultInput, equation)
                print(subparts,"subparts",resultInput)
                if len(subparts[0]) :
                    if(subparts[0][0] in symList):
                        nextEq= str(subparts[0])
                    else:    
                        nextEq= str(int(subparts[0]))
                output  = eval(output +  nextEq)
            if(sym != '='):
                resultInput=sym
                equation += (sym +' ')
            else: 
                resultInput ='' 
    
   
    print({'resultInput':resultInput,'output':output, 'equation': equation})

    return render(request, 'index.html', {'resultInput':resultInput,'output':output, 'equation': equation})
