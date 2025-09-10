class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        from collections import defaultdict
        
        # Convert each person's languages into a set for fast lookup
        lang_set = [set(l) for l in languages]
        
        # Find all friendships that are unsuccessful
        bad_pairs = []
        for u, v in friendships:
            if lang_set[u - 1] & lang_set[v - 1]:
                continue  # they already share a language
            bad_pairs.append((u - 1, v - 1))
        
        if not bad_pairs:
            return 0  # all friendships are already successful
        
        # Count for each language how many people need to be taught
        count = defaultdict(set)
        
        for u, v in bad_pairs:
            for person in [u, v]:
                for lang in range(1, n + 1):
                    if lang not in lang_set[person]:
                        count[lang].add(person)
        
        # Find the language that requires teaching the fewest people
        min_teach = float('inf')
        for lang, people in count.items():
            min_teach = min(min_teach, len(people))
        
        return min_teach
