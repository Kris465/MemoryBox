public class CodeFromWorkshop {
    
    public class BinaryTree{
        Node Root;
        private class Node{
            int Value;
            Node Left;
            Node Right;
        }

        public boolean find(int Value){
            Node current = Root;
            while(current != null){
                if(current.Value == Value)
                    return true;

                if(Value < current.Value){
                    current = current.Left;
                }else{
                    current = current.Right;
                }
            }
            return false;
        }

        public void push(int Value){
            Node node = new Node();
            node.Value = Value;
            if(Root == null){
                Root = node;
            }else {
                Node current = Root;

                while (current != null) {
                    if (Value < current.Value) {
                        if(current.Left == null){
                            current.Left = node;
                            return ;
                        }
                        current = current.Left;
                    } else {
                        if(current.Right == null){
                            current.Right = node;
                            return ;
                        }
                        current = current.Right;
                    }
                }

            }
        }
    }
    public static void main(String[] args) {

    }
}
