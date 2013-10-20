import requests
from collections import OrderedDict

a = requests.get('http://bot.notenoughmods.com/1.6.2.json').json()
b = requests.get('http://bot.notenoughmods.com/1.6.4.json').json()

a = {x.pop('name'): x for x in a}
b = {x.pop('name'): x for x in b}

unique_a = set(a) - set(b)
unique_b = set(b) - set(a)

equals = []
diffs = {}

for mod in set(a) & set(b):
    # all mods in here are common, let's compare their info
    if a[mod] == b[mod]:
        # info is the same
        equals.append(mod)
    else:
        # info is different, but what info
        diffs[mod] = {}
        # join their keys and de-duplicate them
        for key in set(a[mod].keys() + b[mod].keys()):
            # we can ignore certain keys
            if key in ('shorturl', 'aliases'):
                continue
            val_a = a[mod].get(key, '')
            val_b = b[mod].get(key, '')
            if val_a != val_b:
                diffs[mod][key] = (val_a, val_b)

print "Unique in A (total %d):" % len(unique_a)
for mod in sorted(unique_a, key=lambda s: s.lower()):
    print mod.encode("utf-8")
print

print "Unique in B (total %d):" % len(unique_b)
for mod in sorted(unique_b, key=lambda s: s.lower()):
    print mod.encode("utf-8")
print

print "Common mods, same information (total %d):" % len(equals)
for mod in sorted(equals, key=lambda s: s.lower()):
    print mod.encode("utf-8")
print

print "Common mods, different info (total %d):" % len(diffs)
for mod, values in OrderedDict(sorted(diffs.items(), key=lambda s: s[0].lower())).iteritems():
    print "%s:" % mod.encode("utf-8")
    for k, v in values.iteritems():
        print "    %s: %s -> %s" % (k, v[0] if v[0] else 'None', v[1] if v[1] else 'None')
