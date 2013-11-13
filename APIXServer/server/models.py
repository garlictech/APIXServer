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
from __future__ import unicode_literals
import base64
import os

from django.db import models
from django.conf import settings
import decimal
from PIL import Image
import StringIO


def ExecuteRawQuery(objects, queryString, titleId, exclude=[]):
        data = []
        result = objects.raw(queryString)
        columnNames = result.columns[:]

        for i in exclude:
            try:
                columnNames.remove(i)
            except ValueError:
                print "Column %s cannot be found" %i

        for p in result:
            subset = []

            for column_name in columnNames:
                s1 = unicode(column_name, errors='replace')
                s2 = getattr(p, column_name)

                if type(s2) is str:
                    s2 = s2.decode("windows-1250")
                elif type(s2) is decimal.Decimal:
                    s2 = str(s2)

                subset.append([s1, "", s2])

            data.append(subset)

        return {
            "desc": {
                "title_id": titleId,
                "text_id": True
            },

            "data": data
        }


def GenerateTemperatureString(tableId, temperatureField, isMetric):
    return '%s."%s"' % (tableId, temperatureField) if isMetric == "1" else '(((%s."%s")*9)/5)+32 as "%s"' % (tableId, temperatureField, temperatureField)


def GenerateParentString(node):
    parentStr = ""

    node = "-1"
    for i in range(0, 9):
        parentStr += '("parent%d"=%s) or ' % (i, node)

    return parentStr


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    name = models.CharField(max_length=80, unique=True, db_column='NAME')  # Field name made lowercase.
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    group = models.ForeignKey(AuthGroup, unique=True, db_column='GROUP_ID') # Field name made lowercase.
    permission = models.ForeignKey('AuthPermission', unique=True, db_column='PERMISSION_ID') # Field name made lowercase.
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=50, db_column='NAME') # Field name made lowercase.
    content_type = models.ForeignKey('DjangoContentType', unique=True, db_column='CONTENT_TYPE_ID') # Field name made lowercase.
    codename = models.CharField(max_length=100, unique=True, db_column='CODENAME') # Field name made lowercase.
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    password = models.CharField(max_length=128, db_column='PASSWORD') # Field name made lowercase.
    last_login = models.DateTimeField(db_column='LAST_LOGIN') # Field name made lowercase.
    is_superuser = models.SmallIntegerField(db_column='IS_SUPERUSER') # Field name made lowercase.
    username = models.CharField(max_length=30, unique=True, db_column='USERNAME') # Field name made lowercase.
    first_name = models.CharField(max_length=30, db_column='FIRST_NAME') # Field name made lowercase.
    last_name = models.CharField(max_length=30, db_column='LAST_NAME') # Field name made lowercase.
    email = models.CharField(max_length=75, db_column='EMAIL') # Field name made lowercase.
    is_staff = models.SmallIntegerField(db_column='IS_STAFF') # Field name made lowercase.
    is_active = models.SmallIntegerField(db_column='IS_ACTIVE') # Field name made lowercase.
    date_joined = models.DateTimeField(db_column='DATE_JOINED') # Field name made lowercase.
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user = models.ForeignKey(AuthUser, unique=True, db_column='USER_ID') # Field name made lowercase.
    group = models.ForeignKey(AuthGroup, unique=True, db_column='GROUP_ID') # Field name made lowercase.
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    user = models.ForeignKey(AuthUser, unique=True, db_column='USER_ID') # Field name made lowercase.
    permission = models.ForeignKey(AuthPermission, unique=True, db_column='PERMISSION_ID') # Field name made lowercase.
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

    @staticmethod
    def Details(fromDate, toDate, controllerNum, pistolNum):
        queryString= '''SELECT * from "Bgoz" where ("dt_num">=%s)and("dt_num"<%s)and("vez"='%s')and("piszt"=%s) and ("ervenyes"<>'') order by "dt_num";''' % (fromDate, toDate, controllerNum, pistolNum)

        return ExecuteRawQuery(Bgoz.objects, queryString, "fuelgas_details", ["mynum", "dt_num", "ervenyes"])


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
    num = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    user = models.CharField(max_length=70, blank=True)
    node = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
    ful = models.CharField(max_length=70, blank=True)
    sorrend = models.CharField(max_length=255, blank=True)
    grid = models.TextField(blank=True)
    class Meta:
        db_table = 'dbgrid'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=100, db_column='NAME') # Field name made lowercase.
    app_label = models.CharField(max_length=100, unique=True, db_column='APP_LABEL') # Field name made lowercase.
    model = models.CharField(max_length=100, unique=True, db_column='MODEL') # Field name made lowercase.
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True, db_column='SESSION_KEY') # Field name made lowercase.
    session_data = models.TextField(db_column='SESSION_DATA') # Field name made lowercase.
    expire_date = models.DateTimeField(db_column='EXPIRE_DATE') # Field name made lowercase.
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    domain = models.CharField(max_length=100, db_column='DOMAIN') # Field name made lowercase.
    name = models.CharField(max_length=50, db_column='NAME') # Field name made lowercase.
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

    @staticmethod
    def Details(node, user, fromDate, toDate):
        queryString = '''select v.*
            from "Kartyak" v, A_CARD p
            where
                (EXISTS(SELECT p1.MYCSOP, p1.MYCARD
                    FROM CS_TANK(%s, \'%s\') p1
                    where (v."azonosito"=p1.MYCARD) or
                          (v."csoport"=p1.MYCSOP)
                ))
            and(v."azonosito"=p.MYCARD)
            and(v."id"=p.MYID) order by v."nev";''' % (node , user)

        return ExecuteRawQuery(Kartyak.objects, queryString, "card_details", [""]);

    class Meta:
        db_table = 'Kartyak'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    app_name = models.CharField(max_length=255, db_column='APP_NAME') # Field name made lowercase.
    migration = models.CharField(max_length=255, db_column='MIGRATION') # Field name made lowercase.
    applied = models.DateTimeField(db_column='APPLIED') # Field name made lowercase.
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

    @staticmethod
    def Details(node, username, fromDate, toDate, isMetric):
        temperature_expr = GenerateTemperatureString('v', "hofok", isMetric)
        t_temperature_expr = GenerateTemperatureString('v', "t_hofok", isMetric)

        query = '''SELECT v."abs_id", v."vezerlo", v."sorszam", v."helyszin", v."datumido", v."dt_num", v."sofor_id", v."sofor_card", v."sofor_nev", v."sofor_csop", v."gep_id", v."gep_card", v."gep_nev", v."gep_csop", v."status_c", v."kut", v."km", v."u_ora", v."m_lev", v."e_km", v."e_uo", v."km_n", v."uo_n", v."km_m", v."uo_m", v."km_n_d", v."uo_n_d", v."mil_a",  v."s_n_d", v."km_a", v."uo_a", %s, v."ua_mm", v."v_mm", %s, v."e_ar", v."ua_tipn", v."tipus", v."liter", v."liter15", v."status_n", v.RDB$DB_KEY from "Tankolasok" v, (SELECT a."abs_id", a."vezerlo", a."gep_csop",a."kut" FROM "Tankolasok" a, (SELECT p.MYVEZ, p.MYKUT, MYCSOP FROM H_TANK(%s, \'%s\', -1) p) al WHERE ((a."vezerlo"=al."MYVEZ")AND(a."kut"=al."MYKUT"))or(a."gep_csop"=al.MYCSOP) GROUP by a."abs_id", a."vezerlo", a."kut", a."gep_csop") al2 WHERE v."abs_id"=al2."abs_id" and (v."dt_num">=%f) and (v."dt_num"<=%f)order by v."dt_num";''' % (temperature_expr, t_temperature_expr, int(node) , username,
            float(fromDate), float(toDate))

        data = []
        result = Tankolasok.objects.raw(query)
        for p in result:
            subset = [
                ["vezerlo", "", p.vezerlo],
                ["sorszam", "", p.sorszam],
                ["helyszin", "", p.helyszin],
                ["datumido", "", p.datumido],
                ["sofor_id", "", p.sofor_id],
                ["sofor_card", "", p.sofor_card],
                ["sofor_nev", "", p.sofor_nev],
                ["sofor_csop", "", p.sofor_csop],
                ["gep_id", "", p.gep_id],
                ["gep_card", "", p.gep_card],
                ["gep_nev", "", p.gep_nev],
                ["gep_csop", "", p.gep_csop],
                ["status_c", "", p.status_c],
                ["kut", "", p.kut],
                ["km", "", p.km],
                ["u_ora", "", p.u_ora],
                ["m_lev", "", p.m_lev],
                ["e_km", "", p.e_km],
                ["e_uo", "", p.e_uo],
                ["km_n", "", p.km_n],
                ["uo_n", "", p.uo_n],
                ["km_m", "", p.km_m],
                ["uo_m", "", p.uo_m],
                ["km_n_d", "", p.km_n_d],
                ["uo_n_d", "", p.uo_n_d],
                ["mil_a", "", p.mil_a],
                ["s_n_d", "", p.s_n_d],
                ["uo_a", "", p.uo_a],
                ["hofok", "", p.hofok],
                ["e_ar", "", p.e_ar],
                ["ua_tipn", "", p.ua_tipn],
                ["tipus", "", p.tipus],
                ["liter", "", p.liter],
                ["liter15", "", p.liter15],
                ["mil_a", "", p.mil_a]
            ]

            for item in subset:
                item[2] = unicode(item[2])

            data.append(subset)

        return {
            "desc": {
                "title_id": "refuelling_details",
                "text_id": True
            },

            "data": data
        }


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

    @staticmethod
    def Details(node, user, isMetric):
        parentStr = GenerateParentString(node)
        temperature_expr = GenerateTemperatureString("a", "hofok", isMetric)
        maxLiter_expr = '(a."max_liter" - a."keszlet") as max_liter' if isMetric else 'Trunc((a."max_liter" - a."keszlet")/3.75) as "max_liter"'

        queryString_metric = '''SELECT a."num", a."nev", a."helyszin", a."icon", a."ua_tip", a."es", a."es_vez", a."p1", a."p1_vez", a."p2", a."p2_vez", a."p3", a."p3_vez", a."p4", a."p4_vez", a."sajat", a."keszlet", a."keszlet15", a."kg", a."szazalek", a."csop", a."datumido", a."dt_num", a."suruseg", a."delete", a."zarolt_l", a."zarolt_mm", a."ua_tipn", a."a0", %s, %s, a.RDB$DB_KEY from "Tartalyok" a, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and("delete"='') and ("azonosito"<>'')and("tipus"='2') and ("user"='%s') Group by "nev"  ) al where (a."nev"=al."nev")and(a."delete"='') order by a."nev";''' % (temperature_expr, maxLiter_expr, parentStr, node, user)

        queryString_us = '''SELECT a."num", a."nev", a."helyszin", a."icon", a."ua_tip", a."es", a."es_vez", a."p1", a."p1_vez", a."p2", a."p2_vez", a."p3", a."p3_vez", a."p4", a."p4_vez", a."sajat", Trunc((a."keszlet")/3.75) as "keszlet", Trunc((a."keszlet15")/3.75) as "keszlet15", Trunc((a."kg")/0.45359)as "kg", a."szazalek", a."csop", a."datumido", a."dt_num", a."suruseg", a."delete", Trunc((a."zarolt_l")/3.75) as "zarolt_l", a."zarolt_mm", a."ua_tipn", a."a0", %s, %s, a.RDB$DB_KEY from "Tartalyok" a, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and("delete"='') and ("azonosito"<>'')and("tipus"='2') and ("user"='%s') Group by "nev"  ) al where (a."nev"=al."nev")and(a."delete"='') order by a."nev";''' % (temperature_expr, maxLiter_expr, parentStr, node, user)

        queryString = (queryString_metric if isMetric == '1' else queryString_us)

        return ExecuteRawQuery(Tartalyok.objects, queryString, "tank_details", ["num", "es", "es_vez", "icon", "dt_num", "delete", "db_key", "p1", "p1_vez", "p2", "p2_vez", "p3", "p3_vez", "p4", "p4_vez", "csop", "zarolt_mm", "a0", "max_liter", "ua_tipn", "hofok"])

    class Meta:
        db_table = 'tartalyok'

