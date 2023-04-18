class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, val=None):
        self.length = 1
        self.head = ListNode(val) if val is not None else None

    def add_back(self, data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            it = self.head
            while it.next is not None:
                it = it.next
            new_node = ListNode(data)
            it.next = new_node
            self.length += 1

    def __iter__(self):
        self.it = self.head
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.length:
            rezult = self.it.val
            self.it = self.it.next
            self.index += 1
            return rezult
        else:
            raise StopIteration

    def deleteDuplicates(self, head):
        result = None
        count = 0
        while head.next != None:
            if head.val == head.next.val:
                tmp = head
                head = head.next
                del tmp
                if count == 0:
                    result = head
                count += 1
            else:
                head = head.next
                count += 1
        return Solution(result)


dictionary = {}


def climbStairs(n: int) -> int:
    if n in dictionary:
        return dictionary[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    sum = climbStairs(n - 1) + climbStairs(n - 2)
    dictionary[n] = sum
    return sum


def climbStairs2(n: int) -> int:
    if n <= 3:
        return n
    steps = [0,1,2,3]
    for i in range(4, n + 1):
        steps.append(steps[i-1] + steps[i - 2])
    return steps.pop()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        count = 0
        q = [root]
        while len(q):
            additional = []
            for el in q:
                if el.left:
                    additional.append(el.left)
                if el.right:
                    additional.append(el.right)
            q.clear()
            q.extend(additional)
            count += 1
        return count


def main():
    p = TreeNode(3)
    p.left = TreeNode(9)
    p.right = TreeNode(20)
    sol = Solution()
    print(sol.maxDepth(p))


if __name__ == '__main__':
    main()
