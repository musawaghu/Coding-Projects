import java.io.*;
import java.util.Scanner;

public class Sales
{
    public static void main(String[] args) throws IOException
    {
        while (true)
        {
            System.out.print("Enter 1 to add a sale, 2 to print out all sales, 3 to print the total sales, and 4 to quit: ");
            //Giving the user options to choose from.
            Scanner keyboard = new Scanner(System.in);
            int userInput = keyboard.nextInt();
            //You may assume that the first time the user runs the program, then will choose to add a
            //sale (thereby creating the file) before they choose any of the other options. The first time you run the
            //program, please add a sale first.

            if (userInput == 1) //add(append) sale option
            {
                FileWriter salesFile = new FileWriter("sales.txt", true); //read the file
                PrintWriter myFile = new PrintWriter(salesFile); //reference the file to read file
                System.out.println("Enter the amount of the sale: "); //getting input from user
                double saleInput = keyboard.nextDouble();
                myFile.println(saleInput); //appending to the file
                myFile.close();
            }
            if (userInput == 2) //printing the contents of the file
            {
                File myFile = new File("sales.txt"); //read file
                Scanner inputFile = new Scanner(myFile); //reference the read file object
                double sale;
                while (inputFile.hasNext()) //checking if the file has more content after each line
                {
                    sale = inputFile.nextDouble(); //assigning sale to nextDouble
                    System.out.println("$" + sale); //printing out nextDouble
                }
                inputFile.close();
            }
            if (userInput == 3)
            {
                File myFile = new File("sales.txt"); //reading file
                Scanner inputFile = new Scanner(myFile); //referencing file to File object
                double total = 0; //counter variable
                while (inputFile.hasNext()) //checking if there is more content in the file
                {
                    total += inputFile.nextDouble(); //summation of all values in the file
                }
                System.out.println("The total sale is $" + total); //printing to the console
                inputFile.close();
            }
            if (userInput == 4)
            {
                break; //quitting the program
            }
        }

    }
}
