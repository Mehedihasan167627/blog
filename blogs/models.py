from django.db import models
from users.models import User 
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.utils.text import slugify
import random 


class BaseEntity(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True 


class Category(BaseEntity):
    name=models.CharField(max_length=255,unique=True)
    show_case_type=models.CharField(max_length=255,choices=(
        ("Left One big right 4 List","Left One big right 4 List"),
        ("One Row Three Column Grid","One Row Three Column Grid"),
        ("Row Single Grid","Row Single Grid"),
        ("Top One Big Bottom 3 Column","Top One Big Bottom 3 Column")
    )) 
    ordering=models.PositiveBigIntegerField() 
   
    slug=models.SlugField(blank=True,null=True) 
    home_page_items=models.PositiveBigIntegerField(default=5) 
    is_home_page_show=models.BooleanField(default=True)
    ordering=models.PositiveBigIntegerField(default=0) 
    status=models.BooleanField(default=True)



    def __str__(self) -> str:
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)+"-"+str(random.randint(11111,9999999999))

        return super().save(*args,**kwargs)
    @property
    def post_count(self):
        return Post.objects.filter(category__id=self.id).count() 
    





    def __str__(self) -> str:
        return self.name 
    
class Post(BaseEntity):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=255) 
    thumbnail=models.ImageField(upload_to="media/blogs")
    description=RichTextUploadingField()
    tags=TaggableManager()
    slug=models.SlugField(blank=True,null=True)
    is_hero=models.BooleanField(default=False) 
   
    view_count=models.PositiveBigIntegerField(default=0) 
    is_popular=models.BooleanField(default=False)
    status=models.BooleanField(default=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE) 




    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)+"-"+str(random.randint(11111,9999999999))

        return super().save(*args,**kwargs)
  

    def __str__(self) -> str:
        return self.title 
    
    @property
    def tag_list(self):
        tags=self.tags.all()
        return [tag.name for tag in tags]
    

class Comment(BaseEntity):
    post=models.ForeignKey(Post,on_delete=models.CASCADE) 
    content=models.TextField()
    likes=models.ManyToManyField(User,related_name="likes",blank=True) 
    
    slug=models.SlugField(blank=True,null=True)
    commented_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.content)+"-"+str(random.randint(11111,9999999999))

        return super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.content
    
    @property
    def likes_count(self):
        return self.likes.count()
    

class ReplyComment(BaseEntity):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE) 
    content=models.TextField()
    reply_likes=models.ManyToManyField(User,related_name="reply_likes",blank=True) 
    slug=models.SlugField(blank=True,null=True)
    replied_by=models.ForeignKey(User,on_delete=models.CASCADE) 

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.content)+"-"+str(random.randint(11111,9999999999))

        return super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.content
    
    @property
    def likes_count(self):
        return self.reply_likes.count()




