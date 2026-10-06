# Practical 10: Razor Pages and Tag Helpers

Source: `Practical 10_ Razor Pages and Tag Helpers.docx`. Working project: `razor_10/RazorStudent.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `razor_10` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `razor_10/RazorStudent.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **RazorStudent → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **RazorStudent** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5210** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web App (Razor Pages)**, choose the C# template, and click **Next**.
2. Name it **RazorStudent** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `razor_10` into the project directory, replacing **RazorStudent.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Models/Student.cs`
- `Pages/Index.cshtml`
- `Pages/Index.cshtml.cs`
- `Pages/Shared/_Layout.cshtml`
- `Pages/_ViewImports.cshtml`
- `Pages/_ViewStart.cshtml`
- `Program.cs`
- `Properties/launchSettings.json`
- `RazorStudent.csproj`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project RazorStudent.csproj
```

No additional NuGet packages are needed; ASP.NET Core framework libraries come with the SDK.

## Demonstrate the output

1. Open `/`.
2. Enter Roll number **1**, Name **Amit**, Email **amit@example.com**, select Course **BCA**, and Marks **85**.
3. Click **Submit**: a **Submitted Student** section displays those values below the form.
4. Click **Clear form**: input fields are reset.
5. Leave the name empty or enter an invalid email: the browser requires a correction. Server-side validation also checks submitted data.

`Index.cshtml.cs` contains the PageModel and `[BindProperty]`. `Index.cshtml` uses `asp-for`, `asp-validation-for`, and `asp-page`; the form tag helper adds its anti-forgery token automatically. This practical demonstrates a submitted result, not database persistence.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [Razor Pages](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-10.0).
