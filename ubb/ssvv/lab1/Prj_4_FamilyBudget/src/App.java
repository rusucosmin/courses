

import java.io.BufferedWriter;
import repository.MemberRepository;
import controller.MemberController;
import ui.MemberUI;;

public class App {
	public static void main(String[] args) {
		
			MemberRepository repo = new MemberRepository();
		
			MemberController ctrl = new MemberController(repo);
		
			MemberUI console = new MemberUI(ctrl);
			console.Run();
		
	}
}
