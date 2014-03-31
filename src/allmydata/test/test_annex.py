# -*- coding: utf-8 -*-
# :Progetto:  allmydata-tahoe -- tahoe annex test case
# :Creato:    lun 31 mar 2014 18:17:30 CEST
# :Autore:    Alberto Berti <alberto@metapensiero.it>
#

from twisted.trial import unittest
from twisted.test import proto_helpers

from allmydata.scripts import tahoe_annex


class AnnexTestCase(unittest.TestCase):

    def setUp(self):
        self.proto = tahoe_annex.AnnexServerProtocol()
        self.tr = proto_helpers.StringTransport()

    def test_version(self):
        self.proto.makeConnection(self.tr)
        self.assertEqual(self.tr.value(), 'VERSION 1\n')
