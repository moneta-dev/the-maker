# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcDIALOG1(wx.Dialog):
#!XRCED:begin-block:xrcDIALOG1.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcDIALOG1.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreDialog()
        self.PreCreate(pre)
        get_resources().LoadOnDialog(pre, parent, "DIALOG1")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.WebView = xrc.XRCCTRL(self, "WebView")
        self.BottomPanel = xrc.XRCCTRL(self, "BottomPanel")
        self.Cancel = xrc.XRCCTRL(self, "Cancel")
        self.Create = xrc.XRCCTRL(self, "Create")

        self.Bind(wx.EVT_BUTTON, self.OnButton_Cancel, self.Cancel)

#!XRCED:begin-block:xrcDIALOG1.OnButton_Cancel
    def OnButton_Cancel(self, evt):
        # Replace with event handler code
        self.Destroy()
        
#!XRCED:end-block:xrcDIALOG1.OnButton_Cancel        




# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    makerTemplateDialog_xrc = '''\
<?xml version="1.0" ?><resource class="wxStaticText">
  <object class="wxDialog" name="DIALOG1">
    <object class="wxBoxSizer">
      <object class="sizeritem">
        <object class="wxPanel">
          <object class="wxStaticText">
            <pos>20, 20</pos>
            <size>700, 40</size>
            <label>Choose a template:</label>
            <style>wxALIGN_CENTRE</style>
            <XRCED>
              <assign_var>1</assign_var>
            </XRCED>
          </object>
          <size>860, 60</size>
          <style>wxBORDER_RAISED</style>
        </object>
        <option>0</option>
        <flag>wxEXPAND|wxGROW</flag>
        <border>1</border>
      </object>
      <object class="sizeritem">
        <object class="wxHtmlWindow" name="WebView">
          <pos>10, 10</pos>
          <size>320, 800</size>
          <style>wxBORDER_SUNKEN</style>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <option>1</option>
        <flag>wxEXPAND|wxGROW|wxADJUST_MINSIZE|wxFIXED_MINSIZE</flag>
        <minsize>800, 600</minsize>
      </object>
      <object class="sizeritem">
        <object class="wxPanel" name="BottomPanel">
          <object class="wxButton" name="Cancel">
            <pos>20, 20</pos>
            <label>Cancel</label>
            <style>wxBU_RIGHT</style>
            <XRCED>
              <events>EVT_BUTTON</events>
              <assign_var>1</assign_var>
            </XRCED>
          </object>
          <object class="wxButton" name="Create">
            <pos>740, 20</pos>
            <label>Create</label>
            <XRCED>
              <assign_var>1</assign_var>
            </XRCED>
          </object>
          <size>860, 70</size>
          <style>wxBORDER_SUNKEN|wxFULL_REPAINT_ON_RESIZE</style>
          <XRCED>
            <assign_var>1</assign_var>
          </XRCED>
        </object>
        <flag>wxGROW|wxADJUST_MINSIZE</flag>
      </object>
      <orient>wxVERTICAL</orient>
      <XRCED>
        <assign_var>1</assign_var>
      </XRCED>
    </object>
    <pos>10, 10</pos>
    <size>860, 800</size>
    <title>Create new project</title>
    <centered>1</centered>
    <enabled>0</enabled>
    <style>wxSTAY_ON_TOP</style>
  </object>
</resource>'''

    wx.MemoryFSHandler.AddFile('XRC/makerTemplateDialog/makerTemplateDialog_xrc', makerTemplateDialog_xrc)
    __res.Load('memory:XRC/makerTemplateDialog/makerTemplateDialog_xrc')


# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("Choose a template:")
    _("Cancel")
    _("Create")
    _("Create new project")

