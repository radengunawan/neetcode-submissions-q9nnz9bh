class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])
        res = []

        def getIndex(c):
            index = ord(c) - ord('a')
            return index

        def dfs(r, c, node):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or board[r][c] == '*' or
                not node.children[getIndex(board[r][c])]):
                return 0

            tmp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getIndex(tmp)]
            found = 0
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                found += 1

            found += dfs(r + 1, c, node)
            found += dfs(r - 1, c, node)
            found += dfs(r, c + 1, node)
            found += dfs(r, c - 1, node)

            board[r][c] = tmp
            node.refs -= found
            if not node.refs:
                prev.children[getIndex(tmp)] = None
            return found

        for r in range(ROWS):
            for c in range(COLS):
                root.refs -= dfs(r, c, root)

        return res