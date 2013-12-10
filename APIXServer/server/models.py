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
from django.db import models
import decimal
from icons import Icons
import StringIO
import base64
import matplotlib.pyplot as plt
import datetime
from itertools import repeat


IconDB = Icons()

TREENODETYPE_PLACE_OF_USAGE_ID = "0"
TREENODETYPE_USER_GROUPS_ID = "1"
TREENODETYPE_AREA_OF_USAGE_ID = "2"


def ExecuteRawQuery(objects, queryString, titleId, exclude=[], summaryMenu=[], converters={}):
        data = []
        result = objects.raw(queryString)
        columnNames = result.columns[:]

        for i in exclude:
            try:
                columnNames.remove(i)
            except ValueError:
                print "Column %s cannot be found" % i

        for p in result:
            subset = []
            subset.extend(summaryMenu)
            subset.append(["new_section"])

            for column_name in columnNames:
                s1 = unicode(column_name, errors='replace')
                s2 = getattr(p, column_name)

                if type(s2) is str:
                    s2 = s2.decode("windows-1250")
                elif type(s2) is decimal.Decimal:
                    s2 = str(s2)

                if column_name in converters.keys():
                    s2 = converters[column_name](s2.strip())

                subset.append([s1, "", s2])

            data.append(subset)

        return {
            "desc": {
                "title_id": titleId,
                "text_id": True
            },

            "data": data
        }


def GenerateTemperatureString(tableId, temperatureField):
    return '%s."%s"' % (tableId, temperatureField)


def GenerateParentString(node):
    parentStr = ""

    for i in range(0, 9):
        parentStr += '("parent%d"=%s) or ' % (i, node)

    return parentStr


def GetAttr(p, field):
        attr = getattr(p, field)
        return attr if attr else 0


def GetActualField(set, attrName):
    for line in set:
        if line[0] == attrName:
            return line[2]


def RemoveField(set, attrName):
    for line in set:
        if line[0] == attrName:
            set.remove(line)
            continue


def DrawDiagram(axisDesc, results, title_id, ylimit=None):
    dateAxis = []
    # In the database, dt_num is a Delphi/float representation of the dates, starting point is 1899.12.30 0:0:0. Python datetime calculates with starting point 1.1.1 0:0:0. This magic number is teh fload difference of the two.
    delphiStartDate = datetime.date(1899, 12, 30)
    dataAxises = [[]] + list(repeat([], len(axisDesc)))

    for p in results:
        date = datetime.timedelta(GetAttr(p, "dt_num")) + delphiStartDate
        dateAxis.append(date)

        for i in range(0, len(axisDesc)):
            dataAxises[i].append(GetAttr(p, axisDesc[i]["column"]))
            dataAxises[i]

    fig = plt.figure()

    for i in range(0, len(axisDesc)):
        plt.plot_date(dateAxis, dataAxises[i], axisDesc[i]["line"], label=axisDesc[i]["label"])

    if ylimit:
        ax = plt.subplot(111)
        ax.set_ylim(ylimit)

    plt.legend()
    fig.autofmt_xdate()
    # Tweak spacing to prevent clipping of ylabel
    output = StringIO.StringIO()
    plt.savefig(output, format='png', orientation='landscape')
    im_data = output.getvalue()
    data = [["", base64.b64encode(im_data)]]

    return {
        "desc": {
            "title_id": title_id,
            "text_id": True
        },

        "data": [data]
    }


