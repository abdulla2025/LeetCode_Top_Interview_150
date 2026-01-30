class TrieNode:
    __slots__ = ["next", "id"]
    def __init__(self):
        self.next: List[TrieNode | None] = [None] * 26
        self.id = -1

class Solution:
    def minimumCost(self,source: str,target: str,original: List[str],changed: List[str],cost: List[int],) -> int:
        n_conversions = len(cost)
        INF = float('inf')
        dist = [[INF] * (n_conversions << 1) for _ in range(n_conversions << 1)]
        for i in range(n_conversions << 1):
            dist[i][i] = 0
        trie_root = TrieNode()
        next_id = 0
        def add_to_trie(word: str) -> int:
            curr = trie_root
            for ch in word:
                idx = ord(ch) - ord("a")
                if curr.next[idx] is None:
                    curr.next[idx] = TrieNode()
                curr = curr.next[idx]
            if curr.id < 0:
                nonlocal next_id
                curr.id = next_id
                next_id += 1
            return curr.id
        
        @cache
        def min_cost_from(pos: int) -> int:
            if pos >= len(source):
                return 0
            
            result = min_cost_from(pos + 1) if source[pos] == target[pos] else INF
            
            src_node = tgt_node = trie_root
            for end_pos in range(pos, len(source)):
                src_node = src_node.next[ord(source[end_pos]) - ord("a")]
                tgt_node = tgt_node.next[ord(target[end_pos]) - ord("a")]
                
                if src_node is None or tgt_node is None:
                    break
                if src_node.id < 0 or tgt_node.id < 0:
                    continue
                
                result = min(result, min_cost_from(end_pos + 1) + dist[src_node.id][tgt_node.id])
            
            return result
        
        for orig, chg, c in zip(original, changed, cost):
            orig_id = add_to_trie(orig)
            chg_id = add_to_trie(chg)
            dist[orig_id][chg_id] = min(dist[orig_id][chg_id], c)
        
        for mid in range(next_id):
            for start in range(next_id):
                if dist[start][mid] >= INF:
                    continue
                for end in range(next_id):
                    if dist[start][mid] + dist[mid][end] < dist[start][end]:
                        dist[start][end] = dist[start][mid] + dist[mid][end]
        
        answer = min_cost_from(0)
        return -1 if answer >= INF else answer
