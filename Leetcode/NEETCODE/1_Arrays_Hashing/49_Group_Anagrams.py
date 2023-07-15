class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for i in strs: 
            a= ''.join(sorted(i))
            print(a)
            if a in table:
                table[a].append(i)
            else:
                table[a] = [i]
        #print(table)
        return table.values()