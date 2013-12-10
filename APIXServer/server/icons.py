#!/usr/bin/python
# -*- coding: utf-8
from django.conf import settings
from PIL import Image
import os
import StringIO
import base64


class Icons():
    def __init__(self):
        self.icons = []
        self.iconPath = os.path.join(settings.PROJECT_ROOT, "APIXServer", "icons")
        helyszCnt = self.loadIcons(400, 500)
        csopCnt = self.loadIcons(0, 200)
        # Create group icons
        self.createCompositeIcons(408, 'GrpIco.ico', helyszCnt, csopCnt)
        # Create controller icons
        self.createCompositeIcons(403, 'DefUnit48.ico', helyszCnt, csopCnt)
        # Create tank icons
        self.createCompositeIcons(405, 'DefTank48.ico', helyszCnt, csopCnt)
        # Create task icons
        self.createCompositeIcons(409, 'DefTask48.ico', helyszCnt, csopCnt)
        self.loadIcons(200, 300)

        for i in range(0, len(self.icons)):
            output = StringIO.StringIO()
            self.icons[i].save(output, "jpeg")
            im_data = output.getvalue()
            self.icons[i] = base64.b64encode(im_data)

    def createCompositeIcons(self, iconNum, overlayIconName, x, y):
        self.loadIcons(iconNum, iconNum + 1)
        overlayIcon = self.getOverlayIcon(overlayIconName)

        for i in range(x, y):
            self.icons.append(self.overlayIcon(self.icons[i], overlayIcon))

        return len(self.icons)

    def loadIcons(self, x, y):
        for i in range(x, y):
            icon = self.getIcon(i)

            if icon:
                self.icons.append(icon)

        return len(self.icons)

    def openIconFile(self, iconFileName):
        filename = os.path.join(self.iconPath, iconFileName)
        return Image.open(filename)

    def getIcon(self, iconNum):
        try:
            return self.openIconFile("%03d.ico" % iconNum)
        except:
            return None

    def getOverlayIcon(self, iconName):
        return self.openIconFile(iconName) if iconName else None

    def overlayIcon(self, bottomIcon, topIcon):
        return Image.alpha_composite(bottomIcon, topIcon)

    def icon(self, index):
        return self.icons[index]
