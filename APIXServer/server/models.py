#!/usr/bin/python
# -*- coding: utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=80, unique=True, db_column='NAME')

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    group = models.ForeignKey(AuthGroup, unique=True, db_column='GROUP_ID')
    permission = models.ForeignKey('AuthPermission', unique=True, db_column='PERMISSION_ID')

    class Meta:
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=50, db_column='NAME')
    content_type = models.ForeignKey('DjangoContentType', unique=True, db_column='CONTENT_TYPE_ID')
    codename = models.CharField(max_length=100, unique=True, db_column='CODENAME')

    class Meta:
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    password = models.CharField(max_length=128, db_column='PASSWORD')
    last_login = models.DateTimeField(db_column='LAST_LOGIN')
    is_superuser = models.SmallIntegerField(db_column='IS_SUPERUSER')
    username = models.CharField(max_length=30, unique=True, db_column='USERNAME')
    first_name = models.CharField(max_length=30, db_column='FIRST_NAME')
    last_name = models.CharField(max_length=30, db_column='LAST_NAME')
    email = models.CharField(max_length=75, db_column='EMAIL')
    is_staff = models.SmallIntegerField(db_column='IS_STAFF')
    is_active = models.SmallIntegerField(db_column='IS_ACTIVE')
    date_joined = models.DateTimeField(db_column='DATE_JOINED')

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    user = models.ForeignKey(AuthUser, unique=True, db_column='USER_ID')
    group = models.ForeignKey(AuthGroup, unique=True, db_column='GROUP_ID')

    class Meta:
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    user = models.ForeignKey(AuthUser, unique=True, db_column='USER_ID')
    permission = models.ForeignKey(AuthPermission, unique=True, db_column='PERMISSION_ID')

    class Meta:
        db_table = 'auth_user_user_permissions'


class Bgoz(models.Model):
    mynum = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    vez = models.CharField(max_length=30, blank=True)
    piszt = models.IntegerField(null=True, blank=True)
    szazalek = models.IntegerField(null=True, blank=True)
    hiba = models.IntegerField(null=True, blank=True)
    idozito = models.IntegerField(null=True, blank=True)
    ervenyes = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'Bgoz'


class Csoportok(models.Model):
    num = models.IntegerField(primary_key=True, blank=True, db_column='num')
    indx = models.IntegerField(null=True, blank=True)
    nev = models.CharField(max_length=70, blank=True, db_column='nev')
    icon = models.IntegerField(null=True, blank=True)
    sajat = models.CharField(max_length=10, blank=True)
    megj = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = '"Csoportok"'


class Dbgrid(models.Model):
    num = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    user = models.CharField(max_length=70, blank=True)
    node = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    ful = models.CharField(max_length=70, blank=True)
    ful_n = models.IntegerField(null=True, blank=True)
    sorrend = models.CharField(max_length=255, blank=True)
    grid = models.TextField(blank=True)

    class Meta:
        db_table = 'DBGrid'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    name = models.CharField(max_length=100, db_column='NAME')
    app_label = models.CharField(max_length=100, unique=True, db_column='APP_LABEL')
    model = models.CharField(max_length=100, unique=True, db_column='MODEL')

    class Meta:
        db_table = 'django_content_type'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True, db_column='SESSION_KEY')
    session_data = models.TextField(db_column='SESSION_DATA')
    expire_date = models.DateTimeField(db_column='EXPIRE_DATE')

    class Meta:
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    domain = models.CharField(max_length=100, db_column='DOMAIN')
    name = models.CharField(max_length=50, db_column='NAME')

    class Meta:
        db_table = 'django_site'


class EsCalib(models.Model):
    num = models.DecimalField(unique=True, null=True, max_digits=10, decimal_places=0, blank=True)
    nev = models.CharField(max_length=10, blank=True)
    mm = models.IntegerField(null=True, blank=True)
    lit = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    total = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    d_lit = models.FloatField(null=True, blank=True)
    delete = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'es_calib'


