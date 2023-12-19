from rest_framework.serializers import ModelSerializer
from posts.models import Posts

class PostSeralizer (ModelSerializer):
    class Meta:
        model=Posts #Modelo que usará
        fields = ["title", "description", "order", "created_at"] #Compos que usará
        




