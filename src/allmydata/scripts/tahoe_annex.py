# -*- coding: utf-8 -*-
# :Progetto:  allmydata-tahoe -- git annex command
# :Creato:    lun 31 mar 2014 18:42:03 CEST
# :Autore:    Alberto Berti <alberto@metapensiero.it>
# :Licenza:   GNU General Public License version 3 or later
#

from twisted.internet import stdio, reactor
from twisted.protocols import basic
#from twisted.web import client


class AnnexServerProtocol(basic.LineReceiver):

    delimiter = '\n'

    def connectionMade(self):
        self.sendLine('VERSION 1')


def annex(stdin=0, stdout=1):
    return stdio.StandardIO(AnnexServerProtocol(), stdin, stdout)


if __name__ == "__main__":
    stdio.StandardIO(AnnexServerProtocol())
    reactor.run()
