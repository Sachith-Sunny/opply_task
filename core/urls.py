from django.urls import path
# from .views import RegistrationAPI ,LoginAPI, UserAPI
# from knox import views as knox_views

# urlpatterns = [
#     path('register/', RegistrationAPI.as_view()),
#     path('login/', LoginAPI.as_view()),
#     path('user/', UserAPI.as_view()),

# ]
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]