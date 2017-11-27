from denotat.models import Argument, Denotat,  Attitude, Scopos, Question, Text_problematics, Dictionary, Collocation, Text,  Subject_area, Key_Words, Figure_of_speech, Sentence, Word,Research_topic
from django.contrib import admin

#from denotat.admin import custom_admin_site
admin.site.register (Argument, Denotat,  Attitude, Scopos, Question, Text_problematics, Dictionary, Collocation, Text,  Subject_area, Key_Words, Figure_of_speech, Sentence, Word,Research_topic)

#, site=custom_admin_site
