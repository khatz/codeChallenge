class Solution(object):
    def findMaxSubs(self, s, i1, i2):
        """
        i1: start position of search (including position i1)
        i2: end position of search (excluding position i2)
        """
        print(i1, i2, s[i1:i2])
        if i1>=i2:
            # print "0"
            return 0
        if i1+1 == i2:
            # print "1"
            return 1

        # last known position of alphabet
        alpha_pos = {}
        # second last known position of doubling alphabet
        alpha_before = -1
        max_len = 0
        double_count = 0
        # doubling alphabet
        chr = ""

        for i in range(i1, i2):
            # second occurrence of any character
            if s[i] in alpha_pos:
                # find the first doubling character
                if chr is "":
                    print "got", s[i]
                    chr = s[i]
                if chr is s[i]:
                    if alpha_before is not -1:
                        length = self.findMaxSubs(s, alpha_before+1, i)
                    else:
                        length = self.findMaxSubs(s, i1, i)
                    # print "return", length
                    if length > max_len:
                        max_len = length

                    # maintain known positions
                    alpha_before = alpha_pos[chr]

            alpha_pos[s[i]] = i
        # no double char
        if alpha_before is -1:
            print "no double", s[i1:i2], len(s[i1:i2])
            max_len = len(s[i1:i2])
        # last subsequence of doubling char
        else:
            length = self.findMaxSubs(s, alpha_before+1, len(s))
            if length > max_len:
                max_len = length

        # print max_len
        return max_len

    def lengthOfLongestSubstring(self, s):

        ret = self.findMaxSubs(s, 0, len(s))

        return ret

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_start = -1
        max_end = 0
        max_len = 0

        for j in range(len(s)):
            alpha = {}
            cur_start = -1
            cur_len = 0
            for i in range(j, len(s)):
                print s[i]
                # collision
                if alpha.has_key(s[i]):
                    if cur_len > 0:
                        print "saving ", cur_len
                        if max_len == cur_len:
                            max_end = i
                        cur_len = 1
                        cur_start = i
                    alpha = {s[i]: 1}
                # new
                else:
                    alpha[s[i]] = 1
                    cur_len += 1
                    if cur_start == -1:
                        cur_start = i
                    if max_len < cur_len:
                        max_start = cur_start
                        max_len = cur_len

            if cur_len > 0:
                if max_len == cur_len:
                    max_end = i

        print ("max ", max_len, " from ", max_start, " - ", max_end)

        return max_len

def main():
    sol = Solution()
    ret = sol.lengthOfLongestSubstring("qthepvzhouiriqnqjpgwabpwwoqebcguxnankzwztgsdwgwixcexfwvemliqpomnemcolypfgikfognnktkqrhueteukvgzb")
    print ret

main()