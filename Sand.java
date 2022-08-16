public class Sand extends Terrain
{
    public double foodCost()
    {
        return 1.0;
    }
    @Override
    public double waterCost()
    {
        return 1.5;
    }
    @Override
    public double staminaCost()
    {
        return 1.5;
    }
}
