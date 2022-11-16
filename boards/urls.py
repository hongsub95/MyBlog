from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/',views.BoardListView.as_view(),name="board_list"),
    path('<int:pk>/',views.BoardDetailView.as_view(),name="board_detail"),
    path("create/",views.BoardCreateView.as_view(),name="board_create"),
    path("<int:board_pk>/edit/", views.BoardUpdateView.as_view(), name="board_edit"),
    path("<int:board_pk>/delete/", views.board_delete, name="board_delete"),
    path('tag/search/',views.TagSearchView,name='tag_search')
]