#!/usr/bin/python
# -*- coding: utf-8
from models import TreenodeModel
from collection import Collection


class Treenode(Collection, TreenodeModel):
    desc = {
        "title_id": "data",
        "text_id": True
    }

    def getRoot(self, username):
        nodes = Treenode.GetRawNodes(username, -1)
        data = []

        for node in nodes:
            data.append([node.nev, self.IconDB.icon(node.icon), "", "treenode/%d/%d" % (node.dbindx, node.dbindx), "simple_table_view"])

        return {
            "desc": self.desc,
            "data": [data]
        }

    def getNodes(self, username, dbindx, collectionType):
        data = self.getData(username, dbindx, collectionType)

        return {
            "desc": self.desc,
            "data": [data]
        }

    @staticmethod
    def GetRawNodes(username, dbindx):
        return TreenodeModel.objects.filter(
            user=username, parent0=dbindx, delete=""
        ).order_by('nev')

    def getData(self, username, dbindx, collectionType):
        nodes = Treenode.GetRawNodes(username, dbindx)
        data = []

        if collectionType == Collection.COLLECTIONTYPE_AREA_OF_USAGE_ID:
            data.append(["refuellings", "", "", "refueling_details/%s/%s" % (dbindx, Collection.COLLECTIONTYPE_AREA_OF_USAGE_ID), "compound_table_view"])
        elif collectionType == Collection.COLLECTIONTYPE_USER_GROUPS_ID:
            data.append(["refuellings", "", "", "refueling_details/%s/%s" % (dbindx, Collection.COLLECTIONTYPE_USER_GROUPS_ID), "compound_table_view"])
            data.append(["cards", "", "", "card_details/%s/%s" % (dbindx, Collection.COLLECTIONTYPE_USER_GROUPS_ID), "compound_table_view"])
            data.append(["groups", "", "", "group_details/%s" % (dbindx), "compound_table_view"])
        elif collectionType == Collection.COLLECTIONTYPE_PLACE_OF_USAGE_ID:
            data.append(["refuellings", "", "", "refueling_details/%s/%s" % (dbindx, Collection.COLLECTIONTYPE_PLACE_OF_USAGE_ID), "compound_table_view"])
            data.append(["cards", "", "", "card_details/%s/%s" % (dbindx, Collection.COLLECTIONTYPE_PLACE_OF_USAGE_ID), "compound_table_view"])
            data.append(["tanks", "", "", "tank_details/%s" % (dbindx), "compound_table_view"])
            data.append(["controllers", "", "", "controller_details/%s" % (dbindx), "compound_table_view"])
        elif dbindx != "-1":
            data = [
                ["refuellings", "", "", "refueling_details/%s/%s" % (dbindx, collectionType), "compound_table_view"],
                ["cards", "", "", "card_details/%s/%s" % (dbindx, collectionType), "compound_table_view"],
                ["tanks", "", "", "tank_details/%s" % dbindx, "compound_table_view"],
                ["controllers", "", "", "controller_details/%s" % dbindx, "compound_table_view"]
            ]

        data.append(["new_section"])

        for node in nodes:
                data.append([node.nev, self.IconDB.icon(node.icon), "", "treenode/%s/%s" % (node.dbindx, collectionType), "simple_table_view"])

        return data
