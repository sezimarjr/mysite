from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return None