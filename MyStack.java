class MyStack {

    //创建两个队列
    Queue<Integer> que1;
    Queue<Integer> que2;

    public MyStack() {
        que1 = new LinkedList<>();//队列是接口，不能直接实例化
        que2 = new LinkedList<>();//队列是由链表实现的，所以要用链表来实例化队列

    }
    
    public void push(int x) {
        if(empty()){//一开始两个队列都是空的时候，默认将第一个元素插入到que1中
            que1.offer(x);
        }else{//从第二个元素开始，哪个队列不为空，对哪个队列进行插入操作
            if(que1.isEmpty()){
                que2.offer(x);
            }else{
                que1.offer(x);
            }
        }
    
    }
    
    public int pop() {
        if(empty()){
            return -1;
        }
      //出栈也是找哪个队列不为空，就对哪个队列进行操作
        if(que1.isEmpty()){
            int size = que2.size();
            for(int i =0 ; i<size-1 ;i++){
                int tmp = que2.poll();
                que1.offer(tmp);
            }
            return que2.poll();
        }else{
            int size = que1.size();
            for(int i =0 ; i<size-1 ;i++){
                int tmp = que1.poll();
                que2.offer(tmp);
            }
            return que1.poll();
        }
    }
    
    public int top() {
        if(empty()){
            return -1;
        }
     //查看栈顶元素，和出栈类似，只不过记得把队列最后一个元素继续插入到另一个队列的最后
     //不然就是出栈操作了
        if(que1.isEmpty()){
            int size = que2.size();
            int tmp = -1;
            for(int i =0 ; i<size ;i++){
                tmp = que2.poll();
                que1.offer(tmp);
            }
            return tmp;
        }else{
            int size = que1.size();
            int tmp = -1;
            for(int i =0 ; i<size ;i++){
                tmp = que1.poll();
                que2.offer(tmp);
            }
            return tmp;
        }

    }
    
    public boolean empty() {
        return que1.isEmpty() &&  que2.isEmpty();
    }
}