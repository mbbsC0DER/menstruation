using System.Text.Json;
using Microsoft.AspNetCore.Mvc;
public class CartController : Controller
{
    private static readonly Product[] products = [
        new(1, "Notebook", 50m), new(2, "Pen", 10m), new(3, "Backpack", 500m)
    ];
    private List<CartItem> ReadCart() => JsonSerializer.Deserialize<List<CartItem>>(
        HttpContext.Session.GetString("cart") ?? "[]") ?? [];
    private void SaveCart(List<CartItem> cart) => HttpContext.Session.SetString("cart", JsonSerializer.Serialize(cart));
    public IActionResult Index() => View(new CartPage(products, ReadCart()));
    [HttpPost, ValidateAntiForgeryToken]
    public IActionResult Add(int id)
    {
        if (!products.Any(p => p.Id == id)) return NotFound();
        var cart = ReadCart();
        var item = cart.Find(i => i.ProductId == id);
        if (item is null) cart.Add(new CartItem { ProductId = id, Quantity = 1 });
        else item.Quantity++;
        SaveCart(cart);
        return RedirectToAction(nameof(Index));
    }
    [HttpPost, ValidateAntiForgeryToken]
    public IActionResult Remove(int id)
    {
        var cart = ReadCart();
        cart.RemoveAll(i => i.ProductId == id);
        SaveCart(cart);
        return RedirectToAction(nameof(Index));
    }
    [HttpPost, ValidateAntiForgeryToken]
    public IActionResult Clear()
    {
        HttpContext.Session.Remove("cart");
        return RedirectToAction(nameof(Index));
    }
}