def GetLabels(column, language, isMetric="1"):
    columnTranslated = column

    if language == "hu":
        if column == "ua_l":
            columnTranslated = "készlet, " + ("liter " if isMetric == "1" else "gallon")
        elif column == "ua_l15":
            columnTranslated = "készlet, " + ("liter, 15˚C" if isMetric == "1" else "gallon, 58˚F")
        elif column == "hofok":
            columnTranslated = "höfok, " + (", ˚C" if isMetric == "1" else "˚F")
        elif column == "h2o_mm":
            columnTranslated = "víz magasság, mm"
        elif column == "szazalek":
            columnTranslated = "százalék"
        elif column == "hiba":
            columnTranslated = "hibaszám"
    if language == "en":
        if column == "ua_l":
            columnTranslated = "inventory, " + ("liter " if isMetric == "1" else "gallon")
        elif column == "ua_l15":
            columnTranslated = "inventory, " + ("liter, 15˚C" if isMetric == "1" else "gallon, 58˚F")
        elif column == "hofok":
            columnTranslated = "temperature, " + (", ˚C" if isMetric == "1" else "˚F")
        elif column == "h2o_mm":
            columnTranslated = "water level, mm"
        elif column == "szazalek":
            columnTranslated = "percentage"
        elif column == "hiba":
            columnTranslated = "error number"

    return columnTranslated


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
    date_joined = models.DateTimeField(db_column='DATE_JOINED') # Field name made lowercase


    class Meta:
        db_table = 'auth_user'
\
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
    def GetQueryString(fromDate, toDate, controllerNum, pistolNum):
        return '''SELECT * from "Bgoz" where ("dt_num">=%s)and("dt_num"<%s)and("vez"='%s')and("piszt"=%s) and ("ervenyes"<>'') order by "dt_num";''' % (toDate, fromDate, controllerNum, pistolNum)

    @staticmethod
    def Diagrams(fromDate, toDate, controllerNum, pistolNum, language):
        queryString = Bgoz.GetQueryString(fromDate, toDate, controllerNum, pistolNum)

        axisDesc = [
            {
                "column": "szazalek",
                "label": GetLabels("szazalek", language),
                "line": "b-"
            },
            {
                "column": "hiba",
                "label": GetLabels("hiba", language),
                "line": "r-"
            }
        ]

        return DrawDiagram(axisDesc, Bgoz.objects.raw(queryString), "fuelgas_percentage_diagram", [-5, 140])


