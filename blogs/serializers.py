from rest_framework import serializers
from .models import*


class SidebarCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields=["name","post_count","name"
                ,"show_case_type","created_at",
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
        fields=[
            "id","name","slug","post_count","created_at",
        ]



class HomeCategorySerializer(serializers.ModelSerializer):
    posts=serializers.SerializerMethodField()
    class Meta:
        model=Category
        fields=[
            "id","name","slug","posts","created_at",
        ]

    def get_posts(self,obj):
        post=Post.objects.filter(category=obj,status=True).order_by("-id")[:obj.home_page_items]
        return PostSerializer(post,many=True).data 
    


class CommentSerializer(serializers.ModelSerializer):
    commented_by=serializers.CharField(source="commented_by.full_name")
    replies=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=[
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
            "replied_by",
            "comment",
            "content",
            "likes_count",
            "created_at",     
        ]
