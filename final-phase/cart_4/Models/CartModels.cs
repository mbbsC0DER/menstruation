public record Product(int Id, string Name, decimal Price);
public class CartItem
{
    public int ProductId { get; set; }
    public int Quantity { get; set; }
}
public record CartPage(Product[] Products, List<CartItem> Items);
