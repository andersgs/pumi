from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from epidata.models import Account,Epidata

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required = False)
    confirm_password = serializers.CharField(write_only = True, required = False)

    class Meta:
        model = Account
        fields = ('username', 'created_at', 'updated_at', 'first_name', 'last_name', 'password', 'confirm_password')

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                isntance.set_password(password)
                instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance

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
