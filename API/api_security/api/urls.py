from django.urls import path
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('',views.apiRoutes),

    path('create-user/',views.create_user),
    path('update-user/<pk>/',views.update_user),
    path('login-user/',views.login),

    path('blogs/',views.listBlogs),
    path('blog/<str:pk>/',views.showBlog),
    path('create/',views.createBlog),
    path('blog/<str:pk>/update/',views.updateBlog),
    path('blog/<str:pk>/delete/',views.deleteBlog),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]