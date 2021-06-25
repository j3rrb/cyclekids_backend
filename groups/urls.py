from django.urls import path

from groups.views import ListGroupView, DestroyGroupView, RetrieveGroupView,\
    CreateGroupView, UpdateGroupView

urlpatterns = [
    path('', ListGroupView.as_view(), name='groups'),
    path('create/', CreateGroupView.as_view(), name='create_group'),
    path('delete/<int:pk>/', DestroyGroupView.as_view(), name='delete_group'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update_group'),
    path('<int:pk>/', RetrieveGroupView.as_view(), name='get_group')
]
