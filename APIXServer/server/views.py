#!/usr/bin/python
# -*- coding: utf-8
from django.http import HttpResponse
from models import Kartyak, Treenode, Tankolasok, Tartalyok, Vezerlok
from models import User as AvisUser
import json
from django.views.generic import View
import logging
from django.core.exceptions import PermissionDenied
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

logger = logging.getLogger(__name__)


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


class GetCardDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, isMetric):
        self.tableStart("GetCards", username, password)
        data = Kartyak.Details(node, username, fromDate, toDate)
        return self.tableEnd(request, data)


class GetRefuelingDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, isMetric):
        self.tableStart("GetRefuelingDetails", username, password)
        data = Tankolasok.Details(node, username, fromDate, toDate, isMetric)
        return self.tableEnd(request, data)


class GetTankDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, isMetric):
        self.tableStart("GetTankDetails", username, password)
        data = Tartalyok.Details(node, username, isMetric)
        return self.tableEnd(request, data)


class GetControllerDetails(CommonView):
    def get(self, request, username, password, fromDate, toDate, node, isMetric):
        self.tableStart("GetControllerDetails", username, password)
        data = Vezerlok.Details(node, username)
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
