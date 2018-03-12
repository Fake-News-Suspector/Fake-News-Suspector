import re
pattern="Trump says about border wall"
content={"Trump he rejected Mexico request about border wall","Mexico request about border wall"}
p1=pattern.split(" ")
count=0
count1=0
print(pattern.split(" "))
for i in p1:
    result=re.search(i,content)
    print(result)
    if result!=None:
        count=count+1
##    result1=re.match(i,content)
##    print(result1)
##    if result1!=None:
##        count1=count1+1
print(str(count)+" "+str(count1))
Match_percent=(count/len(p1))
if (count/len(p1)) > 0.75 :
    print(" Found" + str(Match_percent))

