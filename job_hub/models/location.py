from django.db import models


class Location(models.Model):
    UKRAINE_REGIONS = [
        ('KYIV', 'Kyiv'),
        ('KHARKIV', 'Kharkiv'),
        ('LVIV', 'Lviv'),
    ]

    ABROAD_REGION = ('ABD', 'Abroad')

    location_name = models.CharField(max_length=255, choices=[ABROAD_REGION] + UKRAINE_REGIONS, default='ABD',
                                     blank=True, null=True)

    def __str__(self):
        return self.get_location_name_display()