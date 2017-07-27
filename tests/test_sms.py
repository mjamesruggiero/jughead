#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import logging
from context import jughead
from jughead import sms

logging.basicConfig(level=logging.DEBUG, format="%(lineno)d\t%(message)s")

class TestSms(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.config = os.path.join(current_dir, 'data', 'jughead.cfg')

    def test_get_config(self):
        """jughead -- can access config"""
        sut = sms.get_config(self.config)

        self.assertEqual('fake-account', sut.account)
        self.assertEqual('fake-token', sut.token)
        self.assertEqual('+14155551234', sut.from_number)
        self.assertEqual('+15105551234', sut.dest_number)

    def test_bad_filepath_throws(self):
        """jughead -- missing file throws"""
        with self.assertRaises(Exception) as ctx:
            sms.get_config('bad-path')

        self.assertTrue('cannot find file at bad-path' in ctx.exception)
