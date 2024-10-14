from django.http import HttpResponse
from django.views import generic


class PostView(generic.View):
    def get(self, resquest, *args, **kwargs):
        return HttpResponse('hell')