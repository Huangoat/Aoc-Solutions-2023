# Private

def read_file(file):return [line.strip() for line in open(file,"r").readlines()]
def split_chunks(arr, num):
    counter = 0
    lst = [[]]
    for ii,i in enumerate(arr):
        lst[counter].append(i)
        if len(lst[counter]) >= num and  ii!=len(arr)-1:
            lst.append([])
            counter += 1
    return lst
