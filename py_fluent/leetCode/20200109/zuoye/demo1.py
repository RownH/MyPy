def isExit(val,values):
    if val in values:
        return isExit(val+0.1,values);
    else:
        return val;

def rankIndex(values,rank):
    lists=[];
    for _ in values:
            lists.append(isExit(sum(_),lists)) 
    listSort=sorted(lists,reverse=False);
    n=listSort[rank-1];
    print(n)
    return lists.index(n);

print(rankIndex([[80,96,81,77],[78,71,93,75],[71,98,70,95],[80,96,89,77],[80,96,81,77],[78,71,93,75]],4));

