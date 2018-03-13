package model;

public class Member {
	private String name;
	private String id;	
	
	public Member(String name, String id){
		this.name= name;
		this.id=id;
		
		
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public String getId() {
		return id;
	}
	
	public String toString() {
		String s=this.name + " " + this.id;
		return s;   
	}
}
