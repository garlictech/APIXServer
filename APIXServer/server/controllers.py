#!/usr/bin/python
# -*- coding: utf-8
from models import Vezerlok
from collection import Collection


class Controllers(Collection, Vezerlok):
    desc = {
        "title_id": "controllers",
        "text_id": True
    }

    DBGRID_TAB_ID = 4

    def deleteAllFields(self, result, fieldName):
        for set in result["data"]:
            for line in set:
                for k in range(1, 5):
                    type_id = "t%dn" % k
                    if line[0] == type_id:
                        set.remove(line)
                        self.deleteAllFields(result, fieldName)

    def getQueryString(self, node, user, order_by):
        parentStr = self.generateParentString(node)

        return '''select v.* from "Vezerlok" v, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and ("azonosito"<>'') and("tipus"='0') and("user"='%s') Group by "nev"  ) al where (v."nev"=al."nev")and(v."delete"='') %s''' % (parentStr, node, user, order_by)

    def details(self, node, user):
        fields = self.getFieldsFromDBGrid(node, user, self.DBGRID_TAB_ID)
        queryString = self.getQueryString(node, user, fields["order_by"])

        #summaryMenu = [["controller_summary", "", "", "controller_summary/%s" % node, "simple_table_view"]]
        summaryMenu = []

        # Add these fields temporarily, required by fuel type calculations.
        # Will be removed from the final result.
        for n in range(1, 5):
            type_id = "t%dn" % n
            fields["fields"].append(type_id)

        result = self.executeRawQuery(Vezerlok.objects, queryString, fields["fields"], summaryMenu)

        for set in result["data"]:
            name = self.getActualField(set, "nev").strip()
            for line in set:
                for n in range(1, 5):
                    type_id = "t%dn" % n
                    pistol_id = "p%d" % n
                    fuel_type = self.getActualField(set, type_id)
                    pistol_num = self.getActualField(set, pistol_id)

                    if line[0] == pistol_id:
                        if line[2]:
                            line[2] = "%d (%s)" % (line[2], Collection.FuelTypeConverter(fuel_type))

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
