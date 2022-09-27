import java.util.*;

public class MarblesGame
{
    public static void main(String[] args)
    {
        System.out.println("Enter a number between 10 and 100: "); //Telling the user to input a number.
        Scanner keyboard = new Scanner(System.in);
        int count = keyboard.nextInt();
        if (count < 10 || count > 100) //checking if number is in range.
        {
            System.out.println("Number must be between 10 and 100.");
        }
        for (int i = count; i > 1; i--) //looping until count is equal to 1
        {
            System.out.println("Number of marbles remaining: " + count);
            System.out.println("Largest number of marbles you can take: " + (count/2));
            System.out.println("Choose a number between 1 and the above value: ");
            int chooseValue = keyboard.nextInt();
            if (chooseValue < 1 || chooseValue > (count/2)) //checking if user's value is within range.
            {
                System.out.println("Your value is not within the given range, please enter again.");
            }
            else
            {
                count = count - chooseValue; //subtracting user's value from count, so it can update count.
                if (chooseValue == 1 && count == 1) //when this happens, the computer will be forced to take the last marble after the user's turn, resulting in the computer's loss.
                {
                    System.out.println("The computer has lost this game of Nin.");
                    break;
                }
            }
            System.out.println("The computer will now choose a value.");
            int computerGuess = (int)Math.floor(Math.random()*((count/2)-1+1)+1); //calculating a random integer withing 1 and (count/2).
            System.out.println("The computer chose: " + computerGuess);
            count = count - computerGuess;
            if (computerGuess == 1 && count == 1) //When this happens, the user will be forced to take the last marble after the computer's turn, resulting in the user's loss.
            {
                System.out.println("You have lost this game of Nin.");
                break;
            }
        }


    }
}
