#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
from controllers import Controllers
from treenode import Treenode
from refuelling import Refuelling
from fuelgas import Fuelgas
from groups import Groups
from cards import Cards
from tanks import Tanks
from models import User as AvisUser
import json
from django.views.generic import View
from django.core.exceptions import PermissionDenied


class CommonView(View):
    def authenticate(self, username, password):
        if not AvisUser.isAuthenticated(username, password):
            raise PermissionDenied

    def tableStart(self, label, username, password):
        self.authenticate(username, password)

    def tableEnd(self, request, data):
        json_response = json.dumps(data)
        #print json_response
        return HttpResponse(json_response, mimetype='application/json')


class GetTreeNode(CommonView):
    def get(self, request, username, password, fromDate, toDate, dbindx, treenodeType):
        self.tableStart("GetTreeNode", username, password)
        data = Treenode().getNodes(username, dbindx, treenodeType)
        return self.tableEnd(request, data)


class GetCardDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetCardDetails", username, password)
        data = Cards().details(node, username, treenodeType)
        return self.tableEnd(request, data)


class GetCardSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetCardSummary", username, password)
        data = Cards().summary(node, username, treenodeType)
        return self.tableEnd(request, data)


class GetRefuelingDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetRefuelingDetails", username, password)
        data = Refuelling().details(node, username, fromDate, toDate, treenodeType)
        return self.tableEnd(request, data)


class GetRefuelingSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetRefuelingSummary", username, password)
        data = Refuelling().summary(node, username, fromDate, toDate, treenodeType)
        return self.tableEnd(request, data)


class GetTankDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetTankDetails", username, password)
        data = Tanks().details(node, username)
        return self.tableEnd(request, data)


class GetTankSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetTankSummary", username, password)
        data = Tanks().summary(node, username)
        return self.tableEnd(request, data)


class GetTankInventoryDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, tankNum, isMetric, language):
        self.tableStart("GetTankInventoryDiagram", username, password)
        data = Tanks().inventoryDiagram(fromDate, toDate, tankNum, isMetric, language)
        return self.tableEnd(request, data)


class GetTankWaterHeightDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, tankNum, isMetric, language):
        self.tableStart("GetTankWaterHeightDiagram", username, password)
        data = Tanks().waterHeightDiagram(fromDate, toDate, tankNum, isMetric, language)
        return self.tableEnd(request, data)


class GetTankTemperatureDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, tankNum, isMetric, language):
        self.tableStart("GetTankTemperatureDiagram", username, password)
        data = Tanks().temperatureDiagram(fromDate, toDate, tankNum, isMetric, language)
        return self.tableEnd(request, data)


class GetControllerDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetControllerDetails", username, password)
        data = Controllers().details(node, username)
        return self.tableEnd(request, data)


class GetControllerSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetControllerSummary", username, password)
        data = Controllers().summary(node, username)
        return self.tableEnd(request, data)


class GetFuelGasDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, controllerNum, pistolNum, isMetric, language):
        self.tableStart("GetFuelGasDiagram", username, password)
        data = Fuelgas().diagram(fromDate, toDate, controllerNum, pistolNum, language)
        return self.tableEnd(request, data)


class GetGroupDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetGroupDetails", username, password)
        data = Groups().details(username, node)
        return self.tableEnd(request, data)


class GetGroupSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetGroupSummary", username, password)
        data = Groups().summary(username, node)
        return self.tableEnd(request, data)


class GetRootTable(CommonView):
    def get(self, request, username, password, fromDate, toDate):
        self.tableStart("GetRootTable", username, password)
        data = Treenode().getRoot(username)
        return self.tableEnd(request, data)


class Login(CommonView):
    def get(self, request, username, password):
        self.tableStart("Login", username, password)
        data = {"authenticated": True}
        return self.tableEnd(request, data)
