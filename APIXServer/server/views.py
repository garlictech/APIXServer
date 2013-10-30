#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
from models import Csoportok, Kartyak, Treenode
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


class GetCollection(CommonView):
    def get(self, request, username, password, id):
        logger.info("Get request arrived")
        self.authenticate(username, password)
        if id == "card_details_table":
            data = Kartyak.Details(1, username)
        elif id == "root_table":
            data = Treenode.GetNodes(0, username)
        else:
            data = testData[id]
        json_response = json.dumps(data)
        print json_response
        return HttpResponse(json_response, mimetype='application/json')


class Login(CommonView):
    def get(self, request, username, password):
        self.authenticate(username, password)
        json_response = json.dumps({"authenticated": True})
        return HttpResponse(json_response, mimetype='application/json')
