from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'MY_BLOG_APP'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register-page'),
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout, name='logout-page'),
    path('create/', views.create_post, name='create-post'),
    path('post/<int:post_id>/', views.view_post, name='view-post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit-post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete-post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add-comment'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
