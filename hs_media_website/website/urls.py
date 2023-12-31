from django.urls import path
from website.views import SignUpView, ProfileView,HomeView
from website import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path("contact",views.contact, name='contact'),
    path('startcontract', views.UploadFile, name='startcontract'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)