# -*- coding: utf-8 -*-
# :Progetto:  allmydata-tahoe -- tahoe annex test case
# :Creato:    lun 31 mar 2014 18:17:30 CEST
# :Autore:    Alberto Berti <alberto@metapensiero.it>
#

from twisted.trial import unittest
from twisted.test import proto_helpers

from allmydata.scripts import tahoe_annex


class AnnexTestCase(unittest.TestCase):

    def _getLines(self):
        return self.tr.value().strip().split('\n')

    def setUp(self):
        self.proto = tahoe_annex.AnnexServerProtocol()
        self.tr = proto_helpers.StringTransport()

    def test_version(self):
        self.proto.makeConnection(self.tr)
        self.assertEqual(self.tr.value(), 'VERSION 1\n')

    def test_initremote(self):
        self.proto.makeConnection(self.tr)
        self.proto.dataReceived('INITREMOTE\n')
        lines = self._getLines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[-1], 'INITREMOTE-SUCCESS')

    def test_prepare(self):
        self.proto.makeConnection(self.tr)
        self.proto.dataReceived('PREPARE\n')
        lines = self._getLines()
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[-1], 'PREPARE-SUCCESS')

    def test_transfer_store(self):
        import os
        self.proto.makeConnection(self.tr)
        self.proto.dataReceived('PREPARE\n')
        lines = self._getLines()
        self.assertEqual(lines[-1], 'PREPARE-SUCCESS')
        this_file = os.path.abspath(__file__)  # just a file
        self.proto.dataReceived('TRANSFER STORE {0} {1}'.format('1', this_file))
