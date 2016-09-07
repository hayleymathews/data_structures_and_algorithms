"""abstract class for euler tour for traversing a Tree"""

from abc import ABC, abstractmethod

class EulerTour(ABC):
    """
    abstract class for performing a euler tour

    _hook_previst and _hook_postvisit may be overridden by subclass
    """

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        """
        perform tour and return any result from post visit of root
        """
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        perform tour of usubtree rooted at Position p

        p position of current node being visited
        d depth of p in the tree
        path list of indices of children on path from root to p
        """
        self._hook_previst(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    @abstractmethod
    def _hook_previst(self, p, d, path):
        """
        visit node for the first time
        """
        pass

    @abstractmethod
    def _hook_postvisit(self, p, d, path, results):
        """
        visit node for the second time
        """
        pass
