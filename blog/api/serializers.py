from rest_framework import serializers
from blog.models import BlogPost

# What does a serializer do? Converts to JSON and validates data passed to the API


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):  # forms.ModelForm
    # url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'pk',
            # 'user',
            'title',
            'content',
            'timestamp',
        ]
        # read_only_fields = ['id', 'user']

    # def get_url(self, obj):
    #     # request
    #     request = self.context.get("request")
    #     return obj.get_api_url(request=request)

    # def validate_title(self, value):
    #     qs = BlogPost.objects.filter(title__iexact=value) # including instance
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise serializers.ValidationError("This title has already been used")
    #     return value
