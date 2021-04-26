from rest_framework import serializers
from .models import Lead


# Lead Seralizer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
