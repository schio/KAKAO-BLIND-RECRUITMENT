import re
def solution(str1, str2):
    answer = 0
    intersection={}
    union={}
    str1_list = []
    str2_list = []
    cluster1 = {}
    cluster2 = {}

    ####### preprocessing part #######
    str1 = str1.lower()
    str2 = str2.lower()

    # extraction words to list
    p = re.compile("[a-zA-Z]{2}") # define pattern
    for i in range(len(str1)-1):
        temp=p.findall(str1[i:i+2])
        if len(temp) != 0:
            str1_list.append(temp[0])
    for i in range(len(str2)-1):
        temp=p.findall(str2[i:i+2])
        if len(temp) != 0:
            str2_list.append(temp[0])

    # words count info save to dict
    for i in range(len(str1_list)):
        cluster1[str1_list[i]] = str1_list.count(str1_list[i])

    for i in range(len(str2_list)):
        cluster2[str2_list[i]] = str2_list.count(str2_list[i])


    ####### calculator part #######

    cluster1_key = list(cluster1.keys())
    cluster2_key = list(cluster2.keys())

    #get intersection, union
    for key in cluster1_key:
        if key in cluster2:
            intersection[key] = min(cluster1[key], cluster2[key])
            union[key] = max(cluster1[key], cluster2[key])
        else:
            union[key]=cluster1[key]

    for key in cluster2_key:
        if key in cluster1:
            intersection[key] = min(cluster1[key], cluster2[key])
            union[key] = max(cluster1[key], cluster2[key])
        else:
            union[key]=cluster2[key]

    sum_inter=sum(list(intersection.values()))
    sum_union=sum(list(union.values()))

    if sum_union==0 and sum_inter==0:
        return 65536
    else:
        return int((sum_inter/sum_union)*65536)