#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 16:01:11 2019

import wx

from diffpy.pdfgui.gui.datasetconfigurepanel import DataSetConfigurePanel
from diffpy.pdfgui.gui.datasetconstraintpanel import DataSetConstraintPanel
from diffpy.pdfgui.gui.datasetresultspanel import DataSetResultsPanel
from diffpy.pdfgui.gui.pdfpanel import PDFPanel


class DataSetPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: DataSetPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.dataSetNotebook = wx.Notebook(self, wx.ID_ANY, style=0)
        self.configurePage = wx.Panel(self.dataSetNotebook, wx.ID_ANY)
        self.configurePanel = DataSetConfigurePanel(self.configurePage, wx.ID_ANY)
        self.constraintsPage = wx.Panel(self.dataSetNotebook, wx.ID_ANY)
        self.constraintPanel = DataSetConstraintPanel(self.constraintsPage, wx.ID_ANY)
        self.resultsPage = wx.Panel(self.dataSetNotebook, wx.ID_ANY)
        self.resultsPanel = DataSetResultsPanel(self.resultsPage, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onNotebookChanged, self.dataSetNotebook)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: DataSetPanel.__set_properties
        pass
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DataSetPanel.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.configurePanel, 1, wx.EXPAND, 0)
        self.configurePage.SetSizer(sizer_1)
        sizer_6.Add(self.constraintPanel, 1, wx.EXPAND, 0)
        self.constraintsPage.SetSizer(sizer_6)
        sizer_7.Add(self.resultsPanel, 1, wx.EXPAND, 0)
        self.resultsPage.SetSizer(sizer_7)
        self.dataSetNotebook.AddPage(self.configurePage, "Configure")
        self.dataSetNotebook.AddPage(self.constraintsPage, "Constraints")
        self.dataSetNotebook.AddPage(self.resultsPage, "Results")
        sizer_3.Add(self.dataSetNotebook, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

    # USER CONFIGURATION CODE #################################################

    def __customProperties(self):
        self.configuration = {}
        self.constraints = {}
        self.results = {}

    # Methods overloaded from PDFPanel
    def refresh(self):
        self.configurePanel.treeCtrlMain = self.treeCtrlMain
        self.constraintPanel.treeCtrlMain = self.treeCtrlMain
        self.resultsPanel.treeCtrlMain = self.treeCtrlMain
        self.configurePanel.mainFrame = self.mainFrame
        self.constraintPanel.mainFrame = self.mainFrame
        self.resultsPanel.mainFrame = self.mainFrame
        self.configurePanel.configuration = self.configuration
        self.configurePanel.constraints = self.constraints
        self.constraintPanel.constraints = self.constraints
        self.resultsPanel.results = self.results

        # Refresh the visible panel
        self.refreshSelectedPage()
        return

    def refreshSelectedPage(self):
        """Refresh the panel corresponding to the currently selected page."""
        # self.configurePanel.refresh()
        # self.constraintPanel.refresh()
        # self.resultsPanel.refresh()
        id = self.dataSetNotebook.GetCurrentPage().GetId()
        if id == self.configurePage.GetId():
            self.configurePanel.refresh()
        elif id == self.constraintsPage.GetId():
            self.constraintPanel.refresh()
        elif id == self.resultsPage.GetId():
            self.resultsPanel.refresh()
        return id

    # EVENT CODE #############################################################

    def onNotebookChanged(self, event):  # wxGlade: DataSetPanel.<event_handler>
        """Refresh the selected panel."""
        self.refreshSelectedPage()
        return

    # Overloaded from Panel.
    def Enable(self, enable=True):
        """Keep the notebook enabled, just not the panels."""
        self.configurePanel.Enable(enable)
        self.constraintPanel.Enable(enable)
        self.resultsPanel.Enable(enable)
        return


# end of class DataSetPanel
