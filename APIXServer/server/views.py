#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
import json

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


def index(request, id):
    json_response = json.dumps(testData[id])
    return HttpResponse(json_response, mimetype='application/json')
