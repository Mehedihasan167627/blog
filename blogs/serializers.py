from rest_framework import serializers
from .models import*


class SidebarCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=[
            "id",
            "name",
            "show_case_type",
            "slug",
            "home_page_items",
            "is_home_page_show",
            "ordering",
        ]


class PostSerializer(serializers.ModelSerializer):
    posted_by=serializers.CharField(source="posted_by.full_name")
    category=serializers.CharField(source="category.name")
    class Meta:
        model=Post 
        fields="__all__" 



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields="__all__"



class HomeCategorySerializer(serializers.ModelSerializer):
    posts=serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields=[
            "id",
            "name",
            "show_case_type",
            "slug",
            "home_page_items",
            "is_home_page_show",
            "ordering",
        ]

    def get_posts(self,obj):
        post=Post.objects.filter(category=obj,status=True,is_hero=False).order_by("-id")[:obj.home_page_items]
        return PostSerializer(post,many=True).data 
    


class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.CharField(source="commented_by.full_name")
    replies=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=[
            "id",
             "commented_by",
            "content",
            "likes_count",
            "created_at",
            "replies"
            
        ]
    
    def get_replies(self,obj):
        rply=ReplyComment.objects.filter(comment=obj)
        return CommentReplySerializer(rply,many=True).data


class CommentReplySerializer(serializers.ModelSerializer):
    replied_by=serializers.CharField(source="replied_by.full_name")
    class Meta:
        model=ReplyComment
        fields=[
            "id",
            "replied_by",
            "comment",
            "content",
            "likes_count",
            "created_at",     
        ]
