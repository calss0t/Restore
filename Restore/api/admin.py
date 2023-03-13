from django.contrib import admin

from api.models import User, Tick_Tack_Toe, Rock_Paper_Scissors, Mario


class UserAdmin(admin.ModelAdmin):
    pass


class Tick_Tack_ToeAdmin(admin.ModelAdmin):
    pass


class Rock_Paper_ScissorsAdmin(admin.ModelAdmin):
    pass

class MarioAdmin(admin.ModelAdmin):
    pass



admin.site.register(User, UserAdmin)
admin.site.register(Tick_Tack_Toe, Tick_Tack_ToeAdmin)
admin.site.register(Rock_Paper_Scissors, Rock_Paper_ScissorsAdmin)
admin.site.register(Mario, MarioAdmin)
