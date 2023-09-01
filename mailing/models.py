from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):

    email = models.EmailField(verbose_name='почта', unique=True)
    full_name = models.CharField(verbose_name='ФИО', max_length=250)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.full_name} {self.email}'


class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц')
    )

    STATUS_CREATED = 'created'
    STATUS_FINISHED = 'done'
    STATUS_STARTED = 'started'

    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_FINISHED, 'Завершена'),
    )

    mailing_time = models.DateTimeField(verbose_name='время рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='периодичность')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус')

    theme = models.CharField(max_length=150, verbose_name='тема', default='No theme')
    message = models.TextField(verbose_name='текст письма')

    client = models.ManyToManyField(Client, max_length=150, verbose_name='клиент')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def __str__(self):
        return f"{self.theme}, {self.period}, {self.status}, {self.client}"


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    last_mailing_time = models.DateTimeField(verbose_name='Последняя попытка')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус попытки')
    mailing = models.ForeignKey(Mailing, max_length=150, verbose_name='рассылка', on_delete=models.CASCADE)
    error_message = models.TextField(verbose_name='текст ошибки')

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'

    def __str__(self):
        return f"{self.mailing}, {self.status}, {self.last_mailing_time}"





