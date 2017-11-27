from django.db import models


class Argument(models.Model):

        Key_Collocation = models.CharField(max_length=255)
        
class Denotat(models.Model):

        Name = models.CharField(max_length=255)
        
class Attitude(models.Model):
        
        Direction = models.CharField(max_length=255)
        Probability = models.CharField(max_length=255)
        
class Scopos(models.Model):

        The_target_audience = models.CharField(max_length=255)

class Question(models.Model):

        User_request = models.CharField(max_length=255)
         
class Text_problematics(models.Model):
        
        Objectives = models.CharField(max_length=255)
        Tasks = models.CharField(max_length=255)
        
class Dictionary(models.Model):

        Notion = models.CharField(max_length=255)
        Deskription = models.CharField(max_length=255)

class Collocation(models.Model):

        Linguistic_characteristics_collocation = models.CharField(max_length=255)
        
class Text(models.Model):

        Caption = models.CharField(max_length=255)
        Author = models.CharField(max_length=255)
        Output = models.CharField(max_length=255)
        
class Subject_area(models.Model):

        Name_area = models.CharField(max_length=255)
        Deskription_area = models.CharField(max_length=255)
        
class Key_Words(models.Model):

        Repetition_rate = models.CharField(max_length=255)
        Science_area = models.CharField(max_length=255)
        
class Figure_of_speech(models.Model):

        Linguistic_characteristics_of_speech = models.CharField(max_length=255)
        
class Sentence(models.Model):

        Linguistic_characteristics_sentence = models.CharField(max_length=255)


class Word(models.Model):

        Infinitive  = models.CharField(max_length=255)
        Linguistic_characteristics_word = models.CharField(max_length=255)
        
class Research_topic(models.Model):

        Section_science_area = models.CharField(max_length=255)
                


