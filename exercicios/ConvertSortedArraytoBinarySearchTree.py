class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedArrayToBST(self, nums):   # converte um array ordenado em uma árvore binária de busca...

        if not nums:
            return None
        
        meio = len(nums) // 2       # obtendo apenas o quociente inteiro da divisão
        
        raiz = TreeNode(nums[meio])
        raiz.left = self.sortedArrayToBST(nums[:meio])
        raiz.right = self.sortedArrayToBST(nums[meio+1:])
        
        return raiz