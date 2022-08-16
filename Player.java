// Student: Musa Waghu
// Course: CS1400
// Professor: David Johannsen

public class Player
{
    private String name;
    private int experience;
    private Stats stats;
    private Status status;
    private int id;
    private static int count;

    public Player(String name, int experience, Stats sta, Status st) //regular constructor
    {
        this.name = name;
        this.experience = experience;
        stats = new Stats(sta);
        status = new Status(st);
        count++;
        this.id = count;
    }
    public Player(Player object2)
    {
        //copy constructor
        name = object2.name;
        experience = object2.experience;
        stats = object2.stats;
        status = object2.status;
        id = object2.id;
        if(object2 == null)
        {
            throw new NullPointerException();
        }
    }
    public String getName() //getters
    {
        return name;
    }
    public int getExperience()
    {
        return experience;
    }
    public Stats getStats()
    {
        return new Stats(stats);
    }
    public Status getStatus()
    {
        return new Status(status);
    }
    public void setName(String name) //setter
    {
        this.name = name;
    }
    public void setExperience(int experience)
    {
        this.experience = experience;
    }
    public void setStats(Stats stats)
    {
        this.stats = stats;
    }
    public void setStatus(Status status)
    {
        this.status = status;
    }
    @Override
    public String toString() //toString override method
    {
        return "PLAYER [Name: " + name + ", Experience: " + experience + "]\n" + stats + "\n" + status;
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
            Player otherPlayer = (Player) other;
            if (otherPlayer.getName() == getName() && otherPlayer.getExperience() == getExperience() && otherPlayer.getStats() == getStats() && otherPlayer.getStatus() == getStatus())
            {
                return true;
            }
        }
        return false;
    }
    public static int playersCreated() //returns the amount of players created that don't have an exception
    {
        return count;
    }
    public void addExperience(int e)
    {
        experience = experience + e;
    }
}
