from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import path
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account import serializers
from account.send_mail import send_confirmation_email
from like.serializers import FavoriteSerializers


from order.serializers import OrderUserSerializer



User = get_user_model()


class UserViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

    @action(['POST'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = serializers.RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email, user.activation_code)
            except Exception as e:
                print(e, '!!!!!!!!!!!!!!!!!!!!')
                return Response({'msg': 'Registered, but trouble with email',
                                 'data': serializer.data}, status=201)

            return Response(serializer.data, status=201)

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except User.DoesNotExist:
            return Response({'msg': 'Invalid link or link expired!'}, status=400)

        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({'msg': 'Successfully activated'}, status=200)

    @action(['GET'], detail=True)
    def favorites(self, request, pk):
        user = self.get_object()
        fav_posts = user.favorites.all()
        serializer = FavoriteSerializers(fav_posts, many=True)
        return Response(serializer.data, status=201)

    @action(['GET'], detail=True)
    def orders(self, request, pk):
        user = self.get_object()
        orders = user.orders.all()
        serializer = OrderUserSerializer(orders, many=True)
        return Response(serializer.data, status=201)


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny, )


class RefreshView(TokenRefreshView):
    permission_classes = (AllowAny, )

class PasswordResetAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()

        if user:
            # Генерация и сохранение токена сброса пароля для пользователя
            token = default_token_generator.make_token(user)
            user.reset_password_token = token
            user.save()

            # Формирование ссылки для сброса пароля
            HOST = 'localhost:8000'
            reset_password_url = token

            # Отправка письма со ссылкой для сброса пароля
            send_mail(
                'Сброс пароля',
                f'Вот ваш токен для сброса пароля: {reset_password_url}',
                'emarketconfirmation@gmail.com',
                [email],
                fail_silently=False,
            )
        print(token, '!!!!!!')
        return Response({'message': 'Email with password reset instructions has been sent.'}, status=status.HTTP_200_OK)

    def get(self, request):
        token = request.data.get('token')
        password = request.data.get('password')
        user = User.objects.filter(reset_password_token=token).first()
        print(user)
        print(token)
        print(password)
        if user and default_token_generator.check_token(user, token):

            # Установка нового пароля для пользователя
            user.set_password(password)
            user.reset_password_token = ''
            user.save()

            return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)