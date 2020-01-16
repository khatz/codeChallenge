
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def dump(self):
        print (self.val)
        if self.next:
            self.next.dump()


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return None

        tmp1 = l1
        tmp2 = l2

        # setup initial pointers
        ptr = None
        ret = None
        flag = False

        while tmp1 is not None and tmp2 is not None:
            # compute current digit with carry-over
            sum = tmp1.val + tmp2.val
            if flag:
                sum += 1
            flag = (sum >= 10)
            if flag:
                sum -= 10
            print "adding " , sum
            node = ListNode(sum)
            if ptr is not None:
                ptr.next = node
            else:
                ret = node
            ptr = node

            # if current digit is the last
            if tmp1.next is None or tmp2.next is None:
                # carry-over
                if flag:
                    nxt = ListNode(1)
                    ptr.next = nxt
                tmp1 = tmp1.next
                tmp2 = tmp2.next
                break

            tmp1 = tmp1.next
            tmp2 = tmp2.next

        # leftover for l1
        while tmp1 is not None:
            node = ListNode(tmp1.val)
            if ptr is not None:
                ptr.next = node
            else:
                ret = node
            ptr = node
            tmp1 = tmp1.next

        # leftover for l2
        while tmp2 is not None:
            node = ListNode(tmp2.val)
            if ptr is not None:
                ptr.next = node
            else:
                ret = node
            ptr = node
            tmp2 = tmp2.next

        return ret

def main():
    l1 = ListNode(2)
    l12 = ListNode(7)
    l13 = ListNode(8)
    l1.next = l12
    l12.next = l13

    l2 = ListNode(0)

    sol = Solution()
    sum = sol.addTwoNumbers(l2, l1)
    sum.dump()

main()
