from project import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.contact,name='about'),
    path('class',views.Myview.as_view(),name='cl'),
    path('greeting',views.AnotherGreeting.as_view(),name='greet'),
    #Test Paths
    path('publishers/', views.PublisherListView.as_view()),
    path('publisherdetail/', views.PublisherDetailView.as_view()),
    path('book/',views.BookListView.as_view()),
    path("author/add/", views.AuthorCreateView.as_view(), name="author-add"),
    path("author/<int:pk>/", views.AuthorUpdateView.as_view(), name="author-update"),
    path("author/<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="author-delete"),
    path('author/',views.AuthorListView.as_view,name='author-detail')
]
