from django.shortcuts import redirect
from app.models import Post
from app.serialazer import PostApi
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response



# Create your views here.
@api_view(http_method_names=['POST','GET'])
def api_page_post(req: Request):
    if req.method == 'POST':
        el = PostApi(data=req.data)
        if el.is_valid():
           el.save()
           return redirect('api_page_list')
    return Response({'msg':'Add post'})
           
    
@api_view(http_method_names=['GET'])
def api_page_list(req: Request):
    return Response({'posts': list(Post.objects.all().values())})
           

@api_view(http_method_names=['GET'])
def api_page_detail(req: Request,pk):
    db = Post.objects.get(pk=pk)
    return Response(PostApi(db).data)
           

@api_view(http_method_names=['GET','DELETE'])
def api_page_delete(req: Request,pk):
    db = Post.objects.get(pk=pk)
    if req.method == 'DELETE':
        db.delete()
        return redirect('api_page_list')
    return Response(PostApi(db).data)
           

@api_view(http_method_names=['GET','PUT'])
def api_page_put(req: Request,pk):
    db = Post.objects.get(pk=pk)
    if req.method == 'PUT':
        el = PostApi(db,data=req.data)
        if el.is_valid():
            el.save()
    return Response(PostApi(db).data)