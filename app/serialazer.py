from rest_framework.serializers import ModelSerializer
from app.models import Post



class PostApi(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'