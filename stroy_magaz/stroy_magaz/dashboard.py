from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    """Настройки админки"""

    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Дополнительно'),
            children=[
                {
                    'title': _('Документация по использованию сайта'),
                    'url': '/admin-detail/documentations/',
                    'external': True,
                },
                {
                    'title': _('Примерная статистика'),
                    'url': '/admin-detail/statistics/',
                    'external': True,
                },

            ],
            column=0,
            order=0
        ))

        self.children.append(modules.ModelList(
            _('Настройки'),
            models=(
                'site_some_settings.SiteSettings',

                'others.AboutUs',
                'others.CollBack',
                'others.Documentation',
                'others.Faq',
                'others.HomePageText',
                'others.MainSlider',
                'others.Partners',

                # 'service.*'
            ),
            column=0,
            order=0
        ))
        self.children.append(modules.ModelList(
            _('Коментарии и отзывы'),
            models = (
                'others.MainComments',
                'service.ServiceComments',
                'service.KindWorksComments',
                'portfolio.PortfolioComments',

                # 'service.*'
            ),
            column=0,
            order=0
        ))
        self.children.append(modules.ModelList(
            _('Раздел работ и услуг'),
            models = (
                'service.Images',
                'service.KindWorks',
                'service.Service',
            ),
            column=1,
            order=0
        ))
        self.children.append(modules.ModelList(
            _('Раздел портфолио'),
            models = (
                'portfolio.Images',
                'portfolio.Topic',
                'portfolio.Portfolio',

                # 'service.*'
            ),
            column=1,
            order=0
        ))
        self.children.append(modules.ModelList(
            _('Заказы'),
            models = (
                'others.CollBackClient',
                'others.Order',
            ),
            column=2,
            order=0
        ))



