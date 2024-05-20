from django.urls import path
from .views import home,add_task,toogle_task,detail_task,delete_task,remove_task,edit_task,sign_up,completed,incompleted

urlpatterns = [
    path('',home,name='home'),
    path('completed_task',completed,name='completed-task'),
    path('incompleted_task',incompleted,name='incompleted-task'),
    path('add_task',add_task,name='add-task'),
    path('toogle_task/<str:task_id>',toogle_task,name='toogle_task'),
    path('detail_task/<str:task_id>',detail_task,name='detail-task'),
    path('delete_task/<str:task_id>',delete_task,name='delete_task'),
    path('remove_task/<str:task_id>',remove_task,name='remove_task'),
    path('edit_task/<str:task_id>',edit_task,name='edit_task'),
    path('sign-up',sign_up,name='sign-up'),
]
