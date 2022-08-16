public class Forest extends Terrain
{
    @Override
    public double foodCost()
    {
        return -10.0;
    }
    public double waterCost()
    {
        return 1.0;
    }
    @Override
    public double staminaCost()
    {
        return 2.0;
    }
}
