# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.stc

###########################################################################
## Class DocxRst
###########################################################################

class DocxRst ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DocxRst", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_stcDocx = wx.stc.StyledTextCtrl(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,300 ), wx.TE_READONLY)
		bSizer12.Add( self.m_stcDocx, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline5, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxDocxSearchBackwards = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Backwards", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_checkBoxDocxSearchBackwards, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_searchCtrlDocx = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrlDocx.ShowSearchButton( True )
		self.m_searchCtrlDocx.ShowCancelButton( True )
		bSizer15.Add( self.m_searchCtrlDocx, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer12.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline3, 0, wx.EXPAND, 5 )
		
		self.m_filePickerDocx = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.docx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_DEFAULT_STYLE )
		bSizer12.Add( self.m_filePickerDocx, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer12.Add( self.m_staticline4, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxLoadOnStart = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Load File on Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_checkBoxLoadOnStart, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button7 = wx.Button( self.m_panel1, wx.ID_ANY, u"Reload File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self.m_panel1, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer12 )
		self.m_panel1.Layout()
		bSizer12.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu1.AppendSeparator()
		
		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"E&xit"+ u"\t" + u"Alt-x", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem2 )
		
		self.m_menubar1.Append( self.m_menu1, u"&File" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"&Find"+ u"\t" + u"Alt-f", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu2, u"&Edit" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBoxDocxSearchBackwards.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxDocxSearchBackwards )
		self.m_searchCtrlDocx.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnCancelButtonDocxFind )
		self.m_searchCtrlDocx.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSearchButtonDocxFind )
		self.m_searchCtrlDocx.Bind( wx.EVT_TEXT_ENTER, self.OnTextEnterDocxFind )
		self.m_filePickerDocx.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedDocx )
		self.m_checkBoxLoadOnStart.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxLoadOnStart )
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnReloadFile )
		self.m_button8.Bind( wx.EVT_BUTTON, self.OnButtonClickExit )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionExit, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionFind, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		# Disconnect Events
		self.m_checkBoxDocxSearchBackwards.Unbind( wx.EVT_CHECKBOX, None )
		self.m_searchCtrlDocx.Unbind( wx.EVT_SEARCHCTRL_CANCEL_BTN, None )
		self.m_searchCtrlDocx.Unbind( wx.EVT_SEARCHCTRL_SEARCH_BTN, None )
		self.m_searchCtrlDocx.Unbind( wx.EVT_TEXT_ENTER, None )
		self.m_filePickerDocx.Unbind( wx.EVT_FILEPICKER_CHANGED, None )
		self.m_checkBoxLoadOnStart.Unbind( wx.EVT_CHECKBOX, None )
		self.m_button7.Unbind( wx.EVT_BUTTON, None )
		self.m_button8.Unbind( wx.EVT_BUTTON, None )
		self.Unbind( wx.EVT_MENU, id = self.m_menuItem2.GetId() )
		self.Unbind( wx.EVT_MENU, id = self.m_menuItem3.GetId() )
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheckBoxDocxSearchBackwards( self, event ):
		event.Skip()
	
	def OnCancelButtonDocxFind( self, event ):
		event.Skip()
	
	def OnSearchButtonDocxFind( self, event ):
		event.Skip()
	
	def OnTextEnterDocxFind( self, event ):
		event.Skip()
	
	def OnFileChangedDocx( self, event ):
		event.Skip()
	
	def OnCheckBoxLoadOnStart( self, event ):
		event.Skip()
	
	def OnReloadFile( self, event ):
		event.Skip()
	
	def OnButtonClickExit( self, event ):
		event.Skip()
	
	def OnMenuSelectionExit( self, event ):
		event.Skip()
	
	def OnMenuSelectionFind( self, event ):
		event.Skip()
	

