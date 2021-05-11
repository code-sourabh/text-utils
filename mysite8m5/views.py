# this page is created by - Sourabh
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request ,'index.html')
    # return HttpResponse("<h1> Hey I am SOURABH MISHRA </h1>")

def removePuctuation(request) :
    djtext = request.POST.get('text' , 'default')
    punc_status = request.POST.get('removepunc'  , 'off')
    newline_status = request.POST.get('newlineremover'  , 'off')
    extraspace_status = request.POST.get('extraspaceremover'  , 'off')
    allcaps_status = request.POST.get('allcaps'  , 'off')

    analysed= ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if punc_status == 'on':
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
                djtext = analysed

    if newline_status == 'on':
        for char in djtext:
            if char == '\n':
                char = " "
                analysed = analysed + char
                djtext = analysed


    if extraspace_status == 'on':
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analysed = analysed + char
                djtext = analysed

    if allcaps_status == 'on':
        analysed = djtext.upper()

    params = { 'analysed_text': analysed }
    return render(request ,'analyse.html' , params)       
    params = { 'analysed_text': djtext}
    return render(request ,'analyse.html' , params)