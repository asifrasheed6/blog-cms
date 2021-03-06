from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

# Note that the post is deleted if:
# - The category associated with the post is deleted
# - The author of the post is deleted
class Post(models.Model):
    title = models.CharField(max_length=17) # Title of the blog post
    excerpt = models.CharField(max_length=50, null=True) # A short extract from the content
    content = models.TextField() # Body of the post
    menu_item = models.IntegerField(default=-1) # Position of post on the website menu (-1 means not in menu)
    status = models.BooleanField(default=False) # Whether the post is published or not
    featured = models.BooleanField(default=False) # Whether the post is featured or not
    page = models.BooleanField(default=False) # Whether the post is a page or not
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_on = models.DateTimeField() # when the post was published

    def __str__(self):
        return '{} by {}\n{}\nCategory: {}\nPublished on {}'.format(
            str(self.title), str(self.author), str(self.excerpt), str(self.category),
            str(self.published_on)
        )

# Comments associated to a post if deleted if the post is deleted or the user associated with the comment is deleted
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField()
    comment_content = models.CharField(max_length=100)

    def __str__(self):
        return '{}\nWritten by: {} on Post {}\nPosted on: {}'.format(
            str(self.comment_content), str(self.author), str(self.post), str(self.comment_date)
        )

# Views would help in the following:
# Find the total number of views on each post
# Find the total number of unique views of each post
# Find the number of visitors on the website based on time (do keep in mind that this would decrease if a post is deleted)
class View(models.Model):
    ipaddress = models.GenericIPAddressField(default='0.0.0.0')
    timestamp = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} visited {} on {}'.format(self.ipaddress, self.post, self.timestamp)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    cover = models.BooleanField(default=False)
    img = models.ImageField(upload_to='uploads/', null=False)
    caption = models.CharField(max_length=100, blank=True, default='')

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    constraints = [models.UniqueConstraint(fields=['user'], name='userimage')]
    img = models.ImageField(upload_to='uploads/', null=True)