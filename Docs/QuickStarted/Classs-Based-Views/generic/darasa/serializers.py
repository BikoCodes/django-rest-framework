from rest_framework import serializers
from .models import Darasa, LANGUAGE_CHOICES, STYLE_CHOICES


class DarasaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


    def create(self, validated_data):
        """
        Create and return a new `Darasa` instance, given the validated data.
        """
        return Darasa.objects.create(**validated_data)
                                
    def update(self, instance, validated_data):
        """
        Update and return an existing `Darasa` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        
        return instance

class DarasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Darasa
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']