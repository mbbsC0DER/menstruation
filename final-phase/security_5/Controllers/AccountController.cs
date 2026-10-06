using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
public class AccountController(UserManager<IdentityUser> users, SignInManager<IdentityUser> signIn) : Controller
{
    [HttpGet] public IActionResult Register() => View(new AccountForm());
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Register(AccountForm form)
    {
        if (!ModelState.IsValid) return View(form);
        var user = new IdentityUser { UserName = form.Email, Email = form.Email };
        var result = await users.CreateAsync(user, form.Password);
        if (!result.Succeeded)
        {
            foreach (var error in result.Errors) ModelState.AddModelError("", error.Description);
            return View(form);
        }
        var roleResult = await users.AddToRoleAsync(user, "User");
        if (!roleResult.Succeeded) throw new InvalidOperationException("Could not assign User role.");
        await signIn.SignInAsync(user, isPersistent: false);
        return RedirectToAction("Dashboard", "Home");
    }
    [HttpGet] public IActionResult Login() => View(new AccountForm());
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Login(AccountForm form)
    {
        if (!ModelState.IsValid) return View(form);
        var result = await signIn.PasswordSignInAsync(form.Email, form.Password, false, false);
        if (result.Succeeded) return RedirectToAction("Dashboard", "Home");
        ModelState.AddModelError("", "Invalid email or password.");
        return View(form);
    }
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Logout()
    {
        await signIn.SignOutAsync();
        return RedirectToAction("Index", "Home");
    }
    public IActionResult Denied()
    {
        Response.StatusCode = 403;
        return View();
    }
}
