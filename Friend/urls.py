from django.urls import path
from Friend.views import(
    send_friend_request,
    cancel_requests,
    notify_user,
    decline,
    accept,
    friendlist
)

app_name = 'Friend'

urlpatterns = [
    path('friend_request/' , send_friend_request , name='friend-request'),
    path('cancel_request/', cancel_requests ,name ='friend-request-cancel'),
    path('tdlgrklfoxxhmjapawjluirdcdlpjfhh/notify/',notify_user,name='friend-notify'),
    path('decline/<int:pk>/',decline,name='decline'),
    path('accept/<int:pk>/',accept,name='accept'),
    path('friend_list/<int:pk>',friendlist,name='friendlist')
]