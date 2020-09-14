class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        
        i, j = 0, 0
        while i < len(l1) or j < len(l2):
            if i == len(l1) and j < len(l2):
                if l2[j].strip("0") != "":
                    return -1
                else:
                    j += 1
            elif j == len(l2) and i < len(l1):
                if l1[i].strip("0") != "":
                    return 1
                else:
                    i += 1
            
            else:
                if int(l1[i].lstrip()) > int(l2[j].lstrip()):
                    return 1
                elif int(l1[i].lstrip()) < int(l2[j].lstrip()):
                    return -1
                else:
                    i += 1
                    j += 1
        return 0
                
            
            
if __name__ == "__main__":
    s = Solution()
    l1 = ["1.01", "1.0", "0.1","1.0.1","7.5.2.4"]
    l2 = ["1.001", "1.0.0", "1.1", "1", "7.5.3"]
    for e1, e2 in zip(l1, l2):
        print(s.compareVersion(e1, e2))