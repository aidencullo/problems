# from typing import Optional, List, Tuple
# from collections import defaultdict

# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         def get_emails(index):
#             return accounts[index][1:]
            
#         def dfs(index):
#             visited.add(index)
#             results = [index]
#             for email in get_emails(index):
#                 for edge in edges[email]:
#                     if not edge in visited:
#                         results.extend(dfs(edge))
#             return results
        
#         edges = defaultdict(list)

#         # O(E)
#         for index, account in enumerate(accounts):
#             emails = account[1:]
#             for email in emails:
#                 edges[email].append(index)

#         cliques = []
#         visited = set()
#         for index, account in enumerate(accounts):
#             if not index in visited:
#                 cliques.append(dfs(index))

#         results = []
#         for clique in cliques:
#             name = accounts[clique[0]][0]
#             new_account = [name]
#             for member in clique:
#                 account = accounts[member]
#                 emails = account[1:]
#                 new_account.extend(emails)
#             results.append(new_account)

#         for result in results:
#             result[1:] = sorted(list(set(result[1:])))
                
#         return results






# ## Solution 2
# # 
# from typing import Optional, List, Tuple
# from collections import defaultdict

# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         uf = UnionFind(len(accounts)) # O(log V)
#         email_to_accts = {}
#         for acct_index, acct in enumerate(accounts): # O(V + ElogV)
#             for email in acct[1:]:
#                 if email in email_to_accts:
#                     uf.union_find(email_to_accts[email], acct_index) # O(logV)
#                 else:
#                     email_to_accts[email] = acct_index

#         results_dict = defaultdict(list)
#         for acct_index, acct in enumerate(accounts): # O(VlogV + V + E)
#             results_dict[uf.find(acct_index)].extend(acct[1:])

#         results = []
#         for key, el in results_dict.items(): # O(V + E + V + ElogE) -> O(V + ElogE)
#             result_account = []
#             result_account.append(accounts[key][0])
#             result_account.extend(sorted(set(el)))
#             results.append(result_account)


#         print(f'{uf.par=}')
            
#         return results


# class UnionFind:

#     def __init__(self, n):
#         self.par = list(range(n))
#         self.rank = [1] * n

#     def find(self, x):
#         while x != self.par[x]:
#             x = self.par[x]
#         return x

#     def union_find(self, x, y):
#         par_x = self.find(x)
#         par_y = self.find(y)

#         if self.rank[par_x] > self.rank[par_y]:
#             self.par[par_y] = par_x
#             self.rank[par_x] += self.rank[par_y]
#         else:
#             self.par[par_x] = par_y
#             self.rank[par_y] += self.rank[par_x]












 

## Solution 3
# 
from typing import Optional, List, Tuple
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts)) # O(log V)
        email_to_accts = {}
        for acct_index, acct in enumerate(accounts): # O(V + ElogV)
            for email in acct[1:]:
                if email in email_to_accts:
                    uf.union_find(email_to_accts[email], acct_index) # O(logV)
                else:
                    email_to_accts[email] = acct_index
        results_dict = defaultdict(list)
        for e, i in email_to_accts.items(): # O(ElogV)
            leader = uf.find(i)
            results_dict[leader].append(e)

        results = []
        for i, e in results_dict.items(): # O(V + ElogE)
            entry = []
            entry.append(accounts[i][0])
            entry.extend(sorted(e))
            results.append(entry)
        return results


class UnionFind:

    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            x = self.par[x]
        return x

    def union_find(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if self.rank[par_x] > self.rank[par_y]:
            self.par[par_y] = par_x
            self.rank[par_x] += self.rank[par_y]
        else:
            self.par[par_x] = par_y
            self.rank[par_y] += self.rank[par_x]
