class Solution(object):
    def isValid(self, s):
        stk=[]
        for i in s:
            if i=="(":
                stk.append(")")
            elif i=="{":
                stk.append("}")
            elif i=="[":
                stk.append("]")
            else:
                if stk==[] or i!=stk.pop():
                    return False
        return len(stk)==0
        