from django.core.exceptions import ValidationError
from django.db import models


class Location(models.Model):
    UKRAINE_REGIONS = [
        ("CHERKASY", "Cherkasy"),
        ("CHERNIGIV", "Chernigiv"),
        ("CHERNIVTSY", "Chernivtsy"),
        ("CRIMEA", "Crimea"),
        ("DNEPRO", "Dnepro"),
        ("DONETSK", "Donetsk"),
        ("IVANO-FRANKIVSK", "Ivano-Frankivsk"),
        ("KHARKIV", "Kharkiv"),
        ("KHERSON", "Kherson"),
        ("KHMELNITSKY", "Khmelnitsky"),
        ("KYIV", "Kyiv"),
        ("KROPYVNYTSKYI", "Kropyvnytskyi"),
        ("LUGANSK", "Lugansk"),
        ("LVIV", "Lviv"),
        ("MYKOLAIV", "Mykolaiv"),
        ("ODESA", "Odesa"),
        ("POLTAVA", "Poltava"),
        ("RIVNE", "Rivne"),
        ("SUMY", "Sumy"),
        ("TERNOPIL", "Ternopil"),
        ("UZHHOROD", "Uzhhorod"),
        ("VINNITSIA", "Vinnitsia"),
        ("LUTSK", "Lutsk"),
        ("ZAPOROZHIA", "Zaporozhia"),
        ("ZHITOMYR", "Zhitomyr"),
    ]

    ABROAD_REGION = ("ABD", "Abroad")
    ALL_REGIONS = ("ALL REGIONS", "All regions")

    location_name = models.CharField(
        max_length=255,
        choices=[ABROAD_REGION, ALL_REGIONS] + UKRAINE_REGIONS,
        default="ALL REGIONS",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        # Check if an object with the same location_name already exists
        existing_location = Location.objects.filter(location_name=self.location_name).first()

        if existing_location:
            raise ValidationError("Location with the same name already exists.")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_location_name_display()
