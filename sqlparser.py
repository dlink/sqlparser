#!/usr/bin/env python

from pyparsing import alphas, alphanums, Combine, delimitedList, Group, \
    Literal, Keyword, Optional, Suppress, Word

class SqlParser(object):

    def __init__(self):
        # literals
        star = Literal('*')
        comma = Suppress(',')

        # indentifiers
        identifier = Word(alphas, alphanums+'_')
        alias      = identifier.copy()

        # select clause
        column_name = Combine(Optional(alias + '.') +
                              identifier +
                              Optional(' as ' + identifier))\
                              .setResultsName('column_name')
        select = Keyword('select', caseless=1)
        select_clause = (star | Group(delimitedList(column_name, comma)))\
            .setResultsName('select_clause')

        # from clause
        from_  = Keyword('from', caseless=1)
        table_name =  delimitedList(identifier + Optional(alias), comma)
        from_clause = table_name.setResultsName('from_clause')

        # select statment
        self.select_stmt = select + select_clause + from_ + from_clause

    def parse(self, sql):
        return self.select_stmt.parseString(sql) 

    def format(self, parser):
        o = ''
        o += 'select\n'
        o += '   ' + ', '.join(map(str, list(
                    [x[0] for x in parser.select_clause]))) + '\n'
        o +=  'from\n'
        o +=  '   ' + ', '.join(map(str, list(parser.from_clause))) + '\n'
        return o


def test():
    TESTSQL = 'select b.id, b.name from books b'
    results = SqlParser().parse(TESTSQL);
    print TESTSQL, '->', results
    print 'select_clause:', results.select_clause
    print 'from_clause:', results.from_clause
    print SqlParser().format(results)

if __name__ == '__main__':
    #test()
    import sys
    filename = sys.argv[1]
    print SqlParser().parse(open(filename, 'r').read())


