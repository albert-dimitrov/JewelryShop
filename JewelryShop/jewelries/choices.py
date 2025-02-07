from django.db import models


class CategoryChoices(models.TextChoices):
    RING = "Rings", "Rings"
    NECKLACE = "Necklaces", "Necklaces"
    EARRING = "Earrings", "Earrings"
    BRACELET = "Bracelets", "Bracelets"
    ANKLET = "Anklets", "Anklets"
    BROOCH = "Brooches & Pins", "Brooches & Pins"
    CHARMS = "Charms", "Charms"
    SET = "Jewelry Sets", "Jewelry Sets"
    WATCH = "Watches", "Watches"
