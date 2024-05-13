from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from users.models import NewUser
from users.serializers import CustomUserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)

        # Lấy thông tin của người dùng từ request
        user = self.user

       # Kiểm tra xem thông tin của người dùng có tồn tại hay không
        if user:
            # Serialize thông tin người dùng bằng CustomUserSerializer
            user_serializer = CustomUserSerializer(user)
            # Thêm thông tin người dùng vào kết quả trả về
            data['user'] = user_serializer.data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
