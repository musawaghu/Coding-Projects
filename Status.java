// Student: Musa Waghu
// Course: CS1400
// Professor: David Johannsen

public class Status
{
    private int hitPoints;
    private int hunger;
    private int sleepiness;
    public Status(int hitPoints, int hunger, int sleepiness)
    {
        //regular constructor
        this.hitPoints = hitPoints;
        this.hunger = hunger;
        this.sleepiness = sleepiness;
        if (hitPoints > 25) //setting hitpoints to 25 if the user enters a value over 25 for hitpoints.
        {
            setHitPoints(25);
        }
        if (hitPoints < 0)
        {
            setHitPoints(0);
        }
        if (hunger > 15)
        {
            setHunger(15);
        }
        if (hunger < 0)
        {
            setHunger(0);
        }
        if (sleepiness > 15)
        {
            setSleepiness(15);
        }
        if (sleepiness < 0)
        {
            setSleepiness(0);
        }
    }
    public Status(Status object2)
    {
        //copy constructor
        hitPoints = object2.hitPoints;
        hunger = object2.hunger;
        sleepiness = object2.sleepiness;
    }
    public int getHitPoints() //getters
    {
        return hitPoints;
    }
    public int getHunger()
    {
        return hunger;
    }
    public int getSleepiness()
    {
        return sleepiness;
    }

    public void setHitPoints(int hitPoints) //setters
    {
        this.hitPoints = hitPoints;
    }
    public void setHunger(int hunger)
    {
        this.hunger = hunger;
    }
    public void setSleepiness(int sleepiness)
    {
        this.sleepiness = sleepiness;
    }
    @Override
    public String toString() //toString override method
    {
        return "STATUS [Hitpoints: " + hitPoints + ", Hunger: " + hunger + ", Sleepiness: " + sleepiness + "]";
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
            Status otherStatus = (Status) other;
            if (otherStatus.getHitPoints() == getHitPoints() && otherStatus.getHunger() == getHunger() && otherStatus.getSleepiness() == getSleepiness())
            {
                return true;
            }
        }
        return false;
    }
    public void addHunger(int delta)
    {
        this.hunger = this.hunger + delta;
        if (this.hunger < 0)
        {
            this.hunger = 0;
        }
        else if (this.hunger > 25)
        {
            this.hunger = 25;
        }
    }
    public void addHitPoints(int delta)
    {
        this.hitPoints = this.hitPoints + delta;
        if (this.hitPoints < 0)
        {
            this.hitPoints = 0;
        }
        else if (this.hitPoints > 25)
        {
            this.hitPoints = 25;
        }
    }
    public void addSleepiness(int delta)
    {
        this.sleepiness = this.sleepiness + delta;
        if (this.sleepiness < 0)
        {
            this.sleepiness = 0;
        }
        else if (this.sleepiness > 25)
        {
            this.sleepiness = 25;
        }
    }
}
