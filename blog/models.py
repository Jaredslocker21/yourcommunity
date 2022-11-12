import string
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# another student helped me on this fx mentioned in read me


def unique_slugify(instance, slug):
    """
    creates a unique slug
    """
    model = Member
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + "-" + get_random_string(length=4)
    return unique_slug


class Member(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    user_email = models.EmailField(max_length=70, blank=True, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    blurb = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='member_likes', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    class Meta:
        """
        Dedending order the member posts in created order,
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)

    def number_of_likes(self):
        """
        Return total amount of likes on a member
        """
        return self.likes.count()
        
    def member_to_edit(self, request, slug):
        """
        Allows only the author to edit Member.
        """
        if self.author:
            return True
        else:
            return False

    def member_to_delete(self, request, slug):
        """
        Allows only the author to delete Member.
        """
        if self.author:
            return True
        else:
            return False


class Comment(models.Model):
    """Comment Model"""
    post = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)      

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"