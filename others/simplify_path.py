"""
71. Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
path = "/a/../../b/../c//.//", => "/c"
path = "/a//b////c/d//././/..", => "/a/b/c"

In a UNIX-style file system, a period ('.') refers to the current directory, so it can be ignored in a simplified path. Additionally, a double period ("..") moves up a directory, so it cancels out whatever the last directory was. For more information, look here: https://en.wikipedia.org/wiki/Path_(computing)#Unix_style

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""

class Solution:
    def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """
        from collections import deque
        if path == None or path.strip() == "":
            return path
        deduped = path[0]
        t = path[1:]
        for i, c in enumerate(t):
            if t[i] == "/" and deduped[len(deduped)-1] == "/":
                continue
            else:
                deduped += t[i]

        if len(deduped) == 1:
            return deduped
        stack = deque()

        dirs = deduped.split("/")

        for d in dirs:
            if d == "" or d == "." or d == "/":
                continue
            if d == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(d)
        simplifiedPath = "/"
        while stack:
            simplifiedPath += stack.popleft() + "/"
        return simplifiedPath[: len(simplifiedPath) - 1]
