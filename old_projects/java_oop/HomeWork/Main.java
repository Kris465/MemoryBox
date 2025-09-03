public class Main{
	public static void main(String[] args){
		Persister persister = new Persister("Bob");
		Controller controller = new Controller(persister);
		ViewUser view = new ViewUser(controller);
        view.run();
	}
}