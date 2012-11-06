#!/usr/bin/env python

import sys
sys.path.append("/usr/share/xdot") # Debian bug in xdot packaging. cf http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=679532
import gtk
import gtk.gdk
import gobject

try:
    import xdot
except ImportError:
    print("You need xdot to run the topology viewer.\n"
          "On Debian/Ubuntu, apt-get install xdot.")
    sys.exit(1)

import logging; logger = logging.getLogger("underworlds")
logging.basicConfig(level=logging.INFO)

import time

import underworlds
from underworlds.types import *

#colors
COL_WORLDS = "FF9700"
COL_WORLDS_BORDER = "A66200"
COL_CLIENTS = "00AB6F"
COL_EDGES = "0E0874"

class UnderworldsDotWindow(xdot.DotWindow):

    ui = '''
    <ui>
        <toolbar name="ToolBar">
            <toolitem action="Reload"/>
            <separator/>
            <toolitem action="Autorefresh"/>
            <separator/>
            <toolitem action="ZoomIn"/>
            <toolitem action="ZoomOut"/>
            <toolitem action="ZoomFit"/>
            <toolitem action="Zoom100"/>
        </toolbar>
    </ui>
    '''

    def __init__(self):
        xdot.DotWindow.__init__(self)


        self.autorefresh = False

        # Create actions
        actiongroup = gtk.ActionGroup('ReloadAction')
        actiongroup.add_actions((
            ('Reload', gtk.STOCK_REFRESH, None, None, "Reload the topology", self.on_reload),
        ))
        actiongroup.add_toggle_actions((
            ('Autorefresh', gtk.STOCK_MEDIA_PLAY, None, None, "Autorefresh", self.toggle_autorefresh, False),
        ))

        # Add the actiongroup to the uimanager
        self.uimanager.insert_action_group(actiongroup)


        self.widget.connect('clicked', self.on_node_clicked)

        self._ctx = underworlds.Context("topology observer")

    def get_topology(self):
        topo = self._ctx.topology()

        dotcode = "digraph G {\n"

        for w in topo["worlds"]:
            dotcode += '"%s" [color="#%s", shape=box, style=filled];\n' % (w, COL_WORLDS)

        for c in topo["clients"].keys():
            dotcode += '"%s" [color="#%s", style=filled];\n' % (c, COL_CLIENTS)

        for c, links in topo["clients"].items():
            for w, details in links.items():
                type, timestamp = details

                last_activity = time.time() - timestamp
                
                label = "%s\\n(last activity: " % type.lower()
                if last_activity < 2:
                    label += "%d ms" % (last_activity * 1000)
                elif last_activity > 60:
                    label += "%d min" % (last_activity / 60)
                else:
                    label += "%.2f sec" % last_activity
                
                label += " ago)"

                # orient the arrow in the right direction
                if type == READER:
                    edge = '"%s" -> "%s"' % (w, c)
                elif type == MONITOR:
                    edge = '"%s" <-> "%s"' % (w, c)
                else:
                    edge = '"%s" -> "%s"' % (c, w)
                dotcode += edge + ' [label="%s", color="#%s", fontsize=8];\n' % (label, COL_EDGES)

        dotcode += "}\n"

        return dotcode

    def toggle_autorefresh(self, action):
        if self.autorefresh:
            self.autorefresh = False
        else:
            self.autorefresh = True
            gobject.timeout_add(200, self.autoupdate)

    def autoupdate(self):
        self.on_reload(None)
        return self.autorefresh

    def on_reload(self, action):
        self.set_dotcode(self.get_topology())
        self.set_title('Underworlds Topology Viewer')

    def on_node_clicked(self, widget, url, event):
        dialog = gtk.MessageDialog(
                parent = self, 
                buttons = gtk.BUTTONS_OK,
                message_format="%s clicked" % url)
        dialog.connect('response', lambda dialog, response: dialog.destroy())
        dialog.run()
        return True

def main():
    window = UnderworldsDotWindow()
    window.on_reload(None)
    window.connect('destroy', gtk.main_quit)
    gtk.main()

if __name__ == '__main__':
    main()
