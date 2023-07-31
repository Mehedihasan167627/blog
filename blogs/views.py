from rest_framework import response,views,permissions,pagination,status 
from .models import*
from users.models import User ,Contact
from .serializers import*

class SidebarView(views.APIView):
    def get(self,request):
        user=User.objects.filter(user_type="1").last()

        contact=Contact.objects.get(author=user)
        footer={
            "gmail":contact.email,
            "phone":contact.phone,
            "address":contact.address,
        }
        follow_us={
            "facebook":{
                "link":contact.facebook_link,
                "follower":contact.facebook_follower
            },
             "twitter":{
                "link":contact.twitter_link,
                "follower":contact.twitter_follower
            },
             "linkedin":{
                "link":contact.linkedin_link,
                "follower":contact.linkedin_follower
            },
        }
        category=Category.objects.filter(status=True)
        categories=CategorySerializer(category,many=True).data


        popular_obj=Post.objects.all().order_by("-view_count")[:4]
        popular=PostSerializer(popular_obj,many=True).data

        recent_obj=Post.objects.all().order_by("-id")[:4]
        recent=PostSerializer(recent_obj,many=True).data
        
        data={
            "follow_us":follow_us,
            "categories":categories,
            "popular":popular,
            "recent":recent,
            "footer":footer
        }

        return response.Response({"data":data})


class HomeAPIView(views.APIView):
    def get(self,request):
        qs=Category.objects.filter(is_home_page_show=True).order_by("ordering")
        serializer=HomeCategorySerializer(qs,many=True)  
        is_heros=Post.objects.filter(is_hero=False)
        hero_serializer=PostSerializer(is_heros,many=True)
        return response.Response({"data":serializer.data,"is_hero":hero_serializer.data},status=status.HTTP_200_OK)
       

class PostListView(views.APIView,pagination.PageNumberPagination):
    page_size=10
    def get(self,request):
        limit=request.GET.get("limit")
        
        if limit:
            PostListView.page_size=limit 
        else:
            PostListView.page_size=10
        qs=Post.objects.order_by("-view_count")
  
        results = self.paginate_queryset(qs, request, view=self)
        serializer = PostSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    

class PostDetailAPIView(views.APIView):
    def get(self,request,slug):
        try:
           post= Post.objects.get(slug=slug)
           detail = PostSerializer(post).data 
           cmt_qs=Comment.objects.filter(post=post) 
           comments=CommentSerializer(cmt_qs,many=True).data

           return response.Response({"details":detail,"comments":comments})
        except:
            return response.Response({"erorr":"not found"})


class CreateCommentAPIView(views.APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,post_id):
        post=Post.objects.get(id=post_id)
        
        

