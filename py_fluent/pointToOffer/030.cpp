class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {

    }
    void push(int x) {
        if(m_stackB.size()==0||x<=m_stackB.top()){
            m_stackB.push(x);
        }
        m_stackA.push(x);
    }

    void pop() {
        if(m_stackA.size()==0){
            return;
        }
        if(m_stackA.top()==m_stackB.top()){
            m_stackA.pop();
            m_stackB.pop();
        }else{
            m_stackA.pop();
        }
    }

    int top() {
        return m_stackA.top();
    }
    int min() {
        return m_stackB.top();
    }
private:
    stack<int>m_stackA;
    stack<int>m_stackB;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->min();
 */