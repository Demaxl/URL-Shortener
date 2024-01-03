import secrets

from django.shortcuts import render, redirect
from django.views.generic import View
from pprint import pprint
from django.db import IntegrityError
from .models import Link

class IndexView(View):
    def get(self, request):
        result = request.session.get("result", None)
        if result:
            del request.session['result']
            result = request.build_absolute_uri(result)

        return render(request, "index.html", {
            "result": result
        })

    def post(self, request):
        url = request.POST.get("url")
        identifier = self.createLink(url)
        request.session["result"] = identifier
        return redirect("index")

    def createLink(self, url):
        try:
            link = Link.objects.get(url=url)
            return link.identifier
        except Link.DoesNotExist:
            pass
        while True:
            try:
                identifier = secrets.token_urlsafe(7)   
                Link.objects.create(identifier=identifier, url=url)
                break
            except IntegrityError:
                pass
        return identifier
        
