class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists):
        merged_list = self.mergeLists(lists, 0, len(lists) - 1)
        return merged_list
    
    def mergeLists(self, lists, inicio, fim):

        if inicio > fim:
            return None
        
        if inicio == fim:
            return lists[inicio]
        
        meio = (inicio + fim) // 2
        esquerda = self.mergeLists(lists, inicio, meio)
        direita = self.mergeLists(lists, meio + 1, fim)

        return self.mergeTwoLists(esquerda, direita)
    
    def mergeTwoLists(self, l1, l2):

        no = ListNode(0)
        ptr = no

        while l1 and l2:

            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next

            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        ptr.next = l1 if l1 else l2
        
        return no.next
