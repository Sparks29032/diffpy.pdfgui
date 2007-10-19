#!/usr/bin/env python
########################################################################
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
########################################################################

# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.4 on Mon Oct 30 10:53:19 2006

import wx
from copy import copy
import math
from diffpy.pdfgui.control.controlerrors import *
from pdfpanel import PDFPanel

class SGConstrainDialog(wx.Dialog, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: SGConstrainDialog.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "Space Group Constraints")
        self.numConstrainedLabel = wx.StaticText(self, -1, "")
        self.sgLabel = wx.StaticText(self, -1, "Space Group")
        self.sgComboBox = wx.ComboBox(self, -1, choices=["P1"], style=wx.CB_DROPDOWN)
        self.offsetLabel = wx.StaticText(self, -1, "Origin Offset")
        self.offsetTextCtrlX = wx.TextCtrl(self, -1, "0")
        self.offsetTextCtrlY = wx.TextCtrl(self, -1, "0")
        self.offsetTextCtrlZ = wx.TextCtrl(self, -1, "0")
        self.positionCheckBox = wx.CheckBox(self, -1, "constrain positions")
        self.tfCheckBox = wx.CheckBox(self, -1, "constrain temperature factors")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.okButton = wx.Button(self, wx.ID_OK, "OK")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.onSGTextEnter, self.sgComboBox)
        self.Bind(wx.EVT_COMBOBOX, self.onSGSelect, self.sgComboBox)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOXTextEnter, self.offsetTextCtrlX)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOYTextEnter, self.offsetTextCtrlY)
        self.Bind(wx.EVT_TEXT_ENTER, self.onOZTextEnter, self.offsetTextCtrlZ)
        self.Bind(wx.EVT_CHECKBOX, self.onPosFlag, self.positionCheckBox)
        self.Bind(wx.EVT_CHECKBOX, self.onTempFlag, self.tfCheckBox)
        self.Bind(wx.EVT_BUTTON, self.onCancel, id=wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.onOk, id=wx.ID_OK)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: SGConstrainDialog.__set_properties
        self.SetTitle("Space Group Constraints")
        self.sgComboBox.SetSelection(0)
        self.positionCheckBox.SetValue(1)
        self.tfCheckBox.SetValue(1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SGConstrainDialog.__do_layout
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.numConstrainedLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.sgLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_3.Add(self.sgComboBox, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_4.Add(self.offsetLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.offsetTextCtrlX, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.offsetTextCtrlY, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4.Add(self.offsetTextCtrlZ, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_2.Add(self.positionCheckBox, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add(self.tfCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_4_copy.Add((0, 0), 1, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_4_copy.Add(self.cancelButton, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_4_copy.Add(self.okButton, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_2.Add(sizer_4_copy, 0, wx.EXPAND, 0)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        sizer_2.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    ###########################################################################

    def __customProperties(self):
        """Set the custom properties."""
        # setting of combo box items was deferred to updateSpaceGroupList()
        self.spacegroup = None
        self.offset = [0.0,0.0,0.0]
        self.posflag = True
        self.tempflag = True
        self.structure = None
        self.indices = []

        self.textCtrls = [self.offsetTextCtrlX, self.offsetTextCtrlY,
                self.offsetTextCtrlZ]

        # Set the focus events.
        for textctrl in self.textCtrls:
            textctrl.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus) 
        self.sgComboBox.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus) 
        return

    def updateSpaceGroupList(self):
        """Update space group choices in combobox according to
        self.structure.getSpaceGroupList().
        Requires that structure attribute is defined.
        """
        self.sgComboBox.Clear()
        sglist = self.structure.getSpaceGroupList()
        self.spacegroup = self.structure.getSpaceGroup('P1')
        for sg in sglist:
            self.sgComboBox.Append(sg.short_name)
        return

    def setStructure(self, structure):
        """Set the structure and update the widgets."""
        self.structure = structure
        self.updateSpaceGroupList()
        sgname = self.structure.pdffit.get("spcgr")
        offset = self.structure.pdffit.get("sgoffset")
        if sgname:
            self.sgComboBox.SetValue(sgname)
        if offset:
            self.offsetTextCtrlX.SetValue(str(offset[0]))
            self.offsetTextCtrlY.SetValue(str(offset[1]))
            self.offsetTextCtrlZ.SetValue(str(offset[2]))
        self.updateWidgets()
        return

    def getSpaceGroup(self):
        """Get the current space group."""
        return self.spacegroup

    def getOffset(self):
        """Get the offset."""
        return self.offset

    def getPosFlag(self):
        """Get whether the positions should be constrained."""
        return self.posflag

    def getTempFlag(self):
        """Get whether the positions should be constrained."""
        return self.tempflag

    def updateWidgets(self):
        """Update the widgets."""
        # Update space group
        sgname = self.sgComboBox.GetValue()
        try:
            sgname = int(sgname)
        except ValueError:
            pass
        self.spacegroup = self.structure.getSpaceGroup(sgname)
        self.sgComboBox.SetValue(self.spacegroup.short_name)
        # Update offset
        for i in range(3):
            textctrl = self.textCtrls[i]
            val = textctrl.GetValue()
            # make sure the value is meaningful
            try:
                val = float(eval("1.0*"+val, dict(math.__dict__)))
            except (NameError, TypeError, SyntaxError):
                val = 0
            textctrl.SetValue("%s"%val)
            self.offset[i] = val

        # Check the space group
        error = ""
        if sgname != self.spacegroup.short_name and \
            sgname != self.spacegroup.number:
            error = "Space group %s does not exist." % sgname

        # Get a copy of our structure
        #stemp = copy(self.structure)
        ## Expand the structure
        #stemp.applySymmetryConstraints(self.spacegroup, self.indices,
        #                self.posflag, self.tempflag, self.offset)

        #newatoms = len(stemp) - len(self.structure)
        s = ""
        if len(self.indices) != 1:
            s = "s"
        message = "%i atom%s selected." %\
                (len(self.indices), s)
        self.numConstrainedLabel.SetLabel(message)

        # Raise an error if we had to change the space group
        if error:
            raise ControlValueError(error);
        return

    ### Events

    def onKillFocus(self, event):
        """Check value of widgets and update the dialog message."""
        self.updateWidgets()
        return

    def onSGTextEnter(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.updateWidgets()
        return

    def onOXTextEnter(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.updateWidgets()
        return

    def onOYTextEnter(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.updateWidgets()
        return

    def onOZTextEnter(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.updateWidgets()
        return

    def onSGSelect(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.updateWidgets()
        return

    def onOk(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        # check to see if the space group is consistant
        if not self.structure.isSpaceGroupPossible(self.spacegroup):
            message =  "The chosen space group is not consistent\n"
            message += "with the lattice parameters.\n"
            message += "Would you like to proceed anyways?"
            d = wx.MessageDialog( self, message, 
                    "Inconsistent space group", wx.YES_NO)
            code = d.ShowModal()
            if code == wx.ID_YES:
                self.EndModal(wx.ID_OK)
        else:
            self.EndModal(wx.ID_OK)
        return

    def onCancel(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        event.Skip()
        return

    def onPosFlag(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.posflag = self.positionCheckBox.GetValue()
        return

    def onTempFlag(self, event): # wxGlade: SGConstrainDialog.<event_handler>
        self.tempflag = self.tfCheckBox.GetValue()
        return

# end of class SGConstrainDialog
__id__ = "$Id$"
