from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Member(models.Model):
    """ Member Model """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member"
    )

    updated_on = models.DateTimeField(auto_now=True)
    blurb = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='member_likes',
        blank=True
    )

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