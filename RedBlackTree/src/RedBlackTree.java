public class RedBlackTree {
    
    Node root;
    private class Node{
        int key;
        String color;
        Node left;
        Node right;
        Node parent;
    }

    public void add(int key) {
        Node newNode = new Node(key);
        if (root == null) {
            root = newNode;
            root.color = BLACK;
            return;
        }
        Node parent = null;
        Node current = root;
        while (current != null) {
            parent = current;
            if (key < current.key) {
                current = current.left;
            } else if (key > current.key) {
                current = current.right;
            } else {
                return; // элемент уже существует
            }
        }
        newNode.parent = parent;
        if (key < parent.key) {
            parent.left = newNode;
        } else {
            parent.right = newNode;
        }
        balance(newNode);
    }

    private void rotateLeft(Node node) {
        Node rightChild = node.right;
        node.right = rightChild.left;
        if (rightChild.left != null) {
            rightChild.left.parent = node;
        }
        rightChild.parent = node.parent;
        if (node.parent == null) {
            root = rightChild;
        } else if (node == node.parent.left) {
            node.parent.left = rightChild;
        } else {
            node.parent.right = rightChild;
        }
        rightChild.left = node;
        node.parent = rightChild;
    }
}