class Tlevel(models.Model):
    num = models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)
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
        db_table = 'tlevel'


class Treenode(models.Model):
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
    p1 = models.IntegerField(null=True, db_column='P1', blank=True) # Field name made lowercase.
    p2 = models.IntegerField(null=True, db_column='P2', blank=True) # Field name made lowercase.
    p3 = models.IntegerField(null=True, db_column='P3', blank=True) # Field name made lowercase.
    p4 = models.IntegerField(null=True, db_column='P4', blank=True) # Field name made lowercase.
    delete = models.CharField(max_length=20, blank=True)
    make = models.CharField(max_length=20, blank=True)
    read_only = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = 'TreeNode'

    @staticmethod
    def Queries(node):
        return {
            "desc": {
                "title_id": "queries",
                "text_id": True
            },

            "data": [[
                ["refuelling_details", "", "", "refueling_details/%s" % node, "compound_table_view"],
                ["refuelling_summary"],
                ["card_details", "", "", "card_details/%s" % node, "compound_table_view"],
                ["card_summary"],
                ["tank_details", "", "", "tank_details/%s" % node, "compound_table_view"],
                ["tank_diagram"],
                ["tank_summary"],
                ["controller_details", "", "", "controller_details/%s" % node, "compound_table_view"],
                ["controller_summary"],
                ["fuelgas_data"]
            ]]
        }

    @staticmethod
    def GetRoot(username):
        desc = {
            "title_id": "data",
            "text_id": True
        }

        data = Treenode.GetData(username, -1)

        return {
            "desc": desc,
            "data": data
        }

    @staticmethod
    def GetNodes(username, dbindx):
        data = Treenode.GetData(username, dbindx)

        if len(data[0]) == 0:
            return Treenode.Queries(dbindx)
        else:
            return {
                "desc": {
                    "title_id": "data",
                    "text_id": True
                },
                "data": data
            }

    @staticmethod
    def openIconFile(iconFileName):
        iconPath = os.path.join(settings.PROJECT_ROOT, "APIXServer", "icons")
        filename = os.path.join(iconPath, iconFileName)
        return Image.open(filename)

    @staticmethod
    def GetIcon(iconNum):
        try:
            return Treenode.openIconFile("%03d.ico" % iconNum)
        except:
            return None

    @staticmethod
    def GetOverlayIcon(node):
        iconName = None
        try:
            t = int(node.tipus.strip())
            if t == 0:
                iconName = "DefUnit48.ico"
            if t == 1:
                iconName = "GrpIco.ico"
            if t == 2:
                iconName = "DefTank48.ico"
        except ValueError:
            return None

        return Treenode.openIconFile(iconName) if iconName else None

    @staticmethod
    def OverlayIcon(bottomIcon, topIcon):
        return Image.alpha_composite(bottomIcon, topIcon)

    @staticmethod
    def GetData(username, dbindx):
        nodes = Treenode.objects.filter(user=username, parent0=dbindx)
        data = []

        for node in nodes:
            overlayIcon = Treenode.GetOverlayIcon(node)
            iconBlob = Treenode.GetIcon(node.icon)
            im_data = ""

            if iconBlob:
                if overlayIcon:
                    iconBlob = Treenode.OverlayIcon(iconBlob, overlayIcon)
                output = StringIO.StringIO()
                iconBlob.save(output, 'jpeg')
                im_data = output.getvalue()

            data_url = base64.b64encode(im_data)
            data.append([node.nev, data_url, "", "treenode/%d" % node.dbindx, "simple_table_view"])
            #data.append([node.nev, base64.b64encode(iconBlob.tostring()), "", "treenode/%d" % node.dbindx, "simple_table_view"])

        return [data]


