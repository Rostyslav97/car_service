from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()



class CreateUserAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer