from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.conf import settings
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import Group, User
from django.utils import timezone
from django_countries.fields import CountryField


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at  = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        return super().save(*args, **kwargs)
    

# about fun olympic
class AboutFunOlympic(TimeStamp):
    title               = models.CharField(max_length=150)
    content             = models.TextField()
    address             = models.TextField(blank=True,null=True)
    logo                = models.ImageField(upload_to='pics/logo',blank=True,null=True)
    fb_link             = models.CharField(max_length=200,blank=True,null=True)
    instagram_link      = models.CharField(max_length=200,blank=True,null=True)
    youtube_link        = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:130]

    class Meta:
        verbose_name_plural = "About fun olympic"


# news model
class News(TimeStamp):
    title     = models.CharField(max_length=100)
    slug      = models.SlugField(null=True, blank=True, unique=True)
    content   = models.TextField()
    image     = models.ImageField(upload_to='pics/news')
    featured  = models.BooleanField(default=False, null=True, blank=True, verbose_name='Show on home page ??')
    author    = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    views     = models.PositiveIntegerField(default=0,null=True, blank=True)

    class Meta:
        verbose_name_plural = "News"

    def timestamp_pretty(self):
        return self.created_at.strftime('%b %e, %Y')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absoulate_url(self):
        return reverse('core:news_detail',kwargs ={
            'slug':self.slug
        })


# country model
class Country (TimeStamp):
    country = CountryField(blank=False, null=False, blank_label="Select Country")

    def __str__(self):
        return str(self.country)
    
    class Meta:
        verbose_name_plural = "Participant Country"
    


# stand model
class Standing (TimeStamp):
    title         = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# sports model
class Sport(TimeStamp):
    title         = models.CharField(max_length=200)
    display_image = models.ImageField(upload_to='pics/sports')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sports Category"



# athletics model
class Player(TimeStamp):
    sport_category  = models.ForeignKey(Sport, on_delete=models.CASCADE,null=True, blank=True)
    name            = models.CharField(max_length=200)
    image           = models.ImageField(upload_to='pics/player',null=True, blank=True)
    standing        = models.OneToOneField(Standing, null=True, blank=True, on_delete=models.CASCADE)
    country         = models.OneToOneField(Country, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Player"


# video hightlight
class Highlight(TimeStamp):
    sport_category = models.ForeignKey(Sport, on_delete=models.CASCADE,null=True, blank=True)
    title          = models.CharField(max_length=255)
    description    = models.TextField(null=True, blank=True)
    video          = EmbedVideoField(blank=True,null=True)
    country        = models.ManyToManyField(Country, blank=True, verbose_name="Participating Countries")

    def __str__(self):
        return self.title
    


# video hightlight
class LiveMatch(TimeStamp):
    sport_category = models.ForeignKey(Sport, on_delete=models.CASCADE,null=True, blank=True)
    title          = models.CharField(max_length=255)
    description    = models.TextField(null=True, blank=True)
    video_url      = EmbedVideoField(null=False, blank=False)
    venue_name     = models.CharField(max_length=255, verbose_name="Venue Name")
    country        = models.ManyToManyField(Country, blank=True, verbose_name="Participating Countries")

    def __str__(self):
        return self.title
    

# game fixtures
class Fixture(TimeStamp):
    first_participant  = models.CharField(max_length=200,verbose_name='Particant Name')
    second_participant = models.CharField(max_length=200, verbose_name='Particant Name')
    date               = models.DateField(null=True, blank=True, verbose_name='Game Date')
    sport_category     = models.ForeignKey(Sport, on_delete=models.CASCADE,null=True, blank=True)
    venue_name     = models.CharField(max_length=255, verbose_name="Venue Name",null=True, blank=True)