from django.shortcuts import render, redirect
from django.views import View

from business.models import CredibilitySteps, OtherChecklistSteps


class MainChecklistView(View):
    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        othersteps = OtherChecklistSteps.objects.filter(user=request.user).first()
        if not othersteps:
            othersteps = OtherChecklistSteps(user=request.user)
            othersteps.save()

        steps_done = True
        for i, k in steps.__dict__.items():
            if not bool(k):
                steps_done = False

        return render(request, "BusinessCredibilityChecklist/MainCheckList.html",
                      {'steps_done': steps_done, 'othersteps': othersteps})

    def post(self, request):
        othersteps = OtherChecklistSteps.objects.filter(user=request.user).first()
        if not othersteps:
            othersteps = OtherChecklistSteps(user=request.user)
            othersteps.save()

        stp = request.POST.get('step')
        if stp:
            stp = int(stp)
            if stp == 2:
                othersteps.established = True
            if stp == 3:
                othersteps.tier1 = True
            if stp == 4:
                othersteps.monitor = True
            if stp == 5:
                othersteps.tier2 = True
            if stp == 6:
                othersteps.tier3 = True
            if stp == 7:
                othersteps.tier4 = True

        undo = request.POST.get('undo')
        print(undo)
        if undo:
            undo = int(undo)
            if undo == 2:
                othersteps.established = False
            if undo == 3:
                othersteps.tier1 = False
            if undo == 4:
                othersteps.monitor = False
            if undo == 5:
                othersteps.tier2 = False
            if undo == 6:
                othersteps.tier3 = False
            if undo == 7:
                othersteps.tier4 = False

        othersteps.save()
        return redirect('business:business_credibility_checklist')


class EstablishingView(View):
    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        return render(request, "BusinessCredibilityChecklist/EstablishingChecklist.html")

    def post(self, request):
        othersteps = OtherChecklistSteps.objects.filter(user=request.user).first()
        if not othersteps:
            othersteps = OtherChecklistSteps(user=request.user)
            othersteps.save()
        othersteps.established = True
        othersteps.save()
        return redirect('business:business_credibility_checklist')


class BusinessCredibilityChecklist(View):
    def get(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()
        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        page = request.session.get('page')
        request.session.pop('page') if page else None
        return render(request, "BusinessCredibilityChecklist/BusinessCredibilityChecklist.html",
                      {'page': page, 'steps': steps})

    def post(self, request):
        steps = CredibilitySteps.objects.filter(user=request.user).first()

        if not steps:
            steps = CredibilitySteps(user=request.user)
            steps.save()

        data = request.POST
        for i in data:
            if hasattr(steps, i):
                val = data.get(i)
                if val == 'true':
                    val = True
                setattr(steps, i, val)
        steps.save()
        request.session['page'] = request.POST.get('page')
        return redirect('business:business_credibility_checklist1')
