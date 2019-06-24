from django.db import models

# Create your models here.

class Topic(models.Model):
    """Model representing a blog topic."""
    name = models.CharField(max_length=200, help_text='Enter a blog topic (e.g. Family Vacations)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Blogpost(models.Model):
    """Model representing a blogpost (but not a specific post of a blog)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because blogpost can only have one blogger, but blogger can have multiple blogs
    # Blogger as a string rather than object because it hasn't been declared yet in the file
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=3500, help_text='Enter a brief description of the blog')
    website = models.CharField('Website', max_length=200, help_text='200 Character <a href="https://www.website-international.org/content/what-website">Website</a>', null=True)
    
    # ManyToManyField used because topic can contain many blogs. Blogs can cover many topics.
    # Topic class has already been defined so we can specify the object above.
    topic = models.ManyToManyField(Topic, help_text='Select a topic for this blog')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this blog."""
        return reverse('blogpost-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name_plural = "Bloggers Like Me"

    def display_topic(self):
        """Create a string for the Topic. This is required to display topic in Admin."""
        return ', '.join(topic.name for topic in self.topic.all()[:3])
    
    display_topic.short_description = 'Topic'    

class Blogger(models.Model):
    """Model representing an blogger."""
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=8000)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    class Meta:
        verbose_name_plural = "My Blog Posts"



    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blogger-detail', args=[str(self.id)])

    




