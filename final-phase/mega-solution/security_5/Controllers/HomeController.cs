using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
public class HomeController : Controller
{
    [AllowAnonymous] public IActionResult Index() => View();
    [Authorize] public IActionResult Dashboard() => View();
    [Authorize(Roles = "Admin")] public IActionResult Admin() => View();
}
