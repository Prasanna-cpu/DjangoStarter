from django.http import HttpResponse,JsonResponse
# Create your views here.

from django.shortcuts import render
def home(request):
    return HttpResponse("Bolo Jai Shree Ram!")


# def staticfile(request):
#     return render(request, 'index.html')



def Json(request):
    data=[
        {
            "Name":"Kumar",
            "Programming Language":"Python"
        }
        ,
        {

            "Name": "Atul",
            "Programming Language": "Java"

        }
        ,
        {

            "Name": "Dinesh",
            "Programming Language": "Javascript"
        }


    ]

    return JsonResponse(data,status=200,safe=False)

def success(request):
    return HttpResponse("<h3>Hello World!</h3>")


def People(request):

    people=[
        {
            "Name":"Peter Griffin",
            "Gender":"Male",
            "Age":45

        }
        ,
        {
            "Name":"Glenn Quagmire",
            "Gender":"Male",
            "Age":42
        }
        ,
        {
            "Name":"Loius Griffin",
            "Gender":"Female",
            "Age":37
        }

    ]

    return render(request,"index.html",{"people":people})