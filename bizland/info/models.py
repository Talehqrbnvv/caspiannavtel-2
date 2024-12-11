from django.db import models
from ckeditor.fields import RichTextField




class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField()
    
    def __str__(self):
        return self.name



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)  

    def __str__(self):
        return self.title
    
class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='details')
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)  # Fotoğraf alanı
    title = models.CharField(max_length=200)
    description = RichTextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Detail for {self.service.title}: {self.title}"
    

class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('2g', '2G Avadanlıqlar'),  # Mevcut kategori
        ('4g', '4G Avadanlıqlar'),  # Mevcut kategori
        ('sensor', 'Sensorlar'),    # Mevcut kategori
        ('topography', 'Topoqrafiya Avadanlıqları'),  # Yeni kategori
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    detail_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=255)  
    answer = models.TextField()                    
    is_active = models.BooleanField(default=True)  

    def __str__(self):
        return self.question
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/logos/')
    url = models.URLField(max_length=200, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', '-created_at']


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


