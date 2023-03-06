from django.shortcuts import render
from django.views import View


class ChromeExtensionIndexView(View):
    def get(self, request):
        return render(request, "chromeextension-index.html")
