from celery import task
from django.conf import settings
from django.core.mail import send_mail
from site_some_settings.models import SiteSettings



@task
def mail_sent_create_order(info):
    """
        Если заказ создан, то отправляется письмо на мыло клиента с подробностями о его заполнении
        И оповещение администратору на указанный емайл
    """
    site_settings = SiteSettings.objects.first()

    file = None
    if len(info)==7:
        file = '\nПрикреплен файл\n Сылка на файл:\n' + info[6]

    client_message = '{0}\n\nДЕТАЛИ ЗАКАЗА:\nФИО / Название компании:   {1:5}\nТелефон: {2:5}\nEmail: {3}\nТематика работ:    {4}\nОписание заказа:  {5}{6}\n\n\n{7}'.format(site_settings.mail_message_order_create, info[0], info[1], info[2], info[3], info[4], file, site_settings.mail_message_footer)
    mail_sent_client = send_mail(site_settings.mail_subject_order_create, client_message, settings.EMAIL_HOST_USER, [info[2]])


    if site_settings.alert_new_order:
        if site_settings.alert_email:
            admin_email = site_settings.alert_email
        else:
            admin_email = settings.EMAIL_HOST_USER

        admin_message = 'Новый заказ.\n\nЗаказчик:  {0}\nТелефон заказчика: {1}\nEmail заказчика:   {2}\nТематика работ:    {3}\nОписание заказа:   {4}\n\nСсылка на файл:  {5}\n\n\nРедоктирование заказа:  {6}'.format(
            info[0], info[1], info[2], info[3], info[4], file, info[5])
        mail_sent_admin = send_mail('Новый заказ', admin_message, settings.EMAIL_HOST_USER, [admin_email])

        return mail_sent_client, mail_sent_admin
    else:
        return mail_sent_client





@task
def mail_sent_create_coll_back(info):
    """
        Если создан заказ обратного звонка, то отправляется оповещение администратору на указанный емайл
    """
    site_settings = SiteSettings.objects.first()

    if site_settings.alert_email:
        admin_email = site_settings.alert_email
    else:
        admin_email = settings.EMAIL_HOST_USER

    admin_message = 'ДЕТАЛИ ЗАКАЗА ОБРАТНОГО ЗВОНКА:\nФИО / Название компании:   {0}\nТелефон: {1}\nВремя обратного звонка: {2}\nПримечания:    {3}\n\n\nРедоктирование заказа:  {4}'.format(info[0], info[1], info[2], info[3], info[4])
    mail_sent_admin = send_mail('Новый заказ обратного звонка', admin_message, settings.EMAIL_HOST_USER, [admin_email])

    return mail_sent_admin





@task
def mail_sent_create_main_comment(info):
    """
        Если создан отзыв, то отправляется письмо на мыло клиента с подробностями о его заполнении
        И оповещение администратору на указанный емайл
    """
    site_settings = SiteSettings.objects.first()
    client_message = '{0}\n\nВАШ ОТЗЫВ:\nКакие работы у вас производились:   {1}\nВаша оценка произведенным работам: {2} из 10\nВаш отзыв: {3}\n\nСылка на раздел "Отзывы":    {4}\n\n\n{5}'.format(site_settings.mail_message_comment_create, info[4], info[3], info[5], info[6], site_settings.mail_message_footer)
    mail_sent_client = send_mail(site_settings.mail_subject_comment_create, client_message, settings.EMAIL_HOST_USER, [info[1]])


    if site_settings.alert_new_main_comment:
        if site_settings.alert_email:
            admin_email = site_settings.alert_email
        else:
            admin_email = settings.EMAIL_HOST_USER

        admin_message = 'НОВЫЙ ОТЗЫВ.\n\nИмя того кто написал отзыв:  {0}\nEmail: {1}\nТелефон:   {2}\nОценка:    {3}\nКакие работы производились:   {4}\nКомментарий:   {5}\n\nСылка на раздел с комментарием:   {6}\n\n\nРедоктирование или модерация комментария:  {7}'.format(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
        mail_sent_admin = send_mail('Новый отзыв', admin_message, settings.EMAIL_HOST_USER, [admin_email])

        return mail_sent_client, mail_sent_admin
    else:
        return mail_sent_client




