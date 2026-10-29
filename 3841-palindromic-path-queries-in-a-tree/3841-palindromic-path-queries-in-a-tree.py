class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n

        stack = [(0, -1, 0)]
        order = []
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                parent[u] = p
                order.append(u)
                stack.append((u, p, 1))
                for v in g[u]:
                    if v == p:
                        continue
                    depth[v] = depth[u] + 1
                    stack.append((v, u, 0))
            else:
                size[u] = 1
                max_sz = 0
                for v in g[u]:
                    if v == p:
                        continue
                    size[u] += size[v]
                    if size[v] > max_sz:
                        max_sz = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        cur = 0
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            x = u
            while x != -1:
                head[x] = h
                pos[x] = cur
                cur += 1
                for v in g[x]:
                    if v != parent[x] and v != heavy[x]:
                        stack.append((v, v))
                x = heavy[x]

        arr = [0] * n
        chars = list(s)
        for i, ch in enumerate(chars):
            arr[pos[i]] = 1 << (ord(ch) - 97)

        bit = [0] * (n + 1)

        def bit_add(i, delta):
            i += 1
            while i <= n:
                bit[i] ^= delta
                i += i & -i

        def bit_sum(i):
            res = 0
            i += 1
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def range_xor(l, r):
            return bit_sum(r) ^ (bit_sum(l - 1) if l > 0 else 0)

        for i, val in enumerate(arr):
            bit_add(i, val)

        def path_xor(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= range_xor(pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                c = parts[2]
                old_mask = 1 << (ord(chars[u]) - 97)
                new_mask = 1 << (ord(c) - 97)
                if old_mask != new_mask:
                    bit_add(pos[u], old_mask ^ new_mask)
                    chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_xor(u, v)
                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans