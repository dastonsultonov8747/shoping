from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', asosiy, name='asosiy'),
                  #
                  # path('noutboklar/', noutboklar, name='noutboklar'),

                  # path('kompyuter/', kompyuterlar, name='kompyuter'),
                  #
                  # path('printer/', printer, name='printer'),

                  path('telefon/', telefon, name='telefon'),
                  #
                  # path('oyin uchun kompyuter/', oyin_uchun_kompyuter, name='oyin uchun kompyuter'),
                  #


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Geliştirme sırasında medya dosyalarını servis et
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
