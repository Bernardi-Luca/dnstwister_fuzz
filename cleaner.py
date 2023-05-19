fileDomains=open("twistInput","r")
fileTwist=open("twistOut_resolv","r")

domainsLines=fileDomains.read()
twistLines=fileTwist.readlines()

fileOut=open("twist_no_orig","a")

for line in twistLines:
        line2=line.split("-->")[0].strip().lower()
        if line2 not in domainsLines:
                print(line)
                fileOut.write(line)

fileDomains.close()
fileTwist.close()
fileOut.close()
