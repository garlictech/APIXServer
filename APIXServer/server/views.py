#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
from models import Kartyak, Treenode, Tankolasok, Tartalyok, Vezerlok, Bgoz, Csoportok
from models import User as AvisUser
import json
from django.views.generic import View
import logging
from django.core.exceptions import PermissionDenied


class CommonView(View):
    def authenticate(self, username, password):
        if not AvisUser.isAuthenticated(username, password):
            raise PermissionDenied

    def tableStart(self, label, username, password):
        #logger.info("%s request arrived" % label)
        self.authenticate(username, password)

    def tableEnd(self, request, data):
        json_response = json.dumps(data)
        #print json_response
        return HttpResponse(json_response, mimetype='application/json')


class GetTreeNode(CommonView):
    def get(self, request, username, password, fromDate, toDate, dbindx, treenodeType):
        self.tableStart("GetTreeNode", username, password)
        data = Treenode.GetNodes(username, dbindx, treenodeType)
        return self.tableEnd(request, data)


class GetCardDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetCardDetails", username, password)
        data = Kartyak.Details(node, username, treenodeType)
        return self.tableEnd(request, data)


class GetCardSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetCardSummary", username, password)
        data = Kartyak.Summary(node, username, treenodeType)
        return self.tableEnd(request, data)


class GetRefuelingDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetRefuelingDetails", username, password)
        data = Tankolasok.Details(node, username, fromDate, toDate, treenodeType)
        return self.tableEnd(request, data)


class GetRefuelingSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, treenodeType):
        self.tableStart("GetRefuelingSummary", username, password)
        data = Tankolasok.Summary(node, username, fromDate, toDate, treenodeType)
        return self.tableEnd(request, data)


class GetTankDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetTankDetails", username, password)
        data = Tartalyok.Details(node, username)
        return self.tableEnd(request, data)


class GetTankSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetTankSummary", username, password)
        data = Tartalyok.Summary(node, username)
        return self.tableEnd(request, data)


class GetTankInventoryDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, tankNum, isMetric, language):
        self.tableStart("GetTankInventoryDiagram", username, password)
        data = Tartalyok.InventoryDiagram(fromDate, toDate, tankNum, isMetric, language)
        return self.tableEnd(request, data)


class GetTankWaterHeightDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, tankNum, isMetric, language):
        self.tableStart("GetTankWaterHeightDiagram", username, password)
        data = Tartalyok.WaterHeightDiagram(fromDate, toDate, tankNum, isMetric, language)
        return self.tableEnd(request, data)


class GetTankTemperatureDiagram(CommonView):
    def get(self, request, username, password, fromDate, toDate, tankNum, isMetric, language):
        self.tableStart("GetTankTemperatureDiagram", username, password)
        data = Tartalyok.TemperatureDiagram(fromDate, toDate, tankNum, isMetric,language)
        return self.tableEnd(request, data)


class GetControllerDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetControllerDetails", username, password)
        data = Vezerlok.Details(node, username)
        return self.tableEnd(request, data)


class GetControllerSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetControllerSummary", username, password)
        data = Vezerlok.Summary(node, username)
        return self.tableEnd(request, data)


class GetFuelGasDiagrams(CommonView):
    def get(self, request, username, password, fromDate, toDate, controllerNum, pistolNum, isMetric, language):
        self.tableStart("GetFuelGasDiagrams", username, password)
        data = Bgoz.Diagrams(fromDate, toDate, controllerNum, pistolNum, language)
        return self.tableEnd(request, data)


class GetGroupDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetGroupDetails", username, password)
        data = Csoportok.Details(username, node)
        return self.tableEnd(request, data)


class GetGroupSummary(CommonView):
    def get(self, request, username, password, fromDate, toDate, node):
        self.tableStart("GetGroupSummary", username, password)
        data = Csoportok.Summary(username, node)
        return self.tableEnd(request, data)


class GetRootTable(CommonView):
    def get(self, request, username, password, fromDate, toDate):
        self.tableStart("GetRootTable", username, password)
        data = Treenode.GetRoot(username)
        return self.tableEnd(request, data)


class Login(CommonView):
    def get(self, request, username, password):
        self.tableStart("Login", username, password)
        data = {"authenticated": True}
        return self.tableEnd(request, data)
