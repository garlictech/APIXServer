#!/usr/bin/python
# -*- coding: utf-8
from models import Tankolasok
from collection import Collection


class Refuelling(Collection, Tankolasok):
    desc = {
        "title_id": "refuellings",
        "text_id": True,
        "sensitiveTo": ['DatesChanged']
    }

    @staticmethod
    def GetQueryString(node, username, fromDate, toDate, treenodeType):
        if treenodeType == Collection.COLLECTIONTYPE_AREA_OF_USAGE_ID:
            return '''SELECT v.* from "Tankolasok" v WHERE (v."dt_num">=%f) and (v."dt_num"<=%f) order by v."dt_num";''' % (float(fromDate), float(toDate))
        elif treenodeType == Collection.COLLECTIONTYPE_USER_GROUPS_ID:
            return '''SELECT v.* from "Tankolasok" v, (SELECT a."abs_id", a."sofor_csop", a."gep_csop",a."sofor_card",a."gep_card" FROM "Tankolasok" a, (SELECT p.MYCSOP, p.MYCARD FROM CS_TANK(%s, \'%s\') p) al WHERE (a."sofor_csop"=al.MYCSOP)or(a."gep_csop"=al.MYCSOP)or(a."sofor_card"=al.MYCARD)or(a."gep_card"=al.MYCARD) GROUP by a."abs_id", a."sofor_csop", a."gep_csop",a."sofor_card",a."gep_card") al2 WHERE v."abs_id"=al2."abs_id"and (v."dt_num">=%f) and (v."dt_num"<=%f) order by v."dt_num";''' % (node, username, float(fromDate), float(toDate))
        elif treenodeType == Collection.COLLECTIONTYPE_PLACE_OF_USAGE_ID:
            return '''SELECT v.* from "Tankolasok" v, (SELECT a."abs_id", a."vezerlo", a."gep_csop",a."kut" FROM "Tankolasok" a, (SELECT p.MYVEZ, p.MYKUT, p.MYCSOP FROM H_TANK(%s, \'%s\', -1) p) al WHERE ((a."vezerlo"=al."MYVEZ")AND(a."kut"=al."MYKUT"))or(a."gep_csop"=al.MYCSOP) GROUP by a."abs_id", a."vezerlo", a."kut", a."gep_csop") al2 WHERE v."abs_id"=al2."abs_id" and(v."dt_num">=%f)and(v."dt_num"<=%f) order by v."dt_num";''' % (node, username, float(fromDate), float(toDate))

    def details(self, node, username, fromDate, toDate, treenodeType):
        queryString = self.GetQueryString(node, username, fromDate, toDate, treenodeType)

        summaryMenu = [["refuelling_summary", "", "", "refueling_summary/%s/%s" % (node, treenodeType), "simple_table_view"]]

        return self.executeRawQuery(Tankolasok.objects, queryString, ["abs_id", "dt_num", "status_c", "s_n_d", "ua_mm", "v_mm", "t_hofok", "e_ar", "status_n", "mil_a"], summaryMenu)

    def summary(self, node, username, fromDate, toDate, treenodeType):
        queryString = self.GetQueryString(node, username, fromDate, toDate, treenodeType)
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
            sLit += self.getAttr(p, "liter")
            sLit15 += self.getAttr(p, "liter15")

            if smLit < sLit:
                smLit = self.getAttr(p, "liter")
                smLit15 = self.getAttr(p, "liter15")

            ua_tipn = self.getAttr(p, "ua_tipn")

            if ua_tipn and ua_tipn == 1:  # Benzin
                bCNT += 1
                bLit += self.getAttr(p, "liter")
                bLit15 += self.getAttr(p, "liter15")

                if bmLit < bLit:
                    bmLit = self.getAttr(p, "liter")
                    bmLit15 = self.getAttr(p, "liter15")

            if ua_tipn and ua_tipn == 2:  # Gasolin
                dCNT += 1
                dLit += self.getAttr(p, "liter")
                dLit15 += self.getAttr(p, "liter15")

                if dmLit < dLit:
                    dmLit = self.getAttr(p, "liter")
                    dmLit15 = self.getAttr(p, "liter15")

            if ua_tipn and ua_tipn == 3:  # Jet
                jCNT += 1
                jLit += self.getAttr(p, "liter")
                jLit15 += self.getAttr(p, "liter15")

                if jmLit < jLit:
                    jmLit = self.getAttr(p, "liter")
                    jmLit15 = self.getAttr(p, "liter15")

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
            "desc": self.desc,
            "data": [data]
        }
