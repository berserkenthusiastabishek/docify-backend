from django_elasticsearch_dsl_drf.serializers import DocumentSerializer, CharField, BooleanField
from django_elasticsearch_dsl import Document
from rest_framework import serializers
from docsapp.models.editable import Editable
from docsapp.documents.editable import EditableDocument
from docsapp.models.user import Profile
from docsapp.models.tag import Tag

class EditableDocumentSerializer(DocumentSerializer):
    class Meta:
        document = EditableDocument
        fields = (
            # 'content',
            # 'creation_time',
            # 'owner',
            # 'comments',
            'title',
            'id',
            'read_tags',
            'write_tags',
            'slug',
        )

class EditableSerializer(serializers.ModelSerializer):
    read_tags = serializers.SlugRelatedField(many=True, required = False, slug_field='name', queryset=Tag.objects.all())
    write_tags = serializers.SlugRelatedField(many=True, required = False, slug_field='name', queryset = Tag.objects.all())
    # creator = serializers.SlugRelatedField(required = False, slug_field='slug', queryset = Profile.objects.all())
    # comments = serializers.StringRelatedField(many=True, required = False)
    class Meta:
        model = Editable
        fields = ['title', 'id', 'read_tags', 'write_tags','slug', 
                #   'creator'
                  ]


