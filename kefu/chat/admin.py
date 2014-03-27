#admin.py


from django.contrib import admin

from chat.models import *


admin.site.register(chat_user)
admin.site.register(Contact)

