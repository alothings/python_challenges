import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
	int divisorSum(int n);
}

/* 
Task: Write a Calculator class, implement AdvancedArithmetic interface.
implement method divisorSum. Make it pblic, and take an integer n. Return sum 
of all its divisors.
*/

class Calculator implements AdvancedArithmetic{
	public int divisorSum(int n){
		int sum = n;		

		for(int i=1; i<n ; i++){
			if(n % i == 0){
				sum += i;
			}
		}
		return sum;
	}
}

class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();
        
      	AdvancedArithmetic myCalculator = new Calculator(); 
        int sum = myCalculator.divisorSum(n);
        System.out.println("I implemented: " + myCalculator.getClass().getInterfaces()[0].getName() );
        System.out.println(sum);
    }
}
