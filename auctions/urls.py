from django.urls import path

from . import views

app_name = "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("createListing", views.createListing, name="createListing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist_remove", views.watchlist_remove, name="watchlist_remove") 
]
