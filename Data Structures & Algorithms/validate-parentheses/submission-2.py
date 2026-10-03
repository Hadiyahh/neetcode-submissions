class Solution:
    def isValid(self, s: str) -> bool:
        # take out the last element of the string check if its a pair of the other list that we have if yes take them both out if no only take out the element from the string and put it in the list 
        stack = []
        #st = "".join(s)
        #st = s.split() # i want to be able to access the last element and pop it 
        # but since its character 
        st = list(s)

        #if stack.isempty()
        if len(st) == 0:
            return False
        stack.append(st[-1]) 
        st.pop()
        while(st):
            if stack and (stack[-1] == ')' and st[-1] == "(" or stack[-1] == '}' and st[-1] == "{" or stack[-1] == ']' and st[-1] == "["):
                st.pop()
                stack.pop()
            else:
                stack.append(st[-1])
                st.pop()
        if len(stack) == 0 and len(st) == 0:
            return True
        else:
            return False
