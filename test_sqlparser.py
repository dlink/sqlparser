#!/usr/bin/env python

import os
import unittest

from sqlparser import SqlParser

# fixtures

SELECT = 'select * from books'
SELECT2 = 'select id from books'
#SELECT3 = 'select b.id as book_id, b.name from books b'

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
            ['select', 'id', 'from', 'books'],
            list(results))
        self.assertEqual(results.select_clause, 'id')
        self.assertEqual(results.from_clause, 'books')

unittest.main()
