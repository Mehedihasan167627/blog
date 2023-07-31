from django.db import models
from users.models import User 
from ckeditor_uploader.fields import RichTextUploadingField

class BaseEntity(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        abstract=True

class Information(BaseEntity):
    icon_image=models.ImageField(upload_to="media")
    icon_name=models.CharField(max_length=255)
    top_heading=models.CharField(max_length=255,blank=True,null=True)
    top_bio=RichTextUploadingField(blank=True,null=True) 
    about_me=RichTextUploadingField(blank=True,null=True)
    get_to_know=models.TextField(blank=True,null=True) 

class MySkill(BaseEntity):
    teck_name=models.CharField(max_length=255)
    perchange=models.PositiveBigIntegerField()
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="media",blank=True,null=True)


class Portfolio(BaseEntity):
    project_name=models.CharField(max_length=1000)
    thumbnail=models.ImageField(upload_to="media")
    short_description=RichTextUploadingField()
    live_link=models.URLField()
    full_description=RichTextUploadingField() 
    uses_tools=models.CharField(max_length=1000) 

    def __str__(self) -> str:
        return self.project_name


