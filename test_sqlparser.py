#!/usr/bin/env python

import os
import unittest

from sqlparser import SqlParser

# fixtures

SELECT = 'select * from books'
SELECT2 = 'select id from books'
SELECT3 = 'select id, name from books'
SELECT4 = 'select b.id, b.name from books b'

class TestSqlParser(unittest.TestCase):

    def testSql(self):
        p = SqlParser()
        results = p.parse(SELECT)
        self.assertEqual(
            str(['select', '*', 'from', 'books']),
            str(results))
        self.assertEqual(results.select_clause, '*')
        self.assertEqual(list(results.from_clause), ['books'])

    def testSql2(self):
        p = SqlParser()
        results = p.parse(SELECT2)
        self.assertEqual(
            str(['select', [['id']], 'from', 'books']),
            str(results))
        self.assertEqual(
            str(results.select_clause),
            str([['id']]))
        self.assertEqual(list(results.from_clause), ['books'])

    def testSql3(self):
        p = SqlParser()
        results = p.parse(SELECT3)
        self.assertEqual(
            str(['select', [['id'], ['name']], 'from', 'books']),
            str(results))
        self.assertEqual(
            str(results.select_clause),
            str([['id'], ['name']]))
        self.assertEqual(list(results.from_clause), ['books'])

    def testSql4(self):
        p = SqlParser()
        results = p.parse(SELECT4)
        self.assertEqual(
            str(['select', [['b.id'], ['b.name']], 'from', 'books', 'b']),
            str(results))
        self.assertEqual(
            str(results.select_clause),
            str([['b.id'], ['b.name']]))
        self.assertEqual(list(results.from_clause), ['books', 'b'])

unittest.main()
