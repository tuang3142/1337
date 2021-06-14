class Solution:
    def maximumRemovals(self, word, seq, remove):
        def check_seq(m):
            i = 0
            for j, w in enumerate(word):
                if w == seq[i] and remove_id[j] > m:
                    i += 1
                    if i == len(seq):
                        return True
            return False

        remove_id = [float('inf')] * len(word)
        for i, v in enumerate(remove):
            remove_id[v] = i

        l, r = 0, len(remove) - 1
        ret = 0
        while l <= r:
            m = (l + r) // 2
            if check_seq(m):
                ret = m + 1
                l = m + 1
            else:
                r = m - 1
        return ret
