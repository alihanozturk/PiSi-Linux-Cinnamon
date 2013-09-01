#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    shelltools.touch("backends/telepathy/lib/tpf-persona.vala")
    autotools.configure("--disable-static \
                         --disable-fatal-warnings \
                         --disable-eds-backend \
                         --disable-telepathy-backend \
                         --enable-vala \
                         --enable-inspect-tool \
                         --disable-libsocialweb-backend")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")