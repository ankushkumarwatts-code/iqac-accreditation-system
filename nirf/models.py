from django.db import models


class NIRFYearTarget(models.Model):

    year = models.IntegerField(unique=True)

    tlr_target = models.FloatField(default=0)

    rp_target = models.FloatField(default=0)

    go_target = models.FloatField(default=0)

    oi_target = models.FloatField(default=0)

    pr_target = models.FloatField(default=0)

    overall_target = models.FloatField(default=0)

    def __str__(self):
        return str(self.year)


class TLRIndicator(models.Model):

    year = models.ForeignKey(
        NIRFYearTarget,
        on_delete=models.CASCADE
    )

    indicator_name = models.CharField(max_length=300)

    current_value = models.FloatField(default=0)

    target_value = models.FloatField(default=0)

    def __str__(self):
        return self.indicator_name


class RPIndicator(models.Model):

    year = models.ForeignKey(
        NIRFYearTarget,
        on_delete=models.CASCADE
    )

    indicator_name = models.CharField(max_length=300)

    current_value = models.FloatField(default=0)

    target_value = models.FloatField(default=0)

    def __str__(self):
        return self.indicator_name


class GOIndicator(models.Model):

    year = models.ForeignKey(
        NIRFYearTarget,
        on_delete=models.CASCADE
    )

    indicator_name = models.CharField(max_length=300)

    current_value = models.FloatField(default=0)

    target_value = models.FloatField(default=0)

    def __str__(self):
        return self.indicator_name


class OIIndicator(models.Model):

    year = models.ForeignKey(
        NIRFYearTarget,
        on_delete=models.CASCADE
    )

    indicator_name = models.CharField(max_length=300)

    current_value = models.FloatField(default=0)

    target_value = models.FloatField(default=0)

    def __str__(self):
        return self.indicator_name


class PRIndicator(models.Model):

    year = models.ForeignKey(
        NIRFYearTarget,
        on_delete=models.CASCADE
    )

    indicator_name = models.CharField(max_length=300)

    current_value = models.FloatField(default=0)

    target_value = models.FloatField(default=0)

    def __str__(self):
        return self.indicator_name