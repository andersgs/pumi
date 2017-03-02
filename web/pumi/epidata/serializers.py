from rest_framework import serializers

from epidata.models import Epidata

class EpidataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epidata
        fields = ('patient_firstname', 'patient_surname', 'patient_DOB', 'patient_identifier', 'created_at', 'updated_at', 'created_by', 'creator_institution', 'creator_division')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        return Epidata.objectes.create(**validated_data)

    def update(self, instance, validated_data):
        instance.patient_firstname = validated_data.get('patient_firstname', instance.patient_firstname)
        instance.patient_surname = validated_data.get('patient_surname', instance.patient_surname)
        instance.patient_DOB = validated_data.get('patient_DOB', instance.patient_DOB)
        instance.patient_identifier = validated_data.get('patient_identifier', instance.patient_identifier)

        instance.save()

        return instance
