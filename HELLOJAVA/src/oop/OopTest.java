package oop;

public class OopTest {
	
	public static void main(String[] args) {
		Human a = new Human();
		System.out.println("a.age : " + a.getAge());
		System.out.println("a.egg : " + a.egg);
		
		a.getOld();
		System.out.println("a.age : " + a.getAge());
		System.out.println("a.egg : " + a.egg);
	}
}
