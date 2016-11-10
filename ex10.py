# escapes


tabby_Cat = "\tI'm tabbed in"
persian_Cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_Cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_Cat
print persian_Cat
print backslash_cat
print fat_Cat


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
