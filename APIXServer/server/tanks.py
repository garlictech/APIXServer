#!/usr/bin/python
# -*- coding: utf-8
from models import Tartalyok, Tlevel
from collection import Collection


class Tanks(Collection, Tartalyok):
    desc = {
        "title_id": "tanks",
        "text_id": True,
        "sensitiveTo": ["DatesChanged", "MetricChanged"]
    }

    DBGRID_TAB_ID = 3

    def getQueryString(self, node, user, order_by):
        parentStr = self.generateParentString(node)
        maxLiter_expr = '(a."max_liter" - a."keszlet") as max_liter'

        queryString = '''SELECT a."num", a."nev", a."helyszin", a."icon", a."ua_tip", a."es", a."es_vez", a."p1", a."p1_vez", a."p2", a."p2_vez", a."p3", a."p3_vez", a."p4", a."p4_vez", a."sajat", a."keszlet", a."keszlet15", a."kg", a."szazalek", a."csop", a."datumido", a."dt_num", a."suruseg", a."delete", a."zarolt_l", a."zarolt_mm", a."a0", a."hofok", %s, a.RDB$DB_KEY from "Tartalyok" a, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and("delete"='') and ("azonosito"<>'')and("tipus"='2') and ("user"='%s') Group by "nev"  ) al where (a."nev"=al."nev")and(a."delete"='') %s;''' % (maxLiter_expr, parentStr, node, user, order_by)

        return queryString

    def details(self, node, user):
        fields = self.getFieldsFromDBGrid(node, user, self.DBGRID_TAB_ID)
        queryString = self.getQueryString(node, user, fields["order_by"])

        summaryMenu = [
            ["tank_summary", "", "", "tank_summary/%s" % node, "simple_table_view"]
        ]

        # Temporarily, add "num" field, it is required to identify the tanks
        # in the diagrams.
        fields["fields"].append("num")

        result = self.executeRawQuery(Tartalyok.objects, queryString, fields["fields"], summaryMenu)

        data = result["data"]

        for set in data:
            tankNum = self.getActualField(set, "num")

            set.insert(1, ["tank_inventory_diagram", "", "", "tank_inventory_diagram/%d" % tankNum, "image_table_view"])
            set.insert(1, ["tank_water_height_diagram", "", "", "tank_water_height_diagram/%d" % tankNum, "image_table_view"])
            set.insert(1, ["tank_temperature_diagram", "", "", "tank_temperature_diagram/%d" % tankNum, "image_table_view"])
            # num should not be present in the result set, but was required to
            # to construct the diagram menus
            self.removeField(set, "num")

        return result

    def addSummaryField(self, results, field):
        sum = 0

        for p in results:
            attr = self.getAttr(p, field)

            if attr:
                sum += attr

        return [field, "", str(sum)]

    def summary(self, node, user):
        fields = self.getFieldsFromDBGrid(node, user, self.DBGRID_TAB_ID)
        queryString = self.getQueryString(node, user, fields["order_by"])
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
            keszlet = self.getAttr(p, "keszlet")
            keszlet15 = self.getAttr(p, "keszlet15")
            max_liter = self.getAttr(p, "max_liter")
            zarolt_l = self.getAttr(p, "zarolt_l")
            sum_keszlet += keszlet
            sum_keszlet15 += keszlet15
            sum_max_liter += max_liter
            sum_zarolt_l += zarolt_l

            ua_tipn = self.getAttr(p, "ua_tipn")

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
            "desc": self.desc,
            "data": [data]
        }

    def getDiagramQueryString(self, fromDate, toDate, tankNum, isMetric):
        if isMetric == "1":
            return '''SELECT a."num", a."dt_num", a."h2o_mm", a."hofok",  a."ua_l", a."ua_l15" from "TLevel" a where (a."dt_num">=%s)and(a."dt_num"<%s)and(a."tartaly"=%s) and (a."delete" is NULL )and(a."kut">80) order by a."dt_num"''' % (fromDate, toDate, tankNum)
        else:
            return '''SELECT a."num", a."tartaly", a."datumido", a."dt_num", a."ua_mm", a."h2o_mm", (((a."hofok")*9)/5)+32 as "hofok", Trunc((a."ua_l")/3.79) as "ua_l", Trunc((a."ua_l15")/3.79) as "ua_l15", a."h2o_l", a."tipus", a."vez", a."kut", a."e_ar", a."gcsop",  a."delete", a.RDB$DB_KEY from "TLevel" a where (a."dt_num">=%s)and(a."dt_num"<%s)and(a."tartaly"=%s) and (a."delete" is NULL )and(a."kut">80) order by a."dt_num"''' % (fromDate, toDate, tankNum)

    def drawDiagram(self, axisDesc, queryString):
        return self.draw(axisDesc, Tlevel.objects.raw(queryString), "tank_diagram")

    def inventoryDiagram(self, fromDate, toDate, tankNum, isMetric, language):
        queryString = self.getDiagramQueryString(
            fromDate, toDate, tankNum, isMetric)

        axisDesc = [
            {
                "column": "ua_l",
                "label": self.getLabels("ua_l", language, isMetric),
                "line": "b-"
            },
            {
                "column": "ua_l15",
                "label": self.getLabels("ua_l15", language, isMetric),
                "line": "g-"
            },
        ]

        return self.drawDiagram(axisDesc, queryString)

    def temperatureDiagram(self, fromDate, toDate, tankNum, isMetric, language):
        queryString = self.getDiagramQueryString(
            fromDate, toDate, tankNum, isMetric)

        axisDesc = [
            {
                "column": "hofok",
                "label": self.getLabels("hofok", language, isMetric),
                "line": "r-"
            }
        ]

        return self.drawDiagram(axisDesc, queryString)

    def waterHeightDiagram(self, fromDate, toDate, tankNum, isMetric, language):
        queryString = self.getDiagramQueryString(
            fromDate, toDate, tankNum, isMetric)

        axisDesc = [
            {
                "column": "h2o_mm",
                "label": self.getLabels("h2o_mm", language, isMetric),
                "line": "b-"
            }
        ]

        return self.drawDiagram(axisDesc, queryString)
