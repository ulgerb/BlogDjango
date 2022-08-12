from email.policy import default
from sre_constants import CATEGORY
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

DEFAULT = 'post'
CATEGORI = (
    ('post', 'post'),
    ('software', 'yazılım'),
    ('product', 'urun'),
    ('game', 'oyun'),
    ('technology', 'teknoloji'),
    ('movie', 'film'),
)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="")
    
    # status = models.CharField(choices=CATEGORY, max_length=20, default=DEFAULT)
    image = models.ImageField(null=True, blank=True, upload_to="category")

    def __str__(self) -> str:
        return self.title



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    media = models.FileField( upload_to='', null=True, blank=True, verbose_name="Blog Resmi")
    medianame = models.CharField( max_length=100, verbose_name="media name", null=True)
    name = models.CharField( max_length=50, verbose_name="Post name")
    name2 = models.CharField( max_length=100, verbose_name="Post name2", null=True)
    textinfo = models.TextField(max_length=1000, verbose_name="Text info", null=True)
    textpost = models.TextField(verbose_name="Text post", null=True)
    dateshare = models.DateTimeField(blank=True, null=True, verbose_name="Share Date", auto_now_add=True)
    # categori = models.CharField(max_length=20, choices = CATEGORI, default = DEFAULT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) # categoriyle ilişki kuruldu
    # class_group = models.CharField(max_length=30, blank=True, null=True)
    # email = models.EmailField(blank=True, null=True)
    # year = models.IntegerField(blank=True, null=True)
    # assignments = models.ManyToManyField('Assignment', verbose_name='related assignments', blank=True, null=True)

    
    
    def __str__(self):
        return self.name
    
    # def __unicode__(self):
    #     return u'%s %s' % (self.forename, self.surname)

    class Meta:
        ordering = ['-dateshare']

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})


class CurrentPost(models.Model):
    post = models.ForeignKey(Post, verbose_name=("Popüler Post"), on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.post.name
    

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    content = models.TextField(max_length=500, verbose_name='Yorum')
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self) -> str:
        return self.name