class User(models.Model):
    num = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0, blank=True)
    nev = models.CharField(max_length=70, blank=True)
    datumido = models.CharField(max_length=30, blank=True)
    dt_num = models.FloatField(null=True, blank=True)
    delete = models.CharField(max_length=20, blank=True)
    passwd = models.TextField(blank=True)
    picture = models.TextField(blank=True)
    teszt = models.TextField(db_column='Teszt', blank=True)  # Field name made lowercase.

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

    @staticmethod
    def GetActualField(set, attrName):
        for line in set:
            if line[0] == attrName:
                return line[2]

    @staticmethod
    def DeleteAllFields(result, fieldName):
        for set in result["data"]:
            for line in set:
                for k in range(1, 5):
                    type_id = "t%dn" % k
                    if line[0] == type_id:
                        set.remove(line)
                        Vezerlok.DeleteAllFields(result, fieldName)

    @staticmethod
    def Details(node, user):
        parentStr = GenerateParentString(node)

        queryString = '''select v.* from "Vezerlok" v, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and ("azonosito"<>'') and("tipus"='0') and("user"='%s') Group by "nev"  ) al where (v."nev"=al."nev")and(v."delete"='') order by v."nev"''' % (parentStr, node, user)

        result = ExecuteRawQuery(Vezerlok.objects, queryString, "controller_details", ["icon", "abs_id", "num", "delete", "path", "t1", "t2", "t3", "t4", "l_tip", "com", "cim", "ido", "dl_dt", "com_azon", "time_chk", "bgoz", "b_side_vez", "b_side_p", "p1_sz", "p2_sz", "p3_sz", "p4_sz", "p1_err", "p2_err", "p3_err", "p4_err", "p1_tmr", "p2_tmr", "p3_tmr", "p4_tmr", "sajat", "tipus"])

        for set in result["data"]:
            name = Vezerlok.GetActualField(set, "nev").strip()
            for line in set:
                for n in range(1, 5):
                    type_id = "t%dn" % n
                    pistol_id = "p%d" % n
                    fuel_type = Vezerlok.GetActualField(set, type_id)
                    pistol_num = Vezerlok.GetActualField(set, pistol_id)

                    if line[0] == pistol_id and fuel_type == 1:  # 1 means benzin
                        line.append("fuelgas_details/%s/%d" % (name, pistol_num))
                        line.append("compound_table_view")

        for n in range(1, 5):
            type_id = "t%dn" % n
            Vezerlok.DeleteAllFields(result, type_id)

        return result
