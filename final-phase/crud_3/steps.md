# Practical 3: Student CRUD with SQLite

Source: `ASP Practical no 3.docx`. Working project: `crud_3/StudentCrud.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `crud_3` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `crud_3/StudentCrud.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **StudentCrud → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **StudentCrud** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5203** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web App (Model-View-Controller)**, choose the C# template, and click **Next**.
2. Name it **StudentCrud** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `crud_3` into the project directory, replacing **StudentCrud.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Controllers/StudentsController.cs`
- `Data/StudentDb.cs`
- `Models/Student.cs`
- `Program.cs`
- `Properties/launchSettings.json`
- `StudentCrud.csproj`
- `Views/Shared/_Layout.cshtml`
- `Views/Students/Details.cshtml`
- `Views/Students/Edit.cshtml`
- `Views/Students/Index.cshtml`
- `Views/_ViewImports.cshtml`
- `Views/_ViewStart.cshtml`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project StudentCrud.csproj
```

The `.csproj` already includes the required packages. For manual recreation only:

```powershell
dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 10.0.12
```

## Demonstrate the output

1. Open `/`: initially the student table is empty.
2. Click **Add student**. Enter Name **Amit**, Email **amit@example.com**, Course **BCA**, Marks **80**; click **Save**.
3. The table shows the new student and an automatically assigned ID.
4. Click **Details**: all fields are displayed.
5. Go back, click **Edit**, change Marks to **90**, and save. Details now shows **90**.
6. Stop and restart the app: the record remains. This verifies database persistence.
7. Click **Delete**: the record disappears.
8. Browse `/Students/Details/99999`: HTTP 404 is expected.

The `students.db` SQLite database is created automatically in the project folder. No SQL Server, LocalDB, migrations, `dotnet-ef`, or manual database creation is needed for this fixed demo schema. Keep the database to preserve records; stop the app and delete it if you need a clean demo.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [MVC project creation](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0).
