from django.urls import path
from posts.views import RetrievePostView, ListPostView, \
    DestroyPostView, CreatePostView, UpdatePostView

urlpatterns = [
    path('', ListPostView.as_view(), name='posts'),
    path('<int:pk>', RetrievePostView.as_view(), name='post'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('delete/<int:pk>', DestroyPostView.as_view(), name='delete'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
]
