class MyDict(dict):
    def get(self, key):
        if key in self:
            return self[key]
        else:
            return 0


mydict = MyDict()
mydict['a'] = 1
mydict['b'] = 2

print(mydict.get('a'))
print(mydict.get('c'))
