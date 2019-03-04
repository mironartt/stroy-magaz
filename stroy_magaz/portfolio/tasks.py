from celery import task
from django.conf import settings
from django.core.mail import send_mail
from site_some_settings.models import SiteSettings
from portfolio.models.portfolio import Portfolio


@task
def mail_sent_create_portfolio_comment(info):
    """
        Если создан комментарий в разделе "Портфолио", то отправляется письмо на мыло клиента с подробностями о его заполнении
        И оповещение администратору на указанный емайл
    """
    site_settings = SiteSettings.objects.first()
    p_obj = Portfolio.objects.get(id=info[0])

    client_message = '{0}\n\nВАШ ОТЗЫВ:\n\nРаздел портволио в котором оставлен отзывы:    {1}\nВаш отзыв: {2}\n\nСылка на раздел с комментарием:    {3}\n\n\n{4}'.format(site_settings.mail_message_comment_create, p_obj, info[3], info[4], site_settings.mail_message_footer)
    mail_sent_client = send_mail(site_settings.mail_subject_comment_create, client_message, settings.EMAIL_HOST_USER, [info[2]])


    if site_settings.alert_new_portfolio_comments:
        if site_settings.alert_email:
            admin_email = site_settings.alert_email
        else:
            admin_email = settings.EMAIL_HOST_USER

        admin_message = 'НОВЫЙ КОМЕНТАРИЙ В РАЗДЕЛЕ "ПОРТФОЛИО".\n\nРаздел портфолио в котором был оставлен комментарий:  {0}\nФИО / Название компании того кто написал отзыв: {1}\nEmail:   {2}\nКомментарий:    {3}\n\nСылка на раздел с комментарием:   {4}\n\nРедоктирование или модерация комментария:  {5}'.format(p_obj, info[1], info[2], info[3], info[4], info[5])
        mail_sent_admin = send_mail('Новый коментарий в разделе "Портфолио"', admin_message, settings.EMAIL_HOST_USER, [admin_email])

        return mail_sent_client, mail_sent_admin
    else:
        return mail_sent_client



