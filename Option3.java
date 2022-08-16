public class Option3
{
    public static void main(String[] args)
    {
        PlayerSuperclass p1 = new PlayerF();
        p1.setFoodSupply(30.0);
        p1.setWaterSupply(10.0);
        p1.setStaminaSupply(25.0);

        PlayerSuperclass p2 = new PlayerW();
        p2.setFoodSupply(5.0);
        p2.setWaterSupply(30.0);
        p2.setStaminaSupply(15.0);

        PlayerSuperclass p3 = new PlayerS();
        p3.setFoodSupply(10.0);
        p3.setWaterSupply(40.0);
        p3.setStaminaSupply(25.0);
        int count1 = 0;
        int count2 = 0;
        int count3 = 0;

        Terrain[][] arr = new Terrain[10][50];
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 50; j++)
            {
                int type = (int) ((Math.random() * (4 - 1)) + 1);
                if (type == 1)
                {
                    arr[i][j] = new Grass();
                    boolean playerAlive = p1.enter(new Grass());
                    if (playerAlive)
                    {
                        count1++;
                        break;
                    }
                }
                else if (type == 2)
                {
                    arr[i][j] = new Sand();
                    boolean playerAlive = p2.enter(new Sand());
                    if (playerAlive)
                    {
                        count2++;
                        break;
                    }
                }
                else if (type == 3)
                {
                    arr[i][j] = new Forest();
                    boolean playerAlive = p3.enter(new Forest());
                    if (playerAlive)
                    {
                        count3++;
                        break;
                    }
                }
            }
        }
        System.out.println("Player Frank took " + count1 + " steps before dying");
        System.out.println("Player Wally took " + count2 + " steps before dying");
        System.out.println("Player Sam took " + count3 + " steps before dying");
    }
}
