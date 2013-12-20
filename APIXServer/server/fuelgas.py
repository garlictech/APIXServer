#!/usr/bin/python
# -*- coding: utf-8
from models import Bgoz
from collection import Collection


class Fuelgas(Collection, Bgoz):
    desc = {
        "title_id": "fuelgas_diagram",
        "text_id": True,
        "sensitiveTo": ['DatesChanged']
    }

    def getQueryString(self, fromDate, toDate, controllerNum, pistolNum):
        return '''SELECT * from "Bgoz" where ("dt_num">=%s)and("dt_num"<%s)and("vez"='%s')and("piszt"=%s) and ("ervenyes"<>'') order by "dt_num";''' % (toDate, fromDate, controllerNum, pistolNum)

    def diagram(self, fromDate, toDate, controllerNum, pistolNum, language):
        queryString = self.getQueryString(
            fromDate, toDate, controllerNum, pistolNum
        )

        axisDesc = [
            {
                "column": "szazalek",
                "label": self.getLabels("szazalek", language),
                "line": "b-"
            },
            {
                "column": "hiba",
                "label": self.getLabels("hiba", language),
                "line": "r-"
            }
        ]

        return self.draw(axisDesc, Bgoz.objects.raw(queryString), "fuelgas_percentage_diagram", [-5, 140])
