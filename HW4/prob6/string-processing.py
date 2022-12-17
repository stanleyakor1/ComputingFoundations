a = 'now is '; b = 'the time '; c = 'to'  # strings being considered
# formated string print operations
print('a\t\t\t: "{}"\nb\t\t\t: "{}"\nc\t\t\t: "{}"\nlen(a)\t\t\t: {}\na[4]\t\t\t: "{}"\na[2:5]\t\t\t: "{}"'.format(a,b,c,len(a),a[4],a[2:5]))
print('c.upper()\t\t: "{}"\nb.startswith("the")\t: {}\na.find("is")\t\t: {}\na+c\t\t\t: "{}"'.format(c.upper(),b.startswith("the"),a.find("is"),a+c))
print('b.replace("t","T")\t: "{}"\na.split()\t\t: {}\nb==c\t\t\t: {}\na.strip()\t\t: "{}"'.format(b.replace("t","T"),a.split(),b==c,a.strip()))


