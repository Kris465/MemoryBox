public class CodeFromWorkshop {
    public class HashMap{
        private class Entity{
            int Key;
            int Value;
        }
        private class Basket{
            Node Head;
            private class Node{
                Entity entity;
                Node next;
            }

            Entity find(int Key){
                Node current = Head;
                if(Head != null){
                    while (current != null){
                        if(current.entity.Key == Key){
                            return current.entity;
                        }
                        current = current.next;
                    }
                }
                return null;
            }

            private boolean push(Entity entity){
                Node node = new Node();
                node.entity = entity;

                Node current = Head;
                while(current != null){
                    if(current.entity == entity){
                        return false;
                    }
                    if(current.next == null){
                        current.next = node;
                        return true;
                    }
                    current = current.next;
                }
                Head = node;
                return true;
            }

            private boolean del(int Key){
                Node current = Head;
                while(current != null){
                    if(current.next.entity.Key == Key){
                        if(current.next != null) {
                            current.next = current.next.next;
                        }else{
                            current.next = null;
                        }
                        return true;
                    }
                    current = current.next;
                }
                return false;
            }
        }
        private static final int INIT_SIZE = 16;
        private static final int Size = 0;
        private static final double LOAD_FACTOR = 0.75;

        private Basket baskets[];

        public HashMap() {
            this(INIT_SIZE);
        }

        public HashMap(int size) {
            baskets = new Basket[size];
        }

        int calcIndex(int Key){
            return Key % baskets.length;
        }

        public Entity find(int Key){
            int index = calcIndex(Key);
            Basket basket = baskets[index];

            if(basket != null){
                return basket.find(Key);
            }
            return null;
        }

        public void push(int Key, int Value){
            int index = calcIndex(Key);
            Basket basket = baskets[index];

            Entity entity = new Entity();
            entity.Value = Value;
            entity.Key = Key;

            if(basket == null){
                basket = new Basket();
                baskets[index] = basket;
            }

            basket.push(entity);

        }

        public void del(int Key){
            int index = calcIndex(Key);
            Basket basket = baskets[index];

            if(basket != null){
                basket.del(Key);
            }
        }
    }

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
