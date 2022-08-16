// Student: Musa Waghu
// Course: CS1400
// Professor: David Johannsen

public class Stats
{
    private int strength;
    private int intelligence;
    private int stamina;
    public Stats(int strength, int intelligence, int stamina)
    {
        //regular constructor
        this.strength = strength;
        this.intelligence = intelligence;
        this.stamina = stamina;
        if (strength < 1 || strength > 12 || intelligence < 1 || intelligence > 12 || stamina < 1 || stamina > 12 || strength + intelligence + stamina != 20)
        {
            throw new IllegalArgumentException();

        }
    }
    public Stats(Stats object2)
    {
        //copy constructor
        strength = object2.strength;
        intelligence = object2.intelligence;
        stamina = object2.stamina;

    }
    public int getStrength() //getters
    {
        return strength;
    }

    public int getIntelligence() //getters
    {
        return intelligence;
    }

    public int getStamina() //getters
    {
        return stamina;
    }
    @Override
    public String toString() //toString override method
    {
        return "STATS [Strength: " + strength + ", Intelligence: " + intelligence + ", Stamina: " + stamina + "]";
    }
    @Override
    public boolean equals(Object other) //equals override method
    {
        if (other == null || getClass() != other.getClass())
        {
            return false;
        }
        else
        {
            Stats otherStats = (Stats) other;
            if (otherStats.getStrength() == getStrength() && otherStats.getIntelligence() == getIntelligence() && otherStats.getStamina() == getStamina())
            {
                return true;
            }
        }
        return false;
    }
    public void moveStrengthToIntelligence(int amount) //reducing or increasing strength and intelligence, while keeping the total the same, and checking if they are still in range.
    {
        if (amount > 0)
        {
            this.strength -= amount;
            this.intelligence += amount;
            if (this.strength < 1 || this.strength > 12 || this.intelligence < 1 || this.intelligence > 12)
            {
                throw new IllegalArgumentException();
            }
        }
        if (amount < 0)
        {
            this.strength += amount;
            this.intelligence -= amount;
            if (this.strength < 1 || this.strength > 12 || this.intelligence < 1 || this.intelligence > 12)
            {
                throw new IllegalArgumentException();
            }
        }
    }
    public void moveIntelligenceToStamina(int amount) ////reducing or increasing stamina and intelligence, while keeping the total the same, and checking if they are still in range.
    {
        if (amount > 0)
        {
            this.intelligence -= amount;
            this.stamina += amount;
            if (this.stamina < 1 || this.stamina > 12 || this.intelligence < 1 || this.intelligence > 12)
            {
                throw new IllegalArgumentException();
            }
        }
        else if (amount < 0)
        {
            this.intelligence += amount;
            this.stamina -= amount;
            if (this.stamina < 1 || this.stamina > 12 || this.intelligence < 1 || this.intelligence > 12)
            {
                throw new IllegalArgumentException();
            }
        }
    }
    public void moveStaminaToStrength(int amount) ////reducing or increasing strength and stamina, while keeping the total the same, and checking if they are still in range.
    {
        if (amount > 0)
        {
            this.stamina -= amount;
            this.strength += amount;
            if (this.stamina < 1 || this.stamina > 12 || this.strength < 1 || this.strength > 12)
            {
                throw new IllegalArgumentException();
            }
        }
        else if (amount < 0)
        {
            this.stamina += amount;
            this.strength -= amount;
            if (this.stamina < 1 || this.stamina > 12 || this.strength < 1 || this.strength > 12)
            {
                throw new IllegalArgumentException();
            }
        }
    }
}
