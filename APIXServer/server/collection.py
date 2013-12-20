#!/usr/bin/python
# -*- coding: utf-8
from __future__ import unicode_literals
from icons import Icons
import decimal
import matplotlib.pyplot as plt
import datetime
from itertools import repeat
import StringIO
import base64


class Collection():
    # These values represent the root menu items. It is important, because
    # the queries may be different, depending on the values. These values
    # also appear in the URL-s (part of the server API) as is.
    COLLECTIONTYPE_PLACE_OF_USAGE_ID = "0"
    COLLECTIONTYPE_USER_GROUPS_ID = "1"
    COLLECTIONTYPE_AREA_OF_USAGE_ID = "2"

    IconDB = Icons()

    def executeRawQuery(
        self, objects, queryString, exclude=[], summaryMenu=[], converters={}
    ):
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
            "desc": self.desc,
            "data": data
        }

    def getAttr(self, p, field):
        attr = getattr(p, field)
        return attr if attr else 0

    def generateTemperatureString(self, tableId, temperatureField):
        return '%s."%s"' % (tableId, temperatureField)

    def generateParentString(self, node):
        parentStr = ""

        for i in range(0, 9):
            parentStr += '("parent%d"=%s) or ' % (i, node)

        return parentStr

    def getActualField(self, set, attrName):
        for line in set:
            if line[0] == attrName:
                return line[2]

    def removeField(self, set, attrName):
        for line in set:
            if line[0] == attrName:
                set.remove(line)
                continue

    def draw(self, axisDesc, results, title_id, ylimit=None):
        dateAxis = []
        # In the database, dt_num is a Delphi/float representation of the dates, starting point is 1899.12.30 0:0:0. Python datetime calculates with starting point 1.1.1 0:0:0. This magic number is teh fload difference of the two.
        delphiStartDate = datetime.date(1899, 12, 30)
        dataAxises = [[]] + list(repeat([], len(axisDesc)))

        if not len(list(results)):
            return {
                "desc": self.desc,
                "data": []
            }

        for p in results:
            date = datetime.timedelta(self.getAttr(p, "dt_num")) + delphiStartDate

            dateAxis.append(date)

            for i in range(0, len(axisDesc)):
                dataAxises[i].append(self.getAttr(p, axisDesc[i]["column"]))
                dataAxises[i]

        fig = plt.figure()

        for i in range(0, len(axisDesc)):
            plt.plot_date(dateAxis, dataAxises[i], axisDesc[i]["line"], label=axisDesc[i]["label"])

        if ylimit:
            ax = plt.subplot(111)
            ax.set_ylim(ylimit)

        plt.legend()
        # Tweak spacing to prevent clipping of ylabel
        fig.autofmt_xdate()
        output = StringIO.StringIO()
        plt.savefig(output, format='png', orientation='landscape')
        im_data = output.getvalue()
        data = [["", base64.b64encode(im_data)]]

        return {
            "desc": self.desc,
            "data": [data]
        }

    def getLabels(self, column, language, isMetric="1"):
        columnTranslated = column

        if language == "hu":
            if column == "ua_l":
                columnTranslated = "készlet, " + ("liter " if isMetric == "1" else "gallon")
            elif column == "ua_l15":
                columnTranslated = "készlet, " + ("liter, 15˚C" if isMetric == "1" else "gallon, 58˚F")
            elif column == "hofok":
                columnTranslated = "höfok, " + ("˚C" if isMetric == "1" else "˚F")
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
                columnTranslated = "temperature, " + ("˚C" if isMetric == "1" else "˚F")
            elif column == "h2o_mm":
                columnTranslated = "water level, mm"
            elif column == "szazalek":
                columnTranslated = "percentage"
            elif column == "hiba":
                columnTranslated = "error number"

        return columnTranslated
