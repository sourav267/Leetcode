class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        lett= []
        for log in logs:
            item = log.split(" ")
            if item[1].isdigit():
                dig.append(log)
            else:
                lett.append((item[0],' '.join(item[1:])))
        lett = sorted(lett, key=lambda x:(x[1],x[0]))
        res = [' '.join(l) for l in lett]
        res.extend(dig)
        return res
                
        