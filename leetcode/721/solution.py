from typing import Optional, List, Tuple
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def get_emails(index):
            return accounts[index][1:]
            
        def find_clique(index):
            if index in visited:
                return []
            visited.append(index)
            results = [index]
            for email in get_emails(index):
                for edge in edges[email]:
                    results += find_clique(edge)
            return results
        
        edges = defaultdict(list)

        for index, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                edges[email].append(index)

        cliques = []
        visited = []
        for index, account in enumerate(accounts):
            if not index in visited:
                cliques.append(find_clique(index))

        results = []
        for clique in cliques:
            name = accounts[clique[0]][0]
            new_account = [name]
            for member in clique:
                account = accounts[member]
                emails = account[1:]
                new_account.extend(emails)
            results.append(new_account)

        for result in results:
            result[1:] = sorted(list(set(result[1:])))
                
        return results
