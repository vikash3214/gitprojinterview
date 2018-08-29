class Stack:

    def __init__(self):
        self.stack = []

    def add(self, element):

        if element not in self.stack:
            self.stack.append(element)
            return True
        else:
            return False
    def remove(self):

        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
	        return self.stack[-1]

def braceRedundancyChecker(str):
    Stack1=Stack()
    for i in range(len(str)):
        if str[i]==')':
            top=Stack1.peek()
            Stack1.remove()
            flag=True
            while (top!='('):
                if top == '+' or top == '-' or top == '*' or top == '/':
                    flag=False
                top=Stack1.peek()
                if top == '(':
                    continue
                else:
                    Stack1.remove()
            if flag==True:
                return True
        else:
            Stack1.add(str[i])
    return False



if __name__=="__main__":
    expression=input("enter expression=====  ")##"((a+b)+(b+y))"
    if braceRedundancyChecker(expression):
        print("duplicates found")
    else:
        print("no duplicates")
