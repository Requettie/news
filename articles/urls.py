from django.urls import path
from .views import ( ArticleListView,
ArticleDetailView, Article



urlpatterns = [
    path('', Art)
    path
    path
    path
    path
]
# 1. Create an article detail view.
# 1.1. Create matching template.
# 2. Create an article create view.
# 3. Create an article update view.
# 4. Create an article delete view.
# 5. Create urlpatterns to map to all of our views.
# To view an article's detail, we're going to go to: /articles/<int:pk>/
# To create an article we're going to go to: /articles/new/
# To update an article we're going to: /articles/<int:pk>/update
# To delete an article we're going to go to: /articles/<int:pk>/delete/
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
]

#
#
#
#
## register model _