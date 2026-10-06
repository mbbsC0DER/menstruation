// Terminal (in this project folder): dotnet restore; dotnet run

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddDistributedMemoryCache();
builder.Services.AddSession(options => {
    options.Cookie.Name = ".CartDemo.Session";
    options.Cookie.IsEssential = true;
});
var app = builder.Build();
app.UseRouting();
app.UseSession();
app.MapControllerRoute("default", "{controller=Cart}/{action=Index}/{id?}");

app.Run();
