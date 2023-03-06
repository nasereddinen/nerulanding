from django.shortcuts import render
from django.views import View


class DnbProductsView(View):
    def get(self, request):
        return render(request, "dnbproducts.html")
