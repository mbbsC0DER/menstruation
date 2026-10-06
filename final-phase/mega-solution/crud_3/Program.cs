// Required packages (already referenced in the project):
// dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 10.0.12
// Terminal (in this project folder): dotnet restore; dotnet run
using Microsoft.EntityFrameworkCore;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddDbContext<StudentDb>(options =>
    options.UseSqlite("Data Source=students.db"));
var app = builder.Build();
app.UseRouting();

app.MapControllerRoute("default", "{controller=Students}/{action=Index}/{id?}");
// A fixed small demo schema: create the SQLite database on first run.
using (var scope = app.Services.CreateScope())
    scope.ServiceProvider.GetRequiredService<StudentDb>().Database.EnsureCreated();
app.Run();
