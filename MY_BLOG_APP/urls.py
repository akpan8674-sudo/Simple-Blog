from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'MY_BLOG_APP'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register-page'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_page, name='logout-page'),
    #path('profile/<str:username>/', views.profile, name='profile-page'),
    #path('profile/<str:username>/edit/', views.edit_profile, name='edit-profile'),
    #path('profile/<str:username>/posts/', views.user_posts, name='user-posts'),
    path('create/', views.create_post, name='create-post'),
    path('post/<int:post_id>/', views.view_post, name='view-post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit-post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete-post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add-comment'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