class Csoportok(models.Model):
    num = models.IntegerField(primary_key=True, blank=True, db_column='num')
    indx = models.IntegerField(null=True, blank=True)
    nev = models.CharField(max_length=70, blank=True, db_column='nev')
    icon = models.IntegerField(null=True, blank=True)
    sajat = models.CharField(max_length=10, blank=True)
    megj = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = '"Csoportok"'

    @staticmethod
    def GetQueryString(node, username):
        parentStr = GenerateParentString(node)

        return '''select v.* from "Csoportok" v, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and("delete"='') and ("azonosito"<>'') and ("tipus"='1') and ("user"='%s') Group by "nev") al where (v."nev"=al."nev") order by v."nev";''' % (parentStr, node, username)

    @staticmethod
    def Details(username, node):
        queryString = Csoportok.GetQueryString(node, username)
        summaryMenu = [["group_summary", "", "", "group_summary/%s" % node, "simple_table_view"]]

        return ExecuteRawQuery(Csoportok.objects, queryString, "group_details", ["icon", "sajat"], summaryMenu)

    @staticmethod
    def Summary(username, node):
        queryString =  Csoportok.GetQueryString(node, username)
        results = Csoportok.objects.raw(queryString)
        data = [["sGroup", "", sum(1 for result in results)]]

        return {
            "desc": {
                "title_id": "group_summary",
                "text_id": True
            },

            "data": [data]
        }

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
    def GetQueryString(node, username, treenodeType):
        if treenodeType == TREENODETYPE_USER_GROUPS_ID:
            return '''select v.*
                from "Kartyak" v, A_CARD p
                where
                    (EXISTS(SELECT p1.MYCSOP, p1.MYCARD
                        FROM CS_TANK(%s, \'%s\') p1
                        where (v."azonosito"=p1.MYCARD) or
                              (v."csoport"=p1.MYCSOP)
                    ))
                and(v."azonosito"=p.MYCARD)
                and(v."id"=p.MYID) order by v."nev";''' % (node, username)
        elif treenodeType == TREENODETYPE_PLACE_OF_USAGE_ID:
            return '''select v.* from "Kartyak" v, (SELECT p.MYID FROM H_CARD(%s, \'%s\') p) al where (v."id"=al.MYID) order by v."nev";''' % (node, username)

    @staticmethod
    def TypeConverter(t):
        if t == "0":
            return "t_master"
        elif t == "1":
            return "t_driver"
        elif t == "2":
            return "t_machine"
        elif t == "4":
            return "t_banned"

        return t

    @staticmethod
    def Details(node, username, treenodeType):
        queryString = Kartyak.GetQueryString(node, username, treenodeType)
        summaryMenu = [["card_summary", "", "", "card_summary/%s/%s" % (node, treenodeType), "simple_table_view"]]
        return ExecuteRawQuery(Kartyak.objects, queryString, "card_details", ["id", "vezerlo", "dt_num", "options", "icon", "actual"], summaryMenu, {'tipus': Kartyak.TypeConverter})

    @staticmethod
    def Summary(node, username, treenodeType):
        queryString = Kartyak.GetQueryString(node, username, treenodeType)
        results = Kartyak.objects.raw(queryString)
        data = []
        sCard = 0;
        dCard = 0;
        cCard = 0;
        mCard = 0;
        tCard = 0;
        sCsop = {};

        for p in results:
            t = GetAttr(p, "tipus").strip()
            sCard += 1
            if t == "0":
                mCard += 1
            elif t == "1":
                dCard += 1
            elif t == "2":
                cCard += 1
            elif t == "4":
                tCard += 1

            sCsop[GetAttr(p, "csoport")] = 1

        data.append(["sCard", "", sCard])
        data.append(["cCard", "", cCard])
        data.append(["dCard", "", dCard])
        data.append(["mCard", "", mCard])
        data.append(["tCard", "", tCard])
        data.append(["sGroup", "", len(sCsop.keys())])

        return {
            "desc": {
                "title_id": "cards_summary",
                "text_id": True
            },

            "data": [data]
        }

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
    def GetQueryString(node, username, fromDate, toDate, treenodeType):
        if treenodeType == TREENODETYPE_AREA_OF_USAGE_ID:
            return '''SELECT v.* from "Tankolasok" v WHERE (v."dt_num">=%f) and (v."dt_num"<=%f) order by v."dt_num";''' % (float(fromDate), float(toDate))
        elif treenodeType == TREENODETYPE_USER_GROUPS_ID:
            return '''SELECT v.* from "Tankolasok" v, (SELECT a."abs_id", a."sofor_csop", a."gep_csop",a."sofor_card",a."gep_card" FROM "Tankolasok" a, (SELECT p.MYCSOP, p.MYCARD FROM CS_TANK(%s, \'%s\') p) al WHERE (a."sofor_csop"=al.MYCSOP)or(a."gep_csop"=al.MYCSOP)or(a."sofor_card"=al.MYCARD)or(a."gep_card"=al.MYCARD) GROUP by a."abs_id", a."sofor_csop", a."gep_csop",a."sofor_card",a."gep_card") al2 WHERE v."abs_id"=al2."abs_id"and (v."dt_num">=%f) and (v."dt_num"<=%f) order by v."dt_num";''' % (node, username, float(fromDate), float(toDate))
        elif treenodeType == TREENODETYPE_PLACE_OF_USAGE_ID:
            return '''SELECT v.* from "Tankolasok" v, (SELECT a."abs_id", a."vezerlo", a."gep_csop",a."kut" FROM "Tankolasok" a, (SELECT p.MYVEZ, p.MYKUT, p.MYCSOP FROM H_TANK(%s, \'%s\', -1) p) al WHERE ((a."vezerlo"=al."MYVEZ")AND(a."kut"=al."MYKUT"))or(a."gep_csop"=al.MYCSOP) GROUP by a."abs_id", a."vezerlo", a."kut", a."gep_csop") al2 WHERE v."abs_id"=al2."abs_id" and(v."dt_num">=%f)and(v."dt_num"<=%f) order by v."dt_num";''' % (node, username, float(fromDate), float(toDate))

    @staticmethod
    def Details(node, username, fromDate, toDate, treenodeType):
        queryString = Tankolasok.GetQueryString(node, username, fromDate, toDate, treenodeType)

        summaryMenu = [["refuelling_summary", "", "", "refueling_summary/%s/%s" % (node, treenodeType), "simple_table_view"]]

        return ExecuteRawQuery(Tankolasok.objects, queryString, "refuelling_details", ["abs_id", "dt_num", "status_c", "s_n_d", "ua_mm", "v_mm", "t_hofok", "e_ar", "status_n", "mil_a"],  summaryMenu)

    @staticmethod
    def Summary(node, username, fromDate, toDate, treenodeType):
        queryString = Tankolasok.GetQueryString(node, username, fromDate, toDate, treenodeType)
        results = Tankolasok.objects.raw(queryString)
        data = []
        sCNT = 0
        sLit = 0
        sLit15 = 0
        smLit = 0
        smLit15 = 0
        bCNT = 0
        bLit = 0
        bLit15 = 0
        bmLit = 0
        bmLit15 = 0
        dCNT = 0
        dLit = 0
        dLit15 = 0
        dmLit = 0
        dmLit15 = 0
        jCNT = 0
        jLit = 0
        jLit15 = 0
        jmLit = 0
        jmLit15 = 0

        for p in results:
            sCNT += 1
            sLit += GetAttr(p, "liter")
            sLit15 += GetAttr(p, "liter15")

            if smLit < sLit:
                smLit = GetAttr(p, "liter")
                smLit15 = GetAttr(p, "liter15")

            ua_tipn = getattr(p, "ua_tipn")

            if ua_tipn and ua_tipn == 1:  # Benzin
                bCNT += 1
                bLit += GetAttr(p, "liter")
                bLit15 += GetAttr(p, "liter15")

                if bmLit < bLit:
                    bmLit = GetAttr(p, "liter")
                    bmLit15 = GetAttr(p, "liter15")

            if ua_tipn and ua_tipn == 2:  # Gasolin
                dCNT += 1
                dLit += GetAttr(p, "liter")
                dLit15 += GetAttr(p, "liter15")

                if dmLit < dLit:
                    dmLit = GetAttr(p, "liter")
                    dmLit15 = GetAttr(p, "liter15")

            if ua_tipn and ua_tipn == 3:  # Jet
                jCNT += 1
                jLit += GetAttr(p, "liter")
                jLit15 += GetAttr(p, "liter15")

                if jmLit < jLit:
                    jmLit = GetAttr(p, "liter")
                    jmLit15 = GetAttr(p, "liter15")

        def average(x, y):
            return str("{0:.3f}".format(x / y) if y > 0 else 0)

        data.append(["E95", "", ""])
        data.append(["count", "", str(bCNT)])
        data.append(["sLiter", "", str(bLit)])
        data.append(["sLiter15", "", str(bLit15)])
        data.append(["aLiter", "", average(bLit, bCNT)])
        data.append(["aLiter15", "", average(bLit15, bCNT)])
        data.append(["mLiter", "", str(bmLit)])
        data.append(["mLiter15", "", str(bmLit15)])

        data.append(["new_section"])
        data.append(["Diesel", "", ""])
        data.append(["count", "", str(dCNT)])
        data.append(["sLiter", "", str(dLit)])
        data.append(["sLiter15", "", str(dLit15)])
        data.append(["aLiter", "", average(dLit, dCNT)])
        data.append(["aLiter15", "", average(dLit15, dCNT)])
        data.append(["mLiter", "", str(dmLit)])
        data.append(["mLiter15", "", str(dmLit15)])

        data.append(["new_section"])
        data.append(["Jet A1", "", ""])
        data.append(["count", "", str(jCNT)])
        data.append(["sLiter", "", str(jLit)])
        data.append(["sLiter15", "", str(jLit15)])
        data.append(["aLiter", "", average(jLit, jCNT)])
        data.append(["aLiter15", "", average(jLit15, jCNT)])
        data.append(["mLiter", "", str(jmLit)])
        data.append(["mLiter15", "", str(jmLit15)])

        data.append(["new_section"])
        data.append(["all_fuel", "", ""])
        data.append(["count", "", str(sCNT)])
        data.append(["sLiter", "", str(sLit)])
        data.append(["sLiter15", "", str(sLit15)])
        data.append(["aLiter", "", average(sLit, sCNT)])
        data.append(["aLiter15", "", average(sLit15, sCNT)])
        data.append(["mLiter", "", str(smLit)])
        data.append(["mLiter15", "", str(smLit15)])

        return {
            "desc": {
                "title_id": "refuelling_summary",
                "text_id": True
            },

            "data": [data]
        }


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

    @staticmethod
    def GetQueryString(node, user):
        parentStr = GenerateParentString(node)
        maxLiter_expr = '(a."max_liter" - a."keszlet") as max_liter'

        queryString = '''SELECT a."num", a."nev", a."helyszin", a."icon", a."ua_tip", a."es", a."es_vez", a."p1", a."p1_vez", a."p2", a."p2_vez", a."p3", a."p3_vez", a."p4", a."p4_vez", a."sajat", a."keszlet", a."keszlet15", a."kg", a."szazalek", a."csop", a."datumido", a."dt_num", a."suruseg", a."delete", a."zarolt_l", a."zarolt_mm", a."a0", a."hofok", %s, a.RDB$DB_KEY from "Tartalyok" a, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and("delete"='') and ("azonosito"<>'')and("tipus"='2') and ("user"='%s') Group by "nev"  ) al where (a."nev"=al."nev")and(a."delete"='') order by a."nev";''' % (maxLiter_expr, parentStr, node, user)

        return queryString

    @staticmethod
    def Details(node, user):
        queryString = Tartalyok.GetQueryString(node, user)
        summaryMenu = [
            ["tank_summary", "", "", "tank_summary/%s" % node, "simple_table_view"]
        ]

        result = ExecuteRawQuery(Tartalyok.objects, queryString, "tank_details", ["es", "es_vez", "icon", "dt_num", "delete", "db_key", "csop", "zarolt_mm", "a0", "max_liter"], summaryMenu)

        data = result["data"]

        for set in data:
            tankNum = GetActualField(set, "num")

            set.insert(1, ["tank_inventory_diagram", "", "", "tank_inventory_diagram/%d" % tankNum, "image_table_view"])
            set.insert(1, ["tank_water_height_diagram", "", "", "tank_water_height_diagram/%d" % tankNum, "image_table_view"])
            set.insert(1, ["tank_temperature_diagram", "", "", "tank_temperature_diagram/%d" % tankNum, "image_table_view"])
            # num should not be present in the result set, but was required to
            # to construct the diagram menus
            RemoveField(set, "num")

        return result

    @staticmethod
    def AddSummaryField(results, field):
        sum = 0

        for p in results:
            attr = getattr(p, field)

            if attr:
                sum += attr

        return [field, "", str(sum)]

    @staticmethod
    def Summary(node, user):
        queryString = Tartalyok.GetQueryString(node, user)
        results = Tartalyok.objects.raw(queryString)
        data = []
        sum_keszlet = 0
        sum_keszlet15 = 0
        sum_max_liter = 0
        sum_zarolt_l = 0
        benzin_keszlet = 0
        benzin_keszlet15 = 0
        benzin_max_liter = 0
        benzin_zarolt_l = 0
        gasolin_keszlet = 0
        gasolin_keszlet15 = 0
        gasolin_max_liter = 0
        gasolin_zarolt_l = 0
        jet_keszlet = 0
        jet_keszlet15 = 0
        jet_max_liter = 0
        jet_zarolt_l = 0
        tankCount = 0

        for p in results:
            tankCount += 1
            keszlet = GetAttr(p, "keszlet")
            keszlet15 = GetAttr(p, "keszlet15")
            max_liter = GetAttr(p, "max_liter")
            zarolt_l = GetAttr(p, "zarolt_l")
            sum_keszlet += keszlet
            sum_keszlet15 += keszlet15
            sum_max_liter += max_liter
            sum_zarolt_l += zarolt_l

            ua_tipn = GetAttr(p, "ua_tipn")

            if ua_tipn and ua_tipn == 1:  # Benzin
                benzin_keszlet += keszlet
                benzin_keszlet15 += keszlet15
                benzin_max_liter += max_liter
                benzin_zarolt_l += zarolt_l

            if ua_tipn and ua_tipn == 2:  # Gasolin
                gasolin_keszlet += keszlet
                gasolin_keszlet15 += keszlet15
                gasolin_max_liter += max_liter
                gasolin_zarolt_l += zarolt_l

            if ua_tipn and ua_tipn == 3:  # Jet
                jet_keszlet += keszlet
                jet_keszlet15 += keszlet15
                jet_max_liter += max_liter
                jet_zarolt_l += zarolt_l

        data.append(["tank_count", "", str(tankCount)])

        data.append(["new_section"])
        data.append(["Diesel", "", ""])
        data.append(["keszlet", "", str(gasolin_keszlet)])
        data.append(["keszlet15", "", str(gasolin_keszlet15)])
        data.append(["max_liter", "", str(gasolin_max_liter)])
        data.append(["zarolt_l", "", str(gasolin_zarolt_l)])

        data.append(["new_section"])
        data.append(["E95", "", ""])
        data.append(["keszlet", "", str(benzin_keszlet)])
        data.append(["keszlet15", "", str(benzin_keszlet15)])
        data.append(["max_liter", "", str(benzin_max_liter)])
        data.append(["zarolt_l", "", str(benzin_zarolt_l)])

        data.append(["new_section"])
        data.append(["Jet A1", "", ""])
        data.append(["keszlet", "", str(jet_keszlet)])
        data.append(["keszlet15", "", str(jet_keszlet15)])
        data.append(["max_liter", "", str(jet_max_liter)])
        data.append(["zarolt_l", "", str(jet_zarolt_l)])

        data.append(["new_section"])
        data.append(["all_fuel", "", ""])
        data.append(["keszlet", "", str(sum_keszlet)])
        data.append(["keszlet15", "", str(sum_keszlet15)])
        data.append(["max_liter", "", str(sum_max_liter)])
        data.append(["zarolt_l", "", str(sum_zarolt_l)])

        return {
            "desc": {
                "title_id": "tank_summary",
                "text_id": True
            },

            "data": [data]
        }

    @staticmethod
    def GetDiagramQueryString(fromDate, toDate, tankNum, isMetric):
        if isMetric == "1":
            return '''SELECT a."num", a."tartaly", a."datumido", a."dt_num", a."ua_mm", a."h2o_mm", a."hofok",  a."ua_l", a."ua_l15", a."h2o_l",a."tipus", a."vez", a."kut", a."e_ar", a."gcsop",  a."delete", a.RDB$DB_KEY from "TLevel" a where (a."dt_num">=%s)and(a."dt_num"<%s)and(a."tartaly"=%s) and (a."delete" is NULL )and(a."kut">80) order by a."dt_num"''' % (toDate, fromDate, tankNum)
        else:
            return '''SELECT a."num", a."tartaly", a."datumido", a."dt_num", a."ua_mm", a."h2o_mm", (((a."hofok")*9)/5)+32 as "hofok", Trunc((a."ua_l")/3.79) as "ua_l", Trunc((a."ua_l15")/3.79) as "ua_l15", a."h2o_l", a."tipus", a."vez", a."kut", a."e_ar", a."gcsop",  a."delete", a.RDB$DB_KEY from "TLevel" a where (a."dt_num">=%s)and(a."dt_num"<%s)and(a."tartaly"=%s) and (a."delete" is NULL )and(a."kut">80) order by a."dt_num"''' % (toDate, fromDate, tankNum)

    @staticmethod
    def DrawDiagram(axisDesc, queryString):
        return DrawDiagram(axisDesc, Tlevel.objects.raw(queryString), "tank_diagram")

    @staticmethod
    def InventoryDiagram(fromDate, toDate, tankNum, isMetric, language):
        queryString = Tartalyok.GetDiagramQueryString(
            fromDate, toDate, tankNum, isMetric)

        axisDesc = [
            {
                "column": "ua_l",
                "label": GetLabels("ua_l", language, isMetric),
                "line" : "b-"
            },
            {
                "column": "ua_l15",
                "label": GetLabels("ua_l15", language, isMetric),
                "line" : "g-"
            },
        ]

        return Tartalyok.DrawDiagram(axisDesc, queryString)

    @staticmethod
    def TemperatureDiagram(fromDate, toDate, tankNum, isMetric, language):
        queryString = Tartalyok.GetDiagramQueryString(
            fromDate, toDate, tankNum, isMetric)

        axisDesc = [
            {
                "column": "hofok",
                "label": GetLabels("hofok", language, isMetric),
                "line": "r-"
            }
        ]

        return Tartalyok.DrawDiagram(axisDesc, queryString)

    @staticmethod
    def WaterHeightDiagram(fromDate, toDate, tankNum, isMetric, language):
        queryString = Tartalyok.GetDiagramQueryString(
            fromDate, toDate, tankNum, isMetric)

        axisDesc = [
            {
                "column": "h2o_mm",
                "label": GetLabels("h2o_mm", language, isMetric),
                "line": "b-"
            }
        ]

        return Tartalyok.DrawDiagram(axisDesc, queryString)


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
    def GetRoot(username):
        nodes = Treenode.GetRawNodes(username, -1);
        data = []

        for node in nodes:
            data.append([node.nev, IconDB.icon(node.icon), "", "treenode/%d/%d" % (node.dbindx, node.dbindx), "simple_table_view"])

        return {
            "desc": {
                "title_id": "data",
                "text_id": True
            },
            "data": [data]
        }

    @staticmethod
    def GetNodes(username, dbindx, treenodeType):
        data = Treenode.GetData(username, dbindx, treenodeType)

        return {
            "desc": {
                "title_id": "data",
                "text_id": True
            },
            "data": [data]
        }

    @staticmethod
    def GetRawNodes(username, dbindx):
        return Treenode.objects.filter(user=username, parent0=dbindx, delete="", ).order_by('nev')

    @staticmethod
    def GetData(username, dbindx, treenodeType):
        nodes = Treenode.GetRawNodes(username, dbindx);
        data = []

        if treenodeType == TREENODETYPE_AREA_OF_USAGE_ID:
            data.append(["refuelling_details", "", "", "refueling_details/%s/%s" % (dbindx, TREENODETYPE_AREA_OF_USAGE_ID), "compound_table_view"])
        elif treenodeType == TREENODETYPE_USER_GROUPS_ID:
            data.append(["refuelling_details", "", "", "refueling_details/%s/%s" % (dbindx, TREENODETYPE_USER_GROUPS_ID), "compound_table_view"])
            data.append(["card_details", "", "", "card_details/%s/%s" % (dbindx, TREENODETYPE_USER_GROUPS_ID), "compound_table_view"])
            data.append(["group_details", "", "", "group_details/%s" % (dbindx), "compound_table_view"])
        elif treenodeType == TREENODETYPE_PLACE_OF_USAGE_ID:
            data.append(["refuelling_details", "", "", "refueling_details/%s/%s" % (dbindx, TREENODETYPE_PLACE_OF_USAGE_ID), "compound_table_view"])
            data.append(["card_details", "", "", "card_details/%s/%s" % (dbindx, TREENODETYPE_PLACE_OF_USAGE_ID), "compound_table_view"])
            data.append(["tank_details", "", "", "tank_details/%s" % (dbindx), "compound_table_view"])
            data.append(["controller_details", "", "", "controller_details/%s" % (dbindx), "compound_table_view"])
        elif dbindx != "-1":
            data = [
                ["refuelling_details", "", "", "refueling_details/%s/%s" % (dbindx, treenodeType), "compound_table_view"],
                ["card_details", "", "", "card_details/%s/%s" % (dbindx, treenodeType), "compound_table_view"],
                ["tank_details", "", "", "tank_details/%s" % dbindx, "compound_table_view"],
                ["controller_details", "", "", "controller_details/%s" % dbindx, "compound_table_view"]
            ]

        data.append(["new_section"])

        for node in nodes:
                data.append([node.nev, IconDB.icon(node.icon), "", "treenode/%s/%s" % (node.dbindx, treenodeType), "simple_table_view"])

        return data


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
    def TypeConverter(t):
        if t == 1:
            return "E95"
        elif t == 2:
            return "Diesel"
        elif t == 3:
            return "Jet"

        return t

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
    def GetQueryString(node, user):
        parentStr = GenerateParentString(node)

        return '''select v.* from "Vezerlok" v, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and ("azonosito"<>'') and("tipus"='0') and("user"='%s') Group by "nev"  ) al where (v."nev"=al."nev")and(v."delete"='') order by v."nev"''' % (parentStr, node, user)

    @staticmethod
    def Details(node, user):
        queryString = Vezerlok.GetQueryString(node, user)
        summaryMenu = [["controller_summary", "", "", "controller_summary/%s" % node, "simple_table_view"]]

        result = ExecuteRawQuery(Vezerlok.objects, queryString, "controller_details", ["icon", "abs_id", "num", "delete", "path", "t1", "t2", "t3", "t4", "l_tip", "com", "cim", "ido", "dl_dt", "com_azon", "time_chk", "bgoz", "b_side_vez", "b_side_p", "p1_sz", "p2_sz", "p3_sz", "p4_sz", "p1_err", "p2_err", "p3_err", "p4_err", "p1_tmr", "p2_tmr", "p3_tmr", "p4_tmr", "sajat", "tipus"], summaryMenu)

        for set in result["data"]:
            name = GetActualField(set, "nev").strip()
            for line in set:
                for n in range(1, 5):
                    type_id = "t%dn" % n
                    pistol_id = "p%d" % n
                    fuel_type = GetActualField(set, type_id)
                    pistol_num = GetActualField(set, pistol_id)

                    if line[0] == pistol_id:
                        if line[2]:
                            line[2] = "%d (%s)" % (line[2], Vezerlok.TypeConverter(fuel_type))

                        if fuel_type == 1:  # 1 means benzin
                            line.append("fuelgas_diagrams/%s/%d" % (name, pistol_num))
                            line.append("image_table_view")

        for n in range(1, 5):
            type_id = "t%dn" % n
            Vezerlok.DeleteAllFields(result, type_id)

        return result

    @staticmethod
    def Summary(node, user):
        queryString = Vezerlok.GetQueryString(node, user)
        results = Vezerlok.objects.raw(queryString)
        data = []



        return {
            "desc": {
                "title_id": "controller_summary",
                "text_id": True
            },

            "data": [data]
        }
