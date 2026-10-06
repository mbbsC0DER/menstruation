using Microsoft.AspNetCore.Mvc;
public class HomeController : Controller
{
    [HttpGet] public IActionResult Index() => View(new PersonalDetails());
    [HttpPost, ValidateAntiForgeryToken]
    public IActionResult Index(PersonalDetails details)
    {
        if (!ModelState.IsValid) return View(details);
        return View("Result", details);
    }
}
