from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import MailingListView, MailingCreateView, MailingDetailView, MailingUpdateView, MailingDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='homepage'),
    path('create/', MailingCreateView.as_view(), name='create_mailing'),
    path('view/<int:pk>', MailingDetailView.as_view(), name='view_mailing'),
    path('edit/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
]
