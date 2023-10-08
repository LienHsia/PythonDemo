//先设计一个递归函数将栈的栈底元素返回并移除

  public static int getAndRemoveLast(Stack<Integer>stack)
    {
        int result = stack.pop();
        if(stack.empty()) return result;
        else
        {
            int last=getAndRemoveLast(stack);
            stack.push(result);
            return last;
        }
    }
    //递归函数2
    public static void reverse(Stack<Integer>stack)
    {
        if(stack.empty())return;
        else{
            int i = getAndRemoveLast(stack);
            reverse(stack);
            stack.push(i);
        }
    }
