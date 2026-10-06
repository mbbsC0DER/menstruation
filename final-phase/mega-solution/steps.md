# Mega Solution — C# and ASP.NET Core practicals 1–10

Copy this **entire mega-solution folder** to your Windows computer. All project files, code, views, test references, and launch profiles are included inside it. The separate basic examples are not included.

## Open in Visual Studio 2026

1. Install the **ASP.NET and web development** workload and **.NET 10 SDK** through **Visual Studio Installer → Modify**. The console project also uses .NET 10.
2. Open Visual Studio 2026 → **File → Open → Project/Solution**.
3. Select **MegaSolution.sln** in the copied folder. Open the solution file, rather than an individual code file.
4. Allow NuGet packages to restore. Internet is needed for the initial package download.
5. Select **Build → Build Solution** (Ctrl+Shift+B).
6. In Solution Explorer, right-click the project for the required practical → **Set as Startup Project**.
7. In the Run dropdown, select that project's named profile, then press **Ctrl+F5**. The web projects launch on their fixed localhost ports.
8. Stop the running practical before switching. Read that practical's own **steps.md** for inputs and expected outputs.

Each ASP.NET example has its own application setup, controllers, and views. Select its startup project to switch practicals; no code needs to be commented out. Projects build together, but only the selected startup project runs.

## Select the practical

| Practical | Startup project | Code folder | Browser URL |
|---|---|---|---|
| 1a — Personal details form | PersonalForm | form_1a | http://localhost:5201 |
| 1b — Console and manual testing | SquareDemo | console_1b | Console window |
| 2 — Calculator API | CalculatorAPI | tests_2/CalculatorAPI | http://localhost:5202 |
| 3 — CRUD with SQLite | StudentCrud | crud_3 | http://localhost:5203 |
| 4 — Shopping cart | CartDemo | cart_4 | http://localhost:5204 |
| 5 — Login and roles | SecurityDemo | security_5 | http://localhost:5205 |
| 6 — Routing and DI | RoutingDemo | routes_6 | http://localhost:5206 |
| 7 — Caching | CacheDemo | cache_7 | http://localhost:5207 |
| 8 — REST and Swagger | StudentRest | rest_8 | http://localhost:5208/swagger |
| 9 — Controllers and views | StudentMvc | mvc_9 | http://localhost:5209 |
| 10 — Razor Pages and Tag Helpers | RazorStudent | razor_10 | http://localhost:5210 |

**Practical 2 tests:** select **Test → Test Explorer → Run All Tests**. Expected: **6 passed**. CalculatorTests is a test project; run its tests in Test Explorer rather than selecting it as the web startup project.

**Practical 5 demo admin:** `admin@example.com` / `Admin123!`. New registrations receive the User role. See `security_5/steps.md` for the full login/authorization demonstration.

The CRUD and security apps create their SQLite databases automatically. No external database server is required. The cart, cache, and REST examples keep temporary data in memory.

## Commands instead of clicking Run

Open **View → Terminal**, then change to this mega-solution folder. Run the shared setup once:

```powershell
# First run: restore packages and build every project.
dotnet restore MegaSolution.sln
dotnet build MegaSolution.sln
```

Choose **one** run command below. Stop it with **Ctrl+C** before running another:

```powershell
# Practical 1a
dotnet run --project form_1a/PersonalForm.csproj
# Practical 1b
dotnet run --project console_1b/SquareDemo.csproj
# Practical 2 API
dotnet run --project tests_2/CalculatorAPI/CalculatorAPI.csproj
# Practical 2 tests (does not start the API)
dotnet test tests_2/CalculatorTests/CalculatorTests.csproj
# Practical 3
dotnet run --project crud_3/StudentCrud.csproj
# Practical 4
dotnet run --project cart_4/CartDemo.csproj
# Practical 5
dotnet run --project security_5/SecurityDemo.csproj
# Practical 6
dotnet run --project routes_6/RoutingDemo.csproj
# Practical 7
dotnet run --project cache_7/CacheDemo.csproj
# Practical 8
dotnet run --project rest_8/StudentRest.csproj
# Practical 9
dotnet run --project mvc_9/StudentMvc.csproj
# Practical 10
dotnet run --project razor_10/RazorStudent.csproj
```

Commands are also included as comments in the projects' Program.cs files. If NuGet restore fails, check the internet connection. If net10.0 is unsupported, install the .NET 10 SDK through the Visual Studio Installer. If a port is already in use, stop the previous copy of that app.

References: [Microsoft solution/project documentation](https://learn.microsoft.com/en-us/visualstudio/ide/solutions-and-projects-in-visual-studio), [startup project selection](https://learn.microsoft.com/en-us/visualstudio/ide/how-to-set-multiple-startup-projects).
