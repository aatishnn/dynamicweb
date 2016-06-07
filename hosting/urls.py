from django.conf.urls import url

from .views import DjangoHostingView, RailsHostingView, PaymentVMView,\
    NodeJSHostingView, LoginView, SignupView, IndexView, \
    OrdersHostingListView, OrdersHostingDetailView, VirtualMachinesPlanListView,\
    VirtualMachineDetailView, GenerateVMSSHKeysView, OrdersHostingDeleteView, NotificationsView, \
    MarkAsReadNotificationView

urlpatterns = [
    url(r'index/?$', IndexView.as_view(), name='index'),
    url(r'django/?$', DjangoHostingView.as_view(), name='djangohosting'),
    url(r'nodejs/?$', NodeJSHostingView.as_view(), name='nodejshosting'),
    url(r'rails/?$', RailsHostingView.as_view(), name='railshosting'),
    url(r'payment/?$', PaymentVMView.as_view(), name='payment'),
    url(r'orders/?$', OrdersHostingListView.as_view(), name='orders'),
    url(r'orders/(?P<pk>\d+)/?$', OrdersHostingDetailView.as_view(), name='orders'),
    url(r'cancel_order/(?P<pk>\d+)/?$', OrdersHostingDeleteView.as_view(), name='delete_order'),
    url(r'my-virtual-machines/?$', VirtualMachinesPlanListView.as_view(), name='virtual_machines'),
    url(r'my-virtual-machines/(?P<pk>\d+)/?$', VirtualMachineDetailView.as_view(),
        name='virtual_machines'),
    url(r'my-virtual-machines/(?P<pk>\d+)/key/?$', GenerateVMSSHKeysView.as_view(),
        name='virtual_machine_key'),
    url(r'^notifications/$', NotificationsView.as_view(), name='notifications'),
    url(r'^notifications/(?P<pk>\d+)/?$', MarkAsReadNotificationView.as_view(),
        name='read_notification'),
    url(r'login/?$', LoginView.as_view(), name='login'),
    url(r'signup/?$', SignupView.as_view(), name='signup'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout',
        {'next_page': '/hosting/login?logged_out=true'}, name='logout')
]
