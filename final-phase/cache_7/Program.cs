// Terminal (in this project folder): dotnet restore; dotnet run

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddMemoryCache();
var app = builder.Build();
app.UseRouting();

app.MapControllerRoute("default", "{controller=Movies}/{action=Index}/{id?}");

app.Run();