class Kartyak(models.Model):
    id_2 = models.DecimalField(unique=True, null=True, max_digits=10, decimal_places=0, blank=True)
    vezerlo = models.CharField(max_length=70, blank=True)
    csoport = models.IntegerField(null=True, blank=True)
    sorszam = models.IntegerField(null=True, blank=True)
    azonosito = models.CharField(max_length=20, blank=True)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    nev = models.CharField(max_length=70, blank=True)
    km_n = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    uo_n = models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)
    tipus = models.CharField(max_length=10, blank=True)
    pin = models.CharField(max_length=4, blank=True)
    max_l = models.IntegerField(null=True, blank=True)
    max_db = models.IntegerField(null=True, blank=True)
    options = models.IntegerField(null=True, blank=True)
    icon = models.IntegerField(null=True, blank=True)
    lit_ki = models.CharField(max_length=1, blank=True)
    km_b = models.CharField(max_length=1, blank=True)
    uo_b = models.CharField(max_length=1, blank=True)
    mo_b = models.CharField(max_length=1, blank=True)
    actual = models.CharField(max_length=1, blank=True)

    class Meta:
        db_table = 'Kartyak'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    app_name = models.CharField(max_length=255, db_column='APP_NAME')
    migration = models.CharField(max_length=255, db_column='MIGRATION')
    applied = models.DateTimeField(db_column='APPLIED')

    class Meta:
        db_table = 'south_migrationhistory'


class Tankolasok(models.Model):
    abs_id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0, blank=True)
    vezerlo = models.CharField(max_length=70, blank=True)
    sorszam = models.IntegerField(null=True, blank=True)
    helyszin = models.CharField(max_length=50, blank=True)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    sofor_id = models.IntegerField(null=True, blank=True)
    sofor_card = models.CharField(max_length=20, blank=True)
    sofor_nev = models.CharField(max_length=70, blank=True)
    sofor_csop = models.IntegerField(null=True, blank=True)
    gep_id = models.IntegerField(null=True, blank=True)
    gep_card = models.CharField(max_length=20, blank=True)
    gep_nev = models.CharField(max_length=70, blank=True)
    gep_csop = models.IntegerField(null=True, blank=True)
    status_c = models.CharField(max_length=40, blank=True)
    kut = models.IntegerField(null=True, blank=True)
    km = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    u_ora = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    m_lev = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    e_km = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    e_uo = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    km_n = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    uo_n = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    km_m = models.IntegerField(null=True, blank=True)
    uo_m = models.IntegerField(null=True, blank=True)
    km_n_d = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    uo_n_d = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    s_n_d = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    km_a = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    uo_a = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    hofok = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    ua_mm = models.IntegerField(null=True, blank=True)
    v_mm = models.IntegerField(null=True, blank=True)
    t_hofok = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    e_ar = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    ua_tipn = models.IntegerField(null=True, blank=True)
    tipus = models.CharField(max_length=30, blank=True)
    liter = models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)
    liter15 = models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)
    mil_a = models.DecimalField(null=True, max_digits=15, decimal_places=5, blank=True)
    status_n = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Tankolasok'


class Tlevel(models.Model):
    num = models.DecimalField(primary_key=True, decimal_places=0, max_digits=10)
    tartaly = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    ua_mm = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    h2o_mm = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    hofok = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    ua_l = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    ua_l15 = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    h2o_l = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    ua_kg = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    tipus = models.CharField(max_length=70, blank=True)
    vez = models.CharField(max_length=70, blank=True)
    kut = models.IntegerField(null=True, blank=True)
    e_ar = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    gcsop = models.IntegerField(null=True, blank=True)
    delete = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'TLevel'


class Tartalyok(models.Model):
    num = models.IntegerField(primary_key=True)
    nev = models.CharField(max_length=70, blank=True)
    helyszin = models.CharField(max_length=50, blank=True)
    icon = models.IntegerField(null=True, blank=True)
    ua_tip = models.CharField(max_length=15, blank=True)
    es = models.CharField(max_length=10, blank=True)
    es_vez = models.CharField(max_length=70, blank=True)
    p1 = models.IntegerField(null=True, blank=True)
    p1_vez = models.CharField(max_length=70, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p2_vez = models.CharField(max_length=70, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p3_vez = models.CharField(max_length=70, blank=True)
    p4 = models.IntegerField(null=True, blank=True)
    p4_vez = models.CharField(max_length=70, blank=True)
    sajat = models.CharField(max_length=10, blank=True)
    keszlet = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    keszlet15 = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    kg = models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)
    szazalek = models.CharField(max_length=10, blank=True)
    csop = models.CharField(max_length=255, blank=True)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    suruseg = models.FloatField(null=True, blank=True)
    delete = models.CharField(max_length=20, blank=True)
    zarolt_l = models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)
    zarolt_mm = models.IntegerField(null=True, blank=True)
    ua_tipn = models.IntegerField(null=True, blank=True)
    a0 = models.FloatField(null=True, blank=True)
    hofok = models.DecimalField(null=True, max_digits=5, decimal_places=1, blank=True)
    max_liter = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Tartalyok'


