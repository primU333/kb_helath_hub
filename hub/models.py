from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Home_Page_Info(models.Model):
    home_page_main_image = models.ImageField(upload_to='settings', default='default.jpg')
    home_page_main_title = models.CharField(max_length=200)
    home_page_sub_title = models.TextField()
    background_image = models.ImageField(upload_to='settings', default='default.jpg')

    home_page_intro_title = models.CharField(max_length=200)
    home_page_intro_sub_title = models.TextField(null=True)
    home_page_intro_image1 = models.ImageField(upload_to='settings', default='default.jpg')
    home_page_intro_image2 = models.ImageField(upload_to='settings', default='default.jpg')
    home_page_map_image = models.ImageField(upload_to='settings', default='default.jpg')

    advice_title = models.CharField(max_length=200)
    advice_sub_text = models.TextField()

    prevention_title = models.CharField(max_length=200)
    prevention_sub_text = models.TextField()

    def __str__(self):
        return 'Home Page Info'
    

class Home_Stats(models.Model):
    active_cases = models.IntegerField(default=0)
    recovered_cases = models.IntegerField(default=0)
    death_cases = models.IntegerField(default=0)
    treated_cases = models.IntegerField(default=0)

    def __str__(self):
        return 'Home Page Stats'
    

class About_Us_Page_Info(models.Model):
    about_us_title_sub_text = models.TextField()
    about_us_introduction_title = models.CharField(max_length=200)
    about_us_introduction_subtext = models.TextField()
    about_us_introduction_image = models.ImageField(upload_to='settings', default='default.jpg')
    background_image = models.ImageField(upload_to='settings', default='default.jpg')

    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()

    about_us_objectives_image = models.ImageField(upload_to='settings')

    consultation_sub_text = models.TextField()

    def __str__(self):
        return 'About us page settings'
    

class Team_Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='team')

    def __str__(self):
        return self.name
    
    
class Objective(models.Model):
    objective = models.TextField()

    def __str__(self):
        return self.objective
    
    
class Advice(models.Model):
    advice = models.CharField(max_length=30)

    def __str__(self):
        return self.advice
    


class Prevention_Method(models.Model):
    method_name = models.CharField(max_length=30)
    method_image = models.ImageField(upload_to='prevention_methods')
    method_description = models.TextField()

    def __str__(self):
        return self.method_name
    


class Testimonial(models.Model):
    testimony = models.TextField()
    submited_by_name = models.CharField(max_length=100)
    submited_by_image = models.ImageField(upload_to='testionials', default='default.jpg')

    def __str__(self):
        return self.submited_by_name
    

class Contact_Us_Page_Info(models.Model):
    contact_us_title_sub_text = models.TextField()
    background_image = models.ImageField(upload_to='settings', default='default.jpg')
    map_link = models.URLField(null=True, blank=True)
    contact_mail = models.EmailField(null=True)
    contact_phone = models.CharField(max_length=100, null=True)
    contact_fax = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    def __str__(self):
        return 'Contact Us Pagee Info'
    

class Contact_Us_Message(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
    


class New(models.Model):
    image = models.ImageField(upload_to='news', default='default.jpg')
    title = models.CharField(max_length=200)
    headline = models.TextField()
    detail = HTMLField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class News_Comment(models.Model):
    news = models.ForeignKey(New, on_delete=models.CASCADE, related_name="comments")
    user_email = models.EmailField()
    user_name = models.CharField(max_length=200)
    user_photo = models.ImageField(upload_to='users', default='default.jpg')
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    

    