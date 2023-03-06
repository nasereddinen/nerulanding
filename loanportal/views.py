from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import ContextMixin

from user.forms import UserDataForm
from user.models import UserData
from .models import *


class LoanApplicationView(View):

    def get(self, request):
        documents = Document.objects.filter(user=Profile.objects.get(user=request.user))
        data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
        if data:
            form = UserDataForm(None, instance=data)
        else:
            form = UserDataForm()
        error = request.session.get("formInvalid")

        return render(request, "loanapplication.html", {"documents": documents, "form": form, "error": error})

    def post(self, request):
        form = UserDataForm(request.POST)
        if form.is_valid():
            print('valid')
            data = UserData.objects.filter(user=Profile.objects.get(user=request.user)).first()
            if data:
                form = UserDataForm(request.POST, instance=data)
                new_data = form.save(commit=False)
                new_data.user = Profile.objects.get(user=request.user)
                new_data.save()
            else:
                new_data = form.save(commit=False)
                new_data.user = Profile.objects.get(user=request.user)
                new_data.save()
            if request.session.get('formInvalid'):
                request.session.pop('formInvalid')
        else:
            print('invalid')
            request.session['formInvalid'] = True
            return redirect("loanportal:loanapplication")

        if 'saveData' in request.POST:
            return redirect("loanportal:loanapplication")

        if request.POST.get('all_documents') == "on":
            data = {
                "document": request.FILES['Driver License / Photo Id'],
                "type": 'Driver License / Photo Id'
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()
            data = {
                "document": request.FILES['Social Security Card'],
                "type": 'Social Security Card'
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()
            data = {
                "document": request.FILES['Last 3 Months Of Bank Statement'],
                "type": 'Last 3 Months Of Bank Statement'
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()

        else:
            data = {
                "document": request.FILES['document'],
                "type": request.POST['document_type']
            }
            new_document = Document(user=Profile.objects.get(user=request.user), **data)
            new_document.save()

        return redirect("loanportal:loanapplication")


class LoanOffersView(ContextMixin, View):
    def get(self, request):
        loans = Loan.objects.filter(user=Profile.objects.get(user=request.user))
        return render(request, "loanoffers.html", {"loans": loans})
