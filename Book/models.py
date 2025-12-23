from django.db import models

class Books(models.Model):
    Book_Genre=(
        ("FA", "Fantasy"),
        ("AC", "Action"),
        ("HO", "Horror")
    )
    Ages=(
        ("CH","children"),
        ("TE","Teens"),
        ("AD","Adult")

    )
    name = models.CharField(max_length=30)
    year = models.DateField()
    genres = models.CharField(max_length=2,choices=Book_Genre)
    Age_group= models.CharField(max_length=2,choices=Ages)
    def __str__(self):
        return self.name


