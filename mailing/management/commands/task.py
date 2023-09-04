import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail

from djangoProject3 import settings


from mailing.models import Mailing, MailingLog


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        now = datetime.datetime.now()
        for mailing in Mailing.objects.filter(status=Mailing.STATUS_STARTED):
            for client in mailing.client.all():
                logs = MailingLog.objects.filter(mailing=mailing, mailing__client=client)
                if logs.exists():
                    last_try_date = logs.order_by('-last_mailing_time').first()
                    if mailing.period == Mailing.PERIOD_DAILY:
                        if (now - last_try_date).days >= 1:
                            send_mail(
                                subject=mailing.theme,
                                message=mailing.message,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[client.email],
                                fail_silently=False
                            )
                    elif mailing.period == Mailing.PERIOD_WEEKLY:
                        if (now - last_try_date).days >= 7:
                            send_mail(
                                subject=mailing.theme,
                                message=mailing.message,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[client.email],
                                fail_silently=False
                            )
                    elif mailing.period == Mailing.PERIOD_MONTHLY:
                        if (now - last_try_date).days >= 30:
                            send_mail(
                                subject=mailing.theme,
                                message=mailing.message,
                                from_email=settings.EMAIL_HOST_USER,
                                recipient_list=[client.email],
                                fail_silently=False
                            )
                else:
                    send_mail(
                            subject=mailing.theme,
                            message=mailing.message,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[client.email],
                            fail_silently=False
                        )















