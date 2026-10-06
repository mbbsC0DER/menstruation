// Required packages (already referenced in the project):
// dotnet add package Swashbuckle.AspNetCore --version 10.2.3
// Terminal: dotnet restore; dotnet run
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddSingleton<StudentStore>();
var app = builder.Build();
app.UseSwagger();
app.UseSwaggerUI();
app.MapGet("/", () => Results.Redirect("/swagger"));
app.MapControllers();
app.Run();
