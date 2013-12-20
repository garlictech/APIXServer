#!/usr/bin/python
# -*- coding: utf-8
from models import Kartyak
from collection import Collection


class Cards(Collection, Kartyak):
    desc = {
        "title_id": "cards",
        "text_id": True
    }

    def getQueryString(self, node, username, treenodeType):
        if treenodeType == self.COLLECTIONTYPE_USER_GROUPS_ID:
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
        elif treenodeType == self.COLLECTIONTYPE_PLACE_OF_USAGE_ID:
            return '''select v.* from "Kartyak" v, (SELECT p.MYID FROM H_CARD(%s, \'%s\') p) al where (v."id"=al.MYID) order by v."nev";''' % (node, username)

    @staticmethod
    def typeConverter(t):
        if t == "0":
            return "t_master"
        elif t == "1":
            return "t_driver"
        elif t == "2":
            return "t_machine"
        elif t == "4":
            return "t_banned"

        return t

    def details(self, node, username, treenodeType):
        queryString = self.getQueryString(node, username, treenodeType)
        summaryMenu = [["card_summary", "", "", "card_summary/%s/%s" % (node, treenodeType), "simple_table_view"]]
        return self.executeRawQuery(Kartyak.objects, queryString, ["id", "vezerlo", "dt_num", "options", "icon", "actual"], summaryMenu, {'tipus': Cards.typeConverter})

    def summary(self, node, username, treenodeType):
        queryString = self.getQueryString(node, username, treenodeType)
        results = Kartyak.objects.raw(queryString)
        data = []
        sCard = 0
        dCard = 0
        cCard = 0
        mCard = 0
        tCard = 0
        sCsop = {}

        for p in results:
            t = self.getAttr(p, "tipus").strip()
            sCard += 1
            if t == "0":
                mCard += 1
            elif t == "1":
                dCard += 1
            elif t == "2":
                cCard += 1
            elif t == "4":
                tCard += 1

            sCsop[self.getAttr(p, "csoport")] = 1

        data.append(["sCard", "", sCard])
        data.append(["cCard", "", cCard])
        data.append(["dCard", "", dCard])
        data.append(["mCard", "", mCard])
        data.append(["tCard", "", tCard])
        data.append(["sGroup", "", len(sCsop.keys())])

        return {
            "desc": self.desc,
            "data": [data]
        }
