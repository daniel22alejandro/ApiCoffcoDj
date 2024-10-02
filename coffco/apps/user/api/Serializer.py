from apps.user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password','rol',"tipo_documento",'numero_documento']

    def create(self, validated_data):
        password = validated_data.pop('password', 'None')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password','rol',"tipo_documento",'numero_documento']

        
class UserUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name']


