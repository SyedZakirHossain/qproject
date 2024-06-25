from django.db import models

class Translator(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sura(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Sura {self.number}: {self.name}"

class Verse(models.Model):
    sura = models.ForeignKey(Sura, on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.TextField()
    translator = models.ForeignKey(Translator, on_delete=models.CASCADE)
    arabik=models.CharField(max_length=3000)
    buchcharon=models.CharField(max_length=3000)
    
    def __str__(self):
        return f"{self.sura.name} - Verse {self.number} ({self.translator.name})"
