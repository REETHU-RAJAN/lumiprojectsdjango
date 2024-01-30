from django.urls import path
from babyflamingo.views import SignUpView,SignInView,CatagoryCreateView,remove_category,\
sign_out_view,IndexView,ToyCreateView,ToyListView,ToyUpdateView,remove_toyview,ToyDetailView,\
DressCreateView,DressDetailView,DressListView,DressUpdateView,remove_dressview,\
StationaryCreateView,StationaryDetailView,StationaryListView,StationaryUpdateView,remove_stationaryview,\
ToyVarientCreateView,ToyVarientUpdateView,remove_toyvarientview,offertoy_delete_view,OffertoyCreateView,\
StationaryVarientCreateView,StationaryVarientUpdateView,remove_stationaryvarientview,offerstationary_delete_view,OfferstationaryCreateView,\
DressVarientCreateView,DressVarientUpdateView,remove_dressvarientview,offerdress_delete_view,OfferdressCreateView

urlpatterns = [
    path("register/",SignUpView.as_view(),name="signup"),
    path("",SignInView.as_view(),name="signin"),
    path("categories/add",CatagoryCreateView.as_view(),name="add-category"),
    path("categories/<int:pk>/remove",remove_category,name="remove-category"),
    path("logout/",sign_out_view,name="signout"),
    path("index",IndexView.as_view(),name='index'),
    path("toys/add",ToyCreateView.as_view(),name="toy-add"),
    path("toys/all",ToyListView.as_view(),name="toy-list"),
    path("toys/<int:pk>/change",ToyUpdateView.as_view(),name="toy-change"),
    path("toys/<int:pk>/remove",remove_toyview,name="toy-remove"),
    
    path("toys/<int:pk>/",ToyDetailView.as_view(),name='toy-detail'),

    path("dress/add",DressCreateView.as_view(),name="dress-add"),
    path("dress/all",DressListView.as_view(),name="dress-list"),
    path("dress/<int:pk>/change",DressUpdateView.as_view(),name="dress-change"),
    path("dress/<int:pk>/remove",remove_dressview,name="dress-remove"),
    
    path("dress/<int:pk>/",DressDetailView.as_view(),name='dress-detail'),

    path("stationary/add",StationaryCreateView.as_view(),name="stationary-add"),
    path("stationary/all",StationaryListView.as_view(),name="stationary-list"),
    path("stationary/<int:pk>/change",StationaryUpdateView.as_view(),name="stationary-change"),
    path("stationary/<int:pk>/remove",remove_stationaryview,name="stationary-remove"),
    
    path("stationary/<int:pk>/",StationaryDetailView.as_view(),name='stationary-detail'),
     path("toy/<int:pk>/tvarients/add",ToyVarientCreateView.as_view(),name="add-tvarient"),
    path("tvarients/<int:pk>/change/",ToyVarientUpdateView.as_view(),name="update-tvarient"),
    path("tvarients/<int:pk>/remove/",remove_toyvarientview,name='remove-tvarient'),
    path("tvarients/<int:pk>/offer/add",OffertoyCreateView.as_view(),name="offerst-add"),
    path("offerst/<int:pk>/remove",offertoy_delete_view,name='delete-offert'),

    path("stationary/<int:pk>/svarients/add",StationaryVarientCreateView.as_view(),name="add-svarient"),
    path("svarients/<int:pk>/change/",StationaryVarientUpdateView.as_view(),name="update-svarient"),
    path("svarients/<int:pk>/remove/",remove_stationaryview,name='remove-svarient'),
    path("svarients/<int:pk>/offer/add",OfferstationaryCreateView.as_view(),name="offerss-add"),
    path("offerss/<int:pk>/remove",offerstationary_delete_view,name='delete-offers'),

    path("dress/<int:pk>/dvarients/add",DressVarientCreateView.as_view(),name="add-dvarient"),
    path("dvarients/<int:pk>/change/",DressVarientUpdateView.as_view(),name="update-dvarient"),
    path("dvarients/<int:pk>/remove/",remove_dressview,name='remove-dvarient'),
    path("dvarients/<int:pk>/offer/add",OfferdressCreateView.as_view(),name="offersd-add"),
    path("offersd/<int:pk>/remove",offerdress_delete_view,name='delete-offers'),

]