# -*- coding: utf-8 -*-
# :Progetto:  allmydata-tahoe -- git annex command
# :Creato:    lun 31 mar 2014 18:42:03 CEST
# :Autore:    Alberto Berti <alberto@metapensiero.it>
#

from twisted.internet import stdio, reactor
from twisted.protocols import basic
#from twisted.web import client


class AnnexServerProtocol(basic.LineReceiver):

    delimiter = '\n'

    def connectionMade(self):
        self.sendLine('VERSION 1')

    def lineReceived(self, line):
        if not line.strip():
            return

        parts = line.split()
        cmd = parts[0].upper()
        args = parts[1:]

        if cmd == 'TRANSFER':  # TRANSFER STORE|RETRIEVE
            cmd = '_'.join((cmd, parts[1].upper()))
            args = parts[2:]

        try:
            method = getattr(self, 'do_' + cmd)
        except AttributeError as e:
            raise # todo
        else:
            method(args)

    def do_INITREMOTE(self, args):
        self.sendLine('INITREMOTE-SUCCESS')

    def do_PREPARE(self, args):
        self.sendLine('PREPARE-SUCCESS')


def annex(stdin=0, stdout=1):
    return stdio.StandardIO(AnnexServerProtocol(), stdin, stdout)


if __name__ == "__main__":
    stdio.StandardIO(AnnexServerProtocol())
    reactor.run()
