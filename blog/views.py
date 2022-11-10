from django.shortcuts import render
from django.views import generic
from .models import Member
# Create your views here.


class MemberList(generic.ListView):
    model = Member
    queryset = Member.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8
