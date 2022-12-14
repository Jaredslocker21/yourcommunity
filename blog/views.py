""" Views """
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Member
from .forms import CommentForm, MemberForm
from django.contrib import messages
# Create your views here.


def about(request):
    """
    renders about page
    """
    return render(request, "about.html")


def create_member(request):
    """
    renders form to create a member page
    """
    member_form = MemberForm(request.POST or None, request.FILES or None)
    context = {
        'member_form': member_form,
    }

    if request.method == "POST":
        member_form = MemberForm(request.POST, request.FILES)
        if member_form.is_valid():
            member_form = member_form.save(commit=False)
            member_form.author = request.user
            member_form.status = 1
            member_form.save()
            messages.success(request, "Your Member page is waiting approval.")
            return redirect('home')
    else:
        member_form = MemberForm()
    return render(request, "create_member.html", context)


def delete_member(request, slug):
    """
    Member delete view
    """
    member = Member.objects.get(slug=slug)

    if member.author.username != request.user.username:
        messages.error(request, "Unauthorized to delete")
        return redirect('home')

    member.delete()
    messages.success(request, "Your member page is deleted")
    return redirect('home')


# Class used from "I think therefore I blog" walkthrough.
class MemberList(generic.ListView):
    """ View code for Member Home page and site pagination """
    model = Member
    queryset = Member.objects.filter(
        status=1).filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


# Class used from "I think therefore I blog" walkthrough.
class MemberDetail(View):
    """ View code for Member Page """
    def get(self, request, slug, *args, **kwargs):
        queryset = Member.objects.filter(approved=True).filter(status=1)
        member = get_object_or_404(queryset, slug=slug)
        comments = member.comments.filter(approved=True).order_by('created_on')
        liked = False
        if member.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "member_detail.html",
            {
                "member": member,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Member.objects.filter(status=1)
        member = get_object_or_404(queryset, slug=slug)
        comments = member.comments.filter(approved=True).order_by('created_on')
        liked = False
        if member.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = member
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "member_detail.html",
            {
                "member": member,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


# This function was wirtten by me with help from a freind a my mentor
def edit_member(request, slug):
    """
    Member Edit view
    """
    member = get_object_or_404(Member, slug=slug)

    if member.author.username != request.user.username:
        messages.error(request, "Unauthorized to edit")
        return redirect('home')

    member_form = MemberForm(request.POST or None, instance=member)
    context = {
        "member_form": member_form,
        "member": member
    }
    if request.method == "POST":
        member_form = MemberForm(request.POST, request.FILES, instance=member)
        if member_form.is_valid():
            member = member_form.save(commit=False)
            member.author = request.user
            member.save()
            return redirect('home')
    else:
        member_form = MemberForm(instance=member)
    return render(request, "edit_member.html", context)


# Class used from "I think therefore I blog" walkthrough.
class MemberLike(View):
    """
    Likes on a Member
    """
    def post(self, request, slug, *args, **kwargs):
        """
        Submits to view
        """
        member = get_object_or_404(Member, slug=slug)
        if member.likes.filter(id=request.user.id).exists():
            member.likes.remove(request.user)
        else:
            member.likes.add(request.user)

        return HttpResponseRedirect(reverse('member_detail', args=[slug]))
