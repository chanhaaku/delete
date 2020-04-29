from django.urls import path
from . import views

urlpatterns =[
				path('',views.home,name='home'),
				path('service/',views.service,name='service'),
				path('about/',views.about,name='about'),
				path('contact/',views.contact,name='contact'),
				path('post-create/',views.postview,name='post-create'),
				path('title/',views.TitleListView.as_view(),name='title'),
				path('title/<int:pk>/',views.titledetail,name='titledetail'),
				path('title/<int:pk>/delete/',views.PostDeleteView.as_view(),name='delete-post'),
				# path('<str:titlename>/delete/',views.PhotoDeleteView.as_view(),name='delete-image'),
				path('images/',views.TestListView.as_view(),name='image'),
				path('images/<int:pk>/',views.PhotoDetailView.as_view(),name='image-detail'),
				path('images/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name='delete-image'),
				

				path('ui/',views.ui,name='ui'),
				path('testnav/',views.testnav,name='nav'),
				path('collection/',views.CollectionListView.as_view(),name='collection'),
				path('collection/<int:pk>/',views.titlesdetail,name='titlesdetail'),
				
			]