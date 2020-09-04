from django.urls import path, include, re_path
from . import views
import bcrypt


urlpatterns = [
    #localhost:8000/buyer
    path('buyer', views.buyer_profile),
    path('seller', views.seller_profile),
    path('buyer_profile_setup/<int:user_id>', views.buyer_profile_setup),
    path('seller_profile_setup/<int:user_id>', views.seller_profile_setup),
    path('seller_profile', views.seller_profile),
    path('seller_profile_page', views.seller_profile),
    path('seller_profile_setup', views.seller_profile_setup, name="seller_profile_setup"),
    path('buyer_profile/<int:user_id>', views.buyer_profile),
    path('buyer_profile', views.buyer_profile),
    path('buyer_profile_page/', views.get_traits, name="buyer_traits"),
    path('buyer_profile_setup.html', views.traits_page, name="traits_page"),
    path('buyer_profile_setup', views.profile_setup_page, name="profile_setup_page"),
    path('buyer_profile_page', views.traits_page, name="buyer_profile_page"),
    path('send_email', views.send_email, name="send_email")
    re_path(r'^save-session-data/$', views.save_session_data, name='save_session_data'),
    re_path(r'^access-session-data/$', views.access_session_data, name='access_session_data'),
    re_path(r'^delete-session-data/$', views.delete_session_data, name='delete_session_data'),
    re_path(r'^test-delete/$', views.test_delete, name='test_delete'),
    re_path(r'^test-session/$', views.test_session, name='test_session'),
]
