#!/usr/bin/env python

import os
import unittest

from sqlparser import SqlParser

# fixtures

SELECT = 'select * from books'
SELECT2 = 'select id from books'
SELECT3 = 'select id, name from books'
#SELECT4 = 'select b.id as book_id, b.name from books b'

class TestSqlParser(unittest.TestCase):

    def testSql(self):
        p = SqlParser()
        results = p.parse(SELECT)
        self.assertEqual(['select', '*', 'from', 'books'], list(results))
        self.assertEqual(results.select_clause, '*')
        self.assertEqual(results.from_clause, 'books')

    def testSql2(self):
        p = SqlParser()
        results = p.parse(SELECT2)
        self.assertEqual(
            str(['select', ['id'], 'from', 'books']),
            str(results))
        self.assertEqual(list(results.select_clause), ['id'])
        self.assertEqual(results.from_clause, 'books')

    def testSql3(self):
        p = SqlParser()
        results = p.parse(SELECT3)
        self.assertEqual(
            str(['select', ['id', 'name'], 'from', 'books']),
            str(results))
        self.assertEqual(list(results.select_clause), ['id', 'name'])
        self.assertEqual(results.from_clause, 'books')

unittest.main()
