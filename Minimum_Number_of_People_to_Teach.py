from collections import Counter
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        def can_communicate(u: int, v: int):
            return bool(set(languages[u-1]) & set(languages[v-1]))

        problematic = set()
        for u,v in friendships:
            if not can_communicate(u,v):
                problematic.add(u)
                problematic.add(v)

        if not problematic:
            return 0
            
        cnt = Counter()
        for u in problematic:
            for lang in languages[u-1]:
                cnt[lang] += 1
        max_known = max(cnt.values(), default = 0)
        return len(problematic) - max_known

    