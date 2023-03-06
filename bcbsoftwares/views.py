from django.shortcuts import render

# Create your views here.


def bcbvideosoftware(request):
    return render(request, 'bcbvideosoftwares.html')


def bcbprojectmanagment(request):
    return render(request, 'bcbprojectmanagment.html')


def bcbcrmsoftware(request):
    return render(request, 'bcbcrmsoftware.html')


def bcbappointmentsoftware(request):
    return render(request, 'bcbappointmentsoftware.html')


def bcbaccountingsoftware(request):
    return render(request, 'bcbaccountingsoftware.html')


def bcbtextmarketing(request):
    return render(request, 'bcbtextmarketingsoftware.html')

# # create viewes for bcbfilesharing.com, bcbvideoconferencing.com,bcbvideoconferencing.com,bcbvoice.com ,www.⦁	bcbmarketingautomation.com,bcbwebsitebuilder.com,www.bcbwebhosting.com,bcbseosoftware.com


def bcbfilesharing(request):
    return render(request, 'bcbfilesharingsoftware.html')


def bcbvideoconferencing(request):
    return render(request, 'bcbvideoconferencingsoftware.html')


def bcbvoice(request):
    return render(request, 'bcbvoice.html')


def bcbmarketingautomation(request):
    return render(request, 'bcbmarketingautomationsoftware.html')


def bcbwebhosting(request):
    return render(request, 'bcbwebhostingsoftware.html')


def bcbwebsitebuilder(request):
    return render(request, 'bcbwebsitebuildersoftware.html')


def bcbseosoftware(request):
    return render(request, 'bcbseosoftware.html')
