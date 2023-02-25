from rest_framework import serializers
from base.models import Blog 

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = '__all__'
        
    
    def validate(self, data):
        
        if len(data['title']) < 10:
            raise serializers.ValidationError("Title must be more than 10 characters.")
        if len(data['body']) < 100:
            raise serializers.ValidationError("Blog post must be more than 1000 characters.")
        return data
    
        