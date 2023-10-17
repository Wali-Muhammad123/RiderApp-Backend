from django.contrib import admin
# Register your models here.
from users.models import *

admin.site.register(RiderUser)
admin.site.register(Rider)
admin.site.register(Customer)
admin.site.register(UserRatingModel)

