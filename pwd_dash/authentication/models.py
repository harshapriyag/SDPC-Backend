from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class SpTnstate(models.Model):
    gid = models.AutoField(primary_key=True)
    area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    perimeter = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    state_name = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.CharField(max_length=254, blank=True, null=True)
    longitude = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sp_tnstate'

class Districts(models.Model):
    gid = models.AutoField(primary_key=True)
    field_gid = models.FloatField(db_column='__gid', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    district = models.CharField(max_length=254, blank=True, null=True)
    cendcode = models.CharField(max_length=254, blank=True, null=True)
    district_c = models.CharField(max_length=50, blank=True, null=True)
    dcode = models.CharField(max_length=3, blank=True, null=True)
    cen_dcode = models.CharField(max_length=254, blank=True, null=True)
    code2011 = models.CharField(max_length=254, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'

class Blocks(models.Model):
    gid = models.AutoField(primary_key=True)
    field_gid = models.FloatField(db_column='__gid', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    district = models.CharField(max_length=254, blank=True, null=True)
    blkname = models.CharField(max_length=254, blank=True, null=True)
    drd_dcode = models.CharField(max_length=254, blank=True, null=True)
    drd_blkcod = models.CharField(max_length=254, blank=True, null=True)
    count = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    blockcode = models.CharField(max_length=254, blank=True, null=True)
    no_of_pt = models.FloatField(blank=True, null=True)
    no_of_hap = models.FloatField(blank=True, null=True)
    slno = models.FloatField(blank=True, null=True)
    dt_code = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    corr_block = models.CharField(max_length=254, blank=True, null=True)
    cat = models.CharField(max_length=254, blank=True, null=True)
    cat_2004 = models.CharField(max_length=254, blank=True, null=True)
    dt2001 = models.CharField(max_length=2, blank=True, null=True)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blocks'