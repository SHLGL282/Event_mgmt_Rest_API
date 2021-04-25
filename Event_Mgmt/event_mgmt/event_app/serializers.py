from django.contrib.auth.models import User
from event_app.models import EventMaster, CategoryMaster
from rest_framework import serializers

'''
class EventMasterSerializer(serializers.HyperlinkedModelSerializer):
    category_name=serializers.StringRelatedField()
    #category_name=serializers.HyperlinkedRelatedField(read_only=True, view_name='category-view', lookup_field='category_name')
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     cate_name = validated_data.get("category_name")
    #     rslt = CategoryMaster.objects.filter(category_name=cate_name).first()
    #     validated_data["category_name"] = rslt
    #     return EventMaster.objects.create(**validated_data)

    class Meta:
        model = EventMaster
        fields = ['id', 'event_name', 'place', 'time', 'duration', 'cast', 'category_name']
'''
# HyperlinkedModelSerializer
class EventMasterSerializer(serializers.ModelSerializer):
    #category_name=serializers.StringRelatedField()
    #tracks=serializers.StringRelatedField()
    #category_name = serializers.RelatedField(source='CategoryMaster.category_name', read_only=True)
    class Meta:
        model = EventMaster
        #fields = '__all__'
        fields = ['event_name', 'place', 'time', 'duration', 'cast', 'category_name']

class CategoryMasterSerializer(serializers.ModelSerializer):
    #category_name=serializers.StringRelatedField()
    class Meta:
        model = CategoryMaster
        fields = ['category_name', 'parent_category']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
