from django.db import migrations, models
class board(models.Model):
  title = models.Charfield('タイトル',max_length=30)
  message = models.Textfield('本文',max_length=300)
  comment = models.Textfield('コメント',max_length=150)
  created = models.Datatimefield(auto_now_add=True)
  updated = models.Datetimefield(auto_now=True)
def __str__(self):
        return self.author