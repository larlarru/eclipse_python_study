package oop;

public class Animal {
	
	public boolean egg = false;
	private int age = 0;
	
	public void getOld() {
		age++;
	}
	
	public void changeEgg() {
		
		egg = !egg;
	}
	
	public int getAge() {
		return age;
	}
}
