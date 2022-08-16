public class PlayerW extends PlayerSuperclass
{
    @Override
    public double foodFactor()
    {
        return 1.5;
    }

    @Override
    public double waterFactor()
    {
        return 3.0;
    }

    @Override
    public double staminaFactor()
    {
        return 2.0;
    }
}
