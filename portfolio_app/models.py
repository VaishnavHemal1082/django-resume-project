from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    tech_stack = models.CharField(max_length=50, help_text = "comma-seprated values e.g, Django, MySql, Bootstrap")
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="project_image/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('ml', 'Machine Learning'),
        ('tools', 'Tools'),
    ]

    LEVEL_CHOICES = [
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
    ]

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon_class = models.CharField(
        max_length=50,
        help_text="Devicon class, e.g. devicon-python-plain"
    )
    proficiency = models.IntegerField(choices=LEVEL_CHOICES, default=2)

    def __str__(self):
        return self.name

    def proficiency_percent(self):
        return self.proficiency * 25
    


class About(models.Model):
    bio = models.TextField(help_text="Short paragraph about yourself")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "About Info"
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"