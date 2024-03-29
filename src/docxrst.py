#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
################################################################################
# 
#   Copyright (C) 2014 Daniel Rodriguez
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""Subclass of DocxParser, which is generated by wxFormBuilder."""

import wx
import maingui

from config import ConfigPrefix, ConfigString, ConfigBool
from model import GetDocument

# Implementing DocxParser
class DocxRst(maingui.DocxRst):

    docxfilename = ConfigString(name='docxfilename', defvalue='')
    loadonstart = ConfigBool(name='loadonstart', defvalue=True)
    searchbackwards = ConfigBool(name='searchbackwards', defvalue=False)
    def __init__(self, parent):
        maingui.DocxRst.__init__(self, parent)

        # Non-permanent variables
        self.searching = False

        # Finish init
        self.m_stcDocx.SetWrapMode(1) # 0 - None, 1 - Word, 2 - Char, 3 - Whitespace
        self.m_stcDocx.SetWrapVisualFlags(1) # 0 - None, 1 - end, 2 - begin next, 4 - margin

        # Init Control values
        self.m_filePickerDocx.SetPath(self.docxfilename)
        self.m_checkBoxLoadOnStart.SetValue(self.loadonstart)
        self.m_checkBoxDocxSearchBackwards.SetValue(self.searchbackwards)

        if self.loadonstart and self.docxfilename:
            self.LoadFile()

	
    # Handlers for DocxParser events.
    def OnFileChangedDocx(self, event):
        self.docxfilename = self.m_filePickerDocx.GetPath()
        self.LoadFile()
	
    def OnReloadFile(self, event):
        self.LoadFile()

    def OnCheckBoxLoadOnStart(self, event):
        self.loadonstart = event.IsChecked()
	
    def OnButtonClickExit(self, event):
        self.Destroy()

    def OnMenuSelectionExit(self, event):
        self.Destroy()

    def OnMenuSelectionFind(self, event):
        pass

    def OnCheckBoxDocxSearchBackwards(self, event):
        self.searchbackwards = event.IsChecked()

    def OnCancelButtonDocxFind(self, event):
        self.m_searchCtrlDocx.SetValue('')
        self.searching = False
        
    def OnTextEnterDocxFind(self, event):
        self.SearchText()

    def OnSearchButtonDocxFind(self, event):
        self.SearchText()

    def SearchText(self):
        '''
        Some notes
        -- Searching forward is "straightforward".
        ---- Get the position, set it as anchor and searchanchor and call Searchnext
        ---- If somethig is found
        ---- Go to the position (needed beacuse SetSelection will not scroll
             the selection into view
        ---- Set the selection between foundpos and anchor
        --
        -- Searching backwards needs some adjustment
        ---- The anchor needs to be moved forward before searching because if not
        ---- you will find the same result over and over again
        ---- but it must not be moved the 1st time or else the 1st result
        ---- could be skipped and therefore the check to see if the anchor has
        ---- to be moved
        '''
        searchtext = self.m_searchCtrlDocx.GetValue()
        lsearchtext = len(searchtext)
        curpos = self.m_stcDocx.GetCurrentPos()

        if self.searchbackwards:
            if not self.searching:
                lsearchtext = 0
            curpos = max(0, curpos - lsearchtext)
        
        self.searching = True
        self.m_stcDocx.SetAnchor(curpos)
        self.m_stcDocx.SearchAnchor()

        if not self.searchbackwards:
            start = self.m_stcDocx.SearchNext(0, searchtext)
        else:
            start = self.m_stcDocx.SearchPrev(0, searchtext)

        if start == -1:
            self.m_statusBar.SetStatusText('"%s" not found' % searchtext)
            self.searching = False
            self.m_stcDocx.SetCurrentPos(curpos)
            return

        anchor = self.m_stcDocx.GetAnchor()
        self.m_statusBar.SetStatusText('"%s" found at pos %d / anchor %d' % (searchtext, start, anchor))
        self.m_stcDocx.GotoPos(start) # Needed to bring the position into view
        self.m_stcDocx.SetSelection(start, anchor) # this modifies current pos

    def LoadFile(self):
        self.m_stcDocx.SetReadOnly(False)
        self.m_stcDocx.ClearAll()
        self.m_stcDocx.SetReadOnly(True)
        retcode, retval = GetDocument(self.docxfilename)

        if not retcode:
            wx.MessageBox(str(e), 'Error Loading File')
            return

        unicode_text = retval.decode('utf-8')
        self.m_stcDocx.SetReadOnly(False)
        self.m_stcDocx.SetText(unicode_text)
        self.m_stcDocx.SetReadOnly(True)
