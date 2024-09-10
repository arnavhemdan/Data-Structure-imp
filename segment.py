from math import ceil, log2

class SegmentTree:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        t = ceil(log2(n))
        self.sz = 2 * pow(2, t) - 1
        self.tree = [0] * self.sz
        self.buildtree(0, 0, n - 1)

    def buildtree(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            self.buildtree(left_node, start, mid)
            self.buildtree(right_node, mid + 1, end)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def update(self, index, value):
        diff = value - self.arr[index]
        self.arr[index] = value
        self._update(0, 0, self.n - 1, index, diff)

    def _update(self, node, start, end, index, diff):
        if start == end == index:
            self.tree[node] += diff
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            if start <= index <= mid:
                self._update(left_node, start, mid, index, diff)
            else:
                self._update(right_node, mid + 1, end, index, diff)
            self.tree[node] = self.tree[left_node] + self.tree[right_node]

    def query(self, query_start, query_end):
        return self._query(0, 0, self.n - 1, query_start, query_end)

    def _query(self, node, start, end, query_start, query_end):
        if query_start > end or query_end < start:
            return 0
        if query_start <= start and query_end >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        left_sum = self._query(left_node, start, mid, query_start, query_end)
        right_sum = self._query(right_node, mid + 1, end, query_start, query_end)
        return left_sum + right_sum


if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input("Enter element {}:".format(i)))
    t1 = SegmentTree(arr, n)
    while True:
        ch = int(input("Enter your choice: 1. Update\n2. Sum\n3. Exit\n"))
        if ch == 1:
            index = int(input("Enter index value: "))
            value = int(input("Enter updated value: "))
            t1.update(index, value)
        elif ch == 2:
            l = int(input("Enter left range: "))
            r = int(input("Enter right range: "))
            print("Sum:", t1.query(l, r))
        elif ch == 3:
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
