import re
format_pat=re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)
logpath = "C:\\Users\M_K_P\Downloads\Compressed\DataScience\DataScience-Python3\\access_log.txt" 
#URLcounts={}
#with open (logpath,"r")as f:
#    for line in (l.rstrip() for l in f):
#        match=format_pat.match(line)
#        if(match):
#           access=match.groupdict()
#          request=access['request']
#           (action,URL,protocol)=request.split()
#            if URLcounts.has_key(URL):
#                URLcounts[URL]=URLcounts[URL]+1
#           else:
#               URLcounts[URL]=1
#results=sorted(URLcounts,key=lambda i: int(URLcounts[i],reverse=True)
#for result in results[ :20]:
#    print(result + " :" +str(URLcounts[result]))  
########
"""URLcounts={}
with open (logpath,"r") as f:
    for line in (l.rstrip() for l in f):
        match=format_pat.match(line)
        if match:
            access=match.groupdict()
            request=access['request']
            fields=request.split()
            if(len(fields)!=3):
                print(fields)
"""
#######
################
"""URLcounts = {}

with open(logpath, "r") as f:
    for line in (l.rstrip() for l in f):
        match= format_pat.match(line)
        if match:
            access = match.groupdict()
            request = access['request']
            fields = request.split()
            if (len(fields) == 3):
                (action, URL, protocol) = fields
                if (action == 'GET'):
                    if URL in URLcounts:
                        URLcounts[URL] = URLcounts[URL] + 1
                    else:
                        URLcounts[URL] = 1

results = sorted(URLcounts, key=lambda i: int(URLcounts[i]), reverse=True)

for result in results[:20]:
    print(result + ": " + str(URLcounts[result]))
"""   
    ###########
    ######
"""UserAgents={}
with open (logpath,"r") as f:
    for line in (l.rstrip() for l in f):
        match=format_pat.match(line)
        if match:
            access=match.groupdict()
            agent=access['user_agent']
            if agent in UserAgents:
                UserAgents[agent]=UserAgents[agent]+1
            else:
                UserAgents[agent]=1
results=sorted(UserAgents,key=lambda i:int(UserAgents[i]),reverse=True)
for result in results:
    print(result+":"+str(UserAgents[result]))
"""
######33
#####3
URLCounts = {}

with open(logpath, "r") as f:
    for line in (l.rstrip() for l in f):
        match= format_pat.match(line)
        if match:
            access = match.groupdict()
            agent = access['user_agent']
            if (not('bot' in agent or 'spider' in agent or 
                    'Bot' in agent or 'Spider' in agent or
                    'W3 Total Cache' in agent or agent =='-')):
                request = access['request']
                fields = request.split()
                if (len(fields) == 3):
                    (action, URL, protocol) = fields
                    if(URL.endswith("/") and not("feed" in URL)):
                        if (action == 'GET'):
                            if URL in URLCounts:
                                URLCounts[URL] = URLCounts[URL] + 1
                            else:
                                URLCounts[URL] = 1

results = sorted(URLCounts, key=lambda i: int(URLCounts[i]), reverse=True)

for result in results[:20]:
    print(result + ": " + str(URLCounts[result]))
