#!/usr/bin/python
# -*- coding: utf-8
from models import Vezerlok
from collection import Collection


class Controllers(Collection, Vezerlok):
    desc = {
        "title_id": "controllers",
        "text_id": True
    }

    @staticmethod
    def TypeConverter(t):
        if t == 1:
            return "E95"
        elif t == 2:
            return "Diesel"
        elif t == 3:
            return "Jet"

        return t

    def deleteAllFields(self, result, fieldName):
        for set in result["data"]:
            for line in set:
                for k in range(1, 5):
                    type_id = "t%dn" % k
                    if line[0] == type_id:
                        set.remove(line)
                        self.deleteAllFields(result, fieldName)

    def getQueryString(self, node, user):
        parentStr = self.generateParentString(node)

        return '''select v.* from "Vezerlok" v, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and ("azonosito"<>'') and("tipus"='0') and("user"='%s') Group by "nev"  ) al where (v."nev"=al."nev")and(v."delete"='') order by v."nev"''' % (parentStr, node, user)

    def details(self, node, user):
        queryString = self.getQueryString(node, user)
        summaryMenu = [["controller_summary", "", "", "controller_summary/%s" % node, "simple_table_view"]]

        result = self.executeRawQuery(Vezerlok.objects, queryString, ["icon", "abs_id", "num", "delete", "path", "t1", "t2", "t3", "t4", "l_tip", "com", "cim", "ido", "dl_dt", "com_azon", "time_chk", "bgoz", "b_side_vez", "b_side_p", "p1_sz", "p2_sz", "p3_sz", "p4_sz", "p1_err", "p2_err", "p3_err", "p4_err", "p1_tmr", "p2_tmr", "p3_tmr", "p4_tmr", "sajat", "tipus"], summaryMenu)

        for set in result["data"]:
            name = self.self.getActualField(set, "nev").strip()
            for line in set:
                for n in range(1, 5):
                    type_id = "t%dn" % n
                    pistol_id = "p%d" % n
                    fuel_type = self.getActualField(set, type_id)
                    pistol_num = self.getActualField(set, pistol_id)

                    if line[0] == pistol_id:
                        if line[2]:
                            line[2] = "%d (%s)" % (line[2], Controllers.TypeConverter(fuel_type))

                        if fuel_type == 1:  # 1 means benzin
                            line.append("fuelgas_diagram/%s/%d" % (name, pistol_num))
                            line.append("image_table_view")

        for n in range(1, 5):
            type_id = "t%dn" % n
            self.deleteAllFields(result, type_id)

        return result

    def summary(self, node, user):
        #queryString = self.getQueryString(node, user)
        #results = Vezerlok.objects.raw(queryString)
        data = []

        return {
            "desc": self.desc,
            "data": [data]
        }
