def pageFaults(self, N, C, pages):
        arr=[]
        page_fault=0
        
        for i in pages:
            if i not in arr:
                if len(arr)==C:
                    arr.pop(0)
                    arr.append(i)
                else:
                    arr.append(i)
                page_fault+=1
            else:
                arr.remove(i)
                arr.append(i)
        return page_fault

