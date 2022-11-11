from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Member
# Create your views here.


class MemberList(generic.ListView):
    """ View code for Member Home page and site pagination """
    model = Member
    queryset = Member.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class MemberDetail(View):
    """ View code for Member Page """
    def get(self, request, slug, *args, **kwargs):
        queryset = Member.objects.filter(status=1)
        member = get_object_or_404(queryset, slug=slug)
        comments = member.comments.filter(approved=True).order_by('created_on')
        liked = False
        if member.likes(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'member_detail.html',
            {
                "member": member,
                "comments": comments,
                "commented": False,
                "liked": liked,
                #"comment_form": CommentForm(),
                #"member_form": MemberForm(),
            }
        )     
