from pyparsing import alphas, alphanums, delimitedList, Group, Literal, \
    Keyword, Optional, Suppress, Word

class SqlParser(object):
    def __init__(self):
        # literals
        star = Literal('*')
        comma = Suppress(',')

        # indentifiers
        identifier = Word(alphas, alphanums+'_').setName('identifier')
        alias      = identifier.copy().setName('alias')

        # select clause
        column_name = identifier.copy().setName('column_name')
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

def test():
    TESTSQL = 'select * from books'

    
    results = SqlParser().parse(TESTSQL);
    print TESTSQL, '->', results

    print 'select_clause:', results.select_clause
    #print '\n'.join(sorted([x for x in dir(results)]))
    print 'from_clause:', results.from_clause
    for token in results:
        print token
        #print dir(token)

if __name__ == '__main__':
    test()
