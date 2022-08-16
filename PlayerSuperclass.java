public class PlayerSuperclass
{
    private double foodSupply;
    private double waterSupply;
    private double staminaSupply;

    public double getFoodSupply()
    {
        return foodSupply;
    }

    public void setFoodSupply(double foodSupply)
    {
        this.foodSupply = foodSupply;
    }

    public double getWaterSupply()
    {
        return waterSupply;
    }

    public void setWaterSupply(double waterSupply)
    {
        this.waterSupply = waterSupply;
    }

    public double getStaminaSupply()
    {
        return staminaSupply;
    }

    public void setStaminaSupply(double staminaSupply)
    {
        this.staminaSupply = staminaSupply;
    }

    public double foodFactor()
    {
        return 1.0;
    }

    public double waterFactor()
    {
        return 1.0;
    }

    public double staminaFactor()
    {
        return 1.0;
    }

    public boolean enter(Terrain square)
    {
        double food = square.foodCost();
        if (food > 0.0)
        {
            food *= foodFactor();
        }
        foodSupply -= food;
        if (foodSupply > 20.0)
        {
            foodSupply = 20.0;
        }
        if (foodSupply < 0.0)
        {
            return false; // The player has 'died'
        }
        double water = square.waterCost();
        if (water > 0.0)
        {
            water *= waterFactor();
        }
        waterSupply -= water;
        if (waterSupply > 20.0)
        {
            waterSupply = 20.0;
        }
        if (waterSupply < 0.0)
        {
            return false; // The player has 'died'
        }
        double stamina = square.staminaCost();
        if (stamina > 0.0)
        {
            stamina *= staminaFactor();
        }
        staminaSupply -= stamina;
        if (staminaSupply > 20.0)
        {
            staminaSupply = 20.0;
        }
        if (staminaSupply < 0.0)
        {
            return false; // The player has 'died'
        }
        return true;
    }
}
