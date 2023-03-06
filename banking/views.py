from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request, 'banking/index.html',{})



def About(request):
    return render(request,'banking/about.html',{})


def Contact(request):
    return render(request,'banking/contact.html',{})


def Faq(request):
    return render(request,'banking/faq.html',{})


def Pricing(request):
    return render(request,'banking/pricing.html',{})


def PrivacyPolicy(request):
    return render(request,'banking/privacy-policy.html',{})


def Services(request):
    return render(request,'banking/services.html',{})


def TermsOfService(request):
    return render(request,'banking/terms-of-service.html',{})










