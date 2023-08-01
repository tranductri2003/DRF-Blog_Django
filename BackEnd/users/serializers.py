from rest_framework import serializers
from users.models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    # avatar = serializers.SerializerMethodField()

    class Meta:
        model = NewUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# class UpdateNumPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = ['num_post']


# class UpdateViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = ['num_view']


# class UpdateLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = ['num_like']


# class UpdateCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NewUser
#         fields = ['num_comment']
