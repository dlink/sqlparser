#!/usr/bin/env python

import os
import unittest

from sqlparser import SqlParser

# fixtures

SELECT = 'select * from books'
SELECT2 = 'select id from books'
SELECT3 = 'select id, name from books'
SELECT4 = 'select b.id, b.name from books b'
SELECT5 = 'select b.id as book_id, b.name as title from books b'

class TestSqlParser(unittest.TestCase):

    def testSql(self):
        self._process(SELECT, ['select', '*', 'from', 'books'], '*', ['books'])

    def testSql2(self):
        self._process(SELECT2,
                     ['select', [['id']], 'from', 'books'],
                     [['id']],
                     ['books'])

    def testSql3(self):
        self._process(SELECT3,
                     ['select', [['id'], ['name']], 'from', 'books'],
                     [['id'], ['name']],
                     ['books'])

    def testSql4(self):
        self._process(SELECT4,
                      ['select', [['b.id'], ['b.name']], 'from', 'books', 'b'],
                      [['b.id'], ['b.name']],
                      ['books', 'b'])


    def testSql5(self):
        self._process(SELECT5,
                      ['select', [['b.id as book_id'], ['b.name as title']],
                       'from', 'books', 'b'],
                      [['b.id as book_id'], ['b.name as title']],
                      ['books', 'b'])

    def _process(self, sql, parsed_sql, select_clause, from_clause):
        p = SqlParser()
        results = p.parse(sql)
        self.assertEqual(str(results), str(parsed_sql))
        self.assertEqual(str(results.select_clause), str(select_clause))
        self.assertEqual(list(results.from_clause), from_clause)

unittest.main()
