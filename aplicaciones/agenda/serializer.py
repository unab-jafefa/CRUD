from rest_framework import serializers
from agenda.models import Agenda
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agenda  
        exclude = ['is_removed', 'created', 'modified']