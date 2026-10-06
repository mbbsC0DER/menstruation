// Required packages (already referenced in the project):
// dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 10.0.12
// dotnet add package Microsoft.AspNetCore.Identity.EntityFrameworkCore --version 10.0.12
// Terminal (in this project folder): dotnet restore; dotnet run
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddDbContext<AuthDb>(o => o.UseSqlite("Data Source=accounts.db"));
builder.Services.AddIdentity<IdentityUser, IdentityRole>()
    .AddEntityFrameworkStores<AuthDb>().AddDefaultTokenProviders();
builder.Services.ConfigureApplicationCookie(o => {
    o.Cookie.Name = ".SecurityDemo.Auth";
    o.LoginPath = "/Account/Login";
    o.AccessDeniedPath = "/Account/Denied";
});
var app = builder.Build();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.MapControllerRoute("default", "{controller=Home}/{action=Index}/{id?}");
using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AuthDb>();
    await db.Database.EnsureCreatedAsync();
    var roles = scope.ServiceProvider.GetRequiredService<RoleManager<IdentityRole>>();
    foreach (var role in new[] { "Admin", "User" })
        if (!await roles.RoleExistsAsync(role)) await roles.CreateAsync(new IdentityRole(role));
    var users = scope.ServiceProvider.GetRequiredService<UserManager<IdentityUser>>();
    const string email = "admin@example.com";
    var admin = await users.FindByEmailAsync(email);
    if (admin is null)
    {
        admin = new IdentityUser { UserName = email, Email = email, EmailConfirmed = true };
        var result = await users.CreateAsync(admin, "Admin123!"); // Local practical demo account.
        if (!result.Succeeded) throw new InvalidOperationException(string.Join("; ", result.Errors.Select(e => e.Description)));
    }
    if (!await users.IsInRoleAsync(admin, "Admin")) await users.AddToRoleAsync(admin, "Admin");
}
app.Run();
