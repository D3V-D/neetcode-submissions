/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* prehead = new ListNode(-1);
        ListNode* curr = prehead;
        while (list1 != nullptr && list2 != nullptr) {
            ListNode* next = new ListNode(std::min(list1->val, list2->val));
            if (list1->val < list2->val) {
                list1 = list1->next;
            } else {
                list2 = list2->next;
            }

            curr->next = next;
            curr = curr->next;
        }

        while (list1 != nullptr) {
            ListNode* next = new ListNode(list1->val);
            curr->next = next;
            curr = curr->next;
            list1 = list1->next;
        }
         
        while (list2 != nullptr) {
            ListNode* next = new ListNode(list2->val);
            curr->next = next;
            curr = curr->next;
            list2 = list2->next;
        }

        return prehead->next;;
    }
};
