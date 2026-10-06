// Terminal: dotnet run
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers();
builder.Services.AddScoped<IStudentService, StudentService>();
var app = builder.Build();
app.MapGet("/", () => "Try /api/students/101/details or /api/students/101/name");
app.MapControllers();
app.Run();
