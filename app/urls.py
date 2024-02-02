from django.urls import path
from app.views import api_page_list,api_page_post,api_page_detail,api_page_delete,api_page_put

urlpatterns = [

    path('api/', api_page_list, name='api_page_list'),
    path('api/post', api_page_post, name='api_page_post'),
    path('api/detail/<int:pk>', api_page_detail, name='api_page_detail'),
    path('api/delete/<int:pk>', api_page_delete, name='api_page_delete'),
    path('api/put/<int:pk>', api_page_put, name='api_page_put'),

]
