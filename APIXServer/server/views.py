#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
from models import Kartyak, Treenode, Tankolasok
from models import User as AvisUser
import json
from django.views.generic import View
import logging
from django.core.exceptions import PermissionDenied

logger = logging.getLogger(__name__)

testData = {}

testData["sites_table"] = [[
    ["Bp, Budaörsi út", "images/db_icons/1.png", "", "queries_collection"],
    ["Bp, Kerepesi út", "images/db_icons/1.png"]
]]

testData["places_table"] = [[
    ["Budapest", "images/db_icons/1.png", "", "sites_collection"],
    ["Bánkút", "images/db_icons/2.png"]
]]

testData["refuelling_details_table"] = [[
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["diagram", "", "", "image_data"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
        ["detail", "", "value1"],
    ],

    [
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["diagram", "", "", "image_data"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
        ["detail", "", "value2"],
    ],

    [
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["diagram", "", "", "image_data"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
        ["detail", "", "value3"],
    ]
]

testData["groups_table"] = [[
    ["Nagy Csoport", "images/db_icons/1.png"],
    ["Kis Csoport", "images/db_icons/2.png"]
]]

testData["fuelgas_table"] = [[
    ["date", "", "2013.10.27 12:42"],
    ["controller_name", "", "name"],
    ["nozzle_number", "", "2"],
    ["fuelgas_suction", "", "78"],
    ["errorneous_suction", "", "78"],
    ["counter_before_stop", "", "45"]
]]


class CommonView(View):
    def authenticate(self, username, password):
        if not AvisUser.isAuthenticated(username, password):
            raise PermissionDenied

    def tableStart(self, label, username, password):
        logger.info("%s request arrived" % label)
        self.authenticate(username, password)

    def tableEnd(self, request, data):
        json_response = json.dumps(data)
        #print json_response
        return HttpResponse(json_response, mimetype='application/json')


class GetTreeNode(CommonView):
    def get(self, request, username, password, fromDate, toDate, dbindx, isMetric):
        self.tableStart("GetTreeNode", username, password)
        data = Treenode.GetNodes(username, dbindx)
        return self.tableEnd(request, data)


class GetCards(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetCards", username, password)
        data = Kartyak.Details(node, username)
        return self.tableEnd(request, data)


class GetRefuelingDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, isMetric):
        self.tableStart("GetRefuelingDetails", username, password)
        data = Tankolasok.Details(node, username, fromDate, toDate, isMetric)
        return self.tableEnd(request, data)


class GetRootTable(CommonView):
    def get(self, request, username, password, fromDate, toDate, isMetric):
        self.tableStart("GetRootTable", username, password)
        data = Treenode.GetRoot(username)
        return self.tableEnd(request, data)


class Login(CommonView):
    def get(self, request, username, password):
        self.tableStart("Login", username, password)
        data = {"authenticated": True}
        return self.tableEnd(request, data)
