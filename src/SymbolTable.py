'''SymbolTable.py'''
###############################################################################
#                                                                             #
#  SYMBOLS and SYMBOL TABLE                                                   #
#                                                                             #
###############################################################################

from collections import OrderedDict


class Symbol(object):
    def __init__(self, name, _type=None):
        self.name = name
        self.type = _type


class VarSymbol(Symbol):
    def __init__(self, name, _type):
        super().__init__(name, _type)

    def __str__(self):
        return f"<{self.__class__.__name__}(name={self.name}, type={self.type})>"
        #return "<{class_name}(name='{name}', type='{type}')>".format(
        #    class_name=self.__class__.__name__,
        #    name=self.name,
        #    type=self.type,
        #)

    __repr__ = __str__


class BuiltinTypeSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.__class__.__name__}(name={self.name})>"
        #return "<{class_name}(name='{name}')>".format(
        #   class_name=self.__class__.__name__,name=self.name,)


class ProcedureSymbol(Symbol):
    def __init__(self, name, params=None):
        super().__init__(name)        
        # a list of formal parameters
        self.params = params if params is not None else []

    def __str__(self):
        return(f"<{self.__class__.__name__}(name={self.name}, parameters={self.params})>")

        # return '<{class_name}(name={name}, parameters={params})>'.format(
        #     class_name=self.__class__.__name__,
        #     name=self.name,
        #     params=self.params,
        # )

    __repr__ = __str__


class FunctionSymbol(Symbol):  
    def __init__(self, name, _type, params=None):
        super().__init__(name, _type)        

        self.params = params if params is not None else []
        self.type = _type

    def __str__(self):
        return(f"<{self.__class__.__name__}(name={self.name}, parameters={self.params}), returntype={self.type}>")

    __repr__ = __str__


class ScopedSymbolTable(object):
    def __init__(self, scope_name, scope_level, enclosing_scope=None):
        self._symbols = OrderedDict()
        self.scope_name = scope_name
        self.scope_level = scope_level
        self.enclosing_scope = enclosing_scope

    def _init_builtins(self):
        self.insert(BuiltinTypeSymbol('INTEGER'))
        self.insert(BuiltinTypeSymbol('REAL'))
        self.insert(BuiltinTypeSymbol('LONGINT'))

    def __str__(self):
        h1 = 'SCOPE (SCOPED SYMBOL TABLE)'
        lines = ['\n', h1, '=' * len(h1)]
        for header_name, header_value in (
            ('Scope name', self.scope_name),
            ('Scope level', self.scope_level),
            ('Enclosing scope',
             self.enclosing_scope.scope_name if self.enclosing_scope else None
            )
        ):
            lines.append('%-15s: %s' % (header_name, header_value))
        h2 = 'Scope (Scoped symbol table) contents'
        lines.extend([h2, '-' * len(h2)])
        lines.extend(
            ('%7s: %r' % (key, value))
            for key, value in self._symbols.items()
        )
        lines.append('\n')
        s = '\n'.join(lines)
        return s

    __repr__ = __str__


    def insert(self, symbol):
        print('Insert: %s' % symbol.name)
        self._symbols[symbol.name] = symbol


    def lookup(self, name, current_scope_only=False):
        print('Lookup: %s : (Scope name: %s)' % (name, self.scope_name))
        # 'symbol' is either an instance of the Symbol class or None
        symbol = self._symbols.get(name)

        if symbol is not None:
            return symbol

        if current_scope_only:
            return None

        # recursively go up the chain and lookup the name
        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup(name)

