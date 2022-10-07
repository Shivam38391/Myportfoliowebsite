import email
from email.policy import default
from django.db import models 
from django.forms import DateInput

# Create your models here.

#profile table

class Profile(models.Model):
    """Model definition for Profile."""
    profile_pic = models.ImageField(upload_to= 'profile/' )
    fullname = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    cv = models.FileField(upload_to= 'profile/cv/', max_length=100)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.fullname
    
    #about table
    
class About(models.Model):
    """Model definition for About."""
    short_bio = models.CharField(max_length=50)
    long_bio = models.CharField(max_length=250)
    
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    language = models.CharField(max_length=50)


    # TODO: Define fields here

    class Meta:
        """Meta definition for About."""

        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        """Unicode representation of About."""
        return self.short_bio


    
class Skill(models.Model):
    """Model definition for Skill."""
    name_of_skill = models.CharField(max_length=50)
    pct= models.CharField( max_length=10)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Skill."""

        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        """Unicode representation of Skill."""
        return self.name_of_skill



    

#porfolio project section............................😜
class Webdevelopment(models.Model):
    """Model definition for Webdevelopment."""
    image = models.ImageField(upload_to='portfolio/project1')
    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    link = models.CharField(max_length=150)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Webdevelopment."""

        verbose_name = 'Webdevelopment'
        verbose_name_plural = 'Webdevelopments'

    def __str__(self):
        """Unicode representation of Webdevelopment."""
        return self.project_name


#personal projects...
class Personal(models.Model):
    """Model definition for Personal."""
    image = models.ImageField(upload_to='portfolio/project1')
    project_name = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    link = models.CharField(max_length=150, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Personal."""

        verbose_name = 'Personal'
        verbose_name_plural = 'Personals'

    def __str__(self):
        """Unicode representation of Personal."""
        return self.project_name
    
    
    
class SefPhotograph(models.Model):
    """Model definition for SefPhotograph."""
    image = models.ImageField(upload_to='portfolio/project1')
    photo_name = models.CharField(max_length=20)
    photo_caption = models.CharField(max_length=100)
    link = models.CharField(max_length=150, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for SefPhotograph."""

        verbose_name = 'SefPhotograph'
        verbose_name_plural = 'SefPhotographs'

    def __str__(self):
        """Unicode representation of SefPhotograph."""
        return self.photo_name

# WORK EXPERIENCE..................
class Experience(models.Model):
    """Model definition for Experience."""
    company_name = models.CharField( max_length=40)
    start_date = models.DateField()
    
    end_date = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    responsibility = models.TextField(blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Experience."""

        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        """Unicode representation of Experience."""
        return self.company_name


#EDUCATION......
class Education(models.Model):
    """Model definition for Education."""
    qualification = models.CharField( max_length=40)
    start_date = models.DateField()
    
    end_date = models.CharField(max_length=30)
    degree = models.CharField(max_length=40)
    institute = models.CharField(max_length=60)
    descriptions = models.TextField(blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Education."""

        verbose_name =  'Education'
        verbose_name_plural =  'Educations'

    def __str__(self):
        """Unicode representation of Education."""
        return self.degree


# references .............
class Reference(models.Model):
    """Model definition for Reference."""
    image = models.ImageField(upload_to='reference/')
    name_of_refer = models.CharField(max_length=50)
    designation_refer = models.CharField(max_length=50)
    words_of_refer = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Reference."""

        verbose_name = 'Reference'
        verbose_name_plural = 'References'

    def __str__(self):
        """Unicode representation of Reference."""
        return self.name_of_refer


#contact..
class Contact(models.Model):
    """Model definition for Contact."""
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField( max_length=100)
    message = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.fullname

#social media link
class SocialMedia(models.Model):
    """Model definition for SocialMedia."""
    Facbook_link = models.CharField(max_length=50)
    Instagram_link = models.CharField(max_length=50)
    Linkedin_link = models.CharField(max_length=50)

    Google_link = models.CharField(max_length=50)


    # TODO: Define fields here

    class Meta:
        """Meta definition for SocialMedia."""

        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'

    def __str__(self):
        """Unicode representation of SocialMedia."""
        return self.Linkedin_link