class User(models.Model):
    num = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0, blank=True)
    nev = models.CharField(max_length=70, blank=True)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    delete = models.CharField(max_length=20, blank=True)
    passwd = models.TextField(blank=True)
    picture = models.TextField(blank=True)
    teszt = models.TextField(db_column='Teszt', blank=True)

    class Meta:
        db_table = 'User'

    @staticmethod
    def isAuthenticated(username, password):
        #res = User.objects.get(nev=username, passwd=base64.b64encode(password))
        try:
            User.objects.get(nev=username)
            return True
        except User.DoesNotExist:
            return False


class Vezerlok(models.Model):
    abs_id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    num = models.IntegerField(null=True, blank=True)
    nev = models.CharField(max_length=70, blank=True)
    tipus = models.CharField(max_length=20, blank=True)
    sajat = models.CharField(max_length=10, blank=True)
    helyszin = models.CharField(max_length=50, blank=True)
    path = models.CharField(max_length=255, blank=True)
    icon = models.IntegerField(null=True, blank=True)
    p1 = models.IntegerField(null=True, blank=True)
    p2 = models.IntegerField(null=True, blank=True)
    p3 = models.IntegerField(null=True, blank=True)
    p4 = models.IntegerField(null=True, blank=True)
    es1 = models.CharField(max_length=10, blank=True)
    es2 = models.CharField(max_length=10, blank=True)
    es3 = models.CharField(max_length=10, blank=True)
    es4 = models.CharField(max_length=10, blank=True)
    t1 = models.CharField(max_length=20, blank=True)
    t2 = models.CharField(max_length=20, blank=True)
    t3 = models.CharField(max_length=20, blank=True)
    t4 = models.CharField(max_length=20, blank=True)
    l_tip = models.CharField(max_length=20, blank=True)
    com = models.CharField(max_length=20, blank=True)
    cim = models.CharField(max_length=20, blank=True)
    ido = models.IntegerField(null=True, blank=True)
    dl_dt = models.FloatField(null=True, blank=True)
    com_azon = models.CharField(max_length=20, blank=True)
    time_chk = models.CharField(max_length=1, blank=True)
    delete = models.CharField(max_length=20, blank=True)
    t1n = models.IntegerField(null=True, blank=True)
    t2n = models.IntegerField(null=True, blank=True)
    t3n = models.IntegerField(null=True, blank=True)
    t4n = models.IntegerField(null=True, blank=True)
    bgoz = models.CharField(max_length=20, blank=True)
    b_side_vez = models.CharField(max_length=30, blank=True)
    b_side_p = models.IntegerField(null=True, blank=True)
    p1_sz = models.IntegerField(null=True, blank=True)
    p2_sz = models.IntegerField(null=True, blank=True)
    p3_sz = models.IntegerField(null=True, blank=True)
    p4_sz = models.IntegerField(null=True, blank=True)
    p1_err = models.IntegerField(null=True, blank=True)
    p2_err = models.IntegerField(null=True, blank=True)
    p3_err = models.IntegerField(null=True, blank=True)
    p4_err = models.IntegerField(null=True, blank=True)
    p1_tmr = models.IntegerField(null=True, blank=True)
    p2_tmr = models.IntegerField(null=True, blank=True)
    p3_tmr = models.IntegerField(null=True, blank=True)
    p4_tmr = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Vezerlok'


class TreenodeModel(models.Model):
    absindx = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    user = models.CharField(max_length=70, blank=True)
    dbindx = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0, blank=True)
    parent0 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent1 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent2 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent3 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent4 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent5 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent6 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent7 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    parent8 = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    nev = models.CharField(max_length=70, blank=True)
    tipus = models.CharField(max_length=10, blank=True)
    azonosito = models.CharField(max_length=70, blank=True)
    icon = models.IntegerField(null=True, blank=True)
    p1 = models.IntegerField(null=True, db_column='P1', blank=True)
    p2 = models.IntegerField(null=True, db_column='P2', blank=True)
    p3 = models.IntegerField(null=True, db_column='P3', blank=True)
    p4 = models.IntegerField(null=True, db_column='P4', blank=True)
    delete = models.CharField(max_length=20, blank=True)
    make = models.CharField(max_length=20, blank=True)
    read_only = models.CharField(max_length=1, blank=True)

    class Meta:
        db_table = 'TreeNode'
