class UnionFind:
    def __init__(self, lst):
        self.parent = {}
        for acc in lst:
            for i in range(1, len(acc)):
                self.parent[acc[i]] = acc[i]
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return 
        
        self.parent[py] = px

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}

        uf = UnionFind(accounts)

        for acc in accounts:
            curr_name = acc[0]
            for i in range(1, len(acc)):
                uf.union(acc[1], acc[i])
                email_to_name[acc[i]] = curr_name
        
        d = {}
        res = []
        
        for k in uf.parent.keys():
            if uf.find(k) == k:
                d[k] = []
        
        for email in uf.parent:
                root = uf.find(email)
                d[root].append(email)
        
        for group in d.values():
            res.append([email_to_name[group[0]]] + sorted(group))
        
        return res
                