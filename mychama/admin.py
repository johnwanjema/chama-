from django.contrib import admin
from .models import Individual,Group,Group_member,Group_contribution,Individual_contribution

# Register your models here.
admin.site.register(Individual)
admin.site.register(Group)
admin.site.register(Group_member)
admin.site.register(Group_contribution)
admin.site.register(Individual_contribution)
