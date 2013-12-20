#!/usr/bin/python
# -*- coding: utf-8
from models import Csoportok
from collection import Collection


class Groups(Collection, Csoportok):
    desc = {
        "title_id": "groups",
        "text_id": True
    }

    def getQueryString(self, node, username):
        parentStr = self.generateParentString(node)

        return '''select v.* from "Csoportok" v, (select "nev" from "TreeNode" where (%s ("dbindx"=%s)) and("delete"='') and ("azonosito"<>'') and ("tipus"='1') and ("user"='%s') Group by "nev") al where (v."nev"=al."nev") order by v."nev";''' % (parentStr, node, username)

    def details(self, username, node):
        queryString = self.getQueryString(node, username)
        summaryMenu = [["group_summary", "", "", "group_summary/%s" % node, "simple_table_view"]]

        return self.executeRawQuery(Csoportok.objects, queryString, ["icon", "sajat"], summaryMenu)

    def summary(self, username, node):
        queryString = self.getQueryString(node, username)
        results = Csoportok.objects.raw(queryString)
        data = [["sGroup", "", sum(1 for result in results)]]

        return {
            "desc": self.desc,
            "data": [data]
        }
