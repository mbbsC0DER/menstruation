# Practical 1a: Personal details form

Source: `TYIT_ASP_Practs.docx`. Working project: `form_1a/PersonalForm.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `form_1a` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `form_1a/PersonalForm.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **PersonalForm → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **PersonalForm** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5201** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web App (Model-View-Controller)**, choose the C# template, and click **Next**.
2. Name it **PersonalForm** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `form_1a` into the project directory, replacing **PersonalForm.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Controllers/HomeController.cs`
- `Models/PersonalDetails.cs`
- `PersonalForm.csproj`
- `Program.cs`
- `Properties/launchSettings.json`
- `Views/Home/Index.cshtml`
- `Views/Home/Result.cshtml`
- `Views/Shared/_Layout.cshtml`
- `Views/_ViewImports.cshtml`
- `Views/_ViewStart.cshtml`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project PersonalForm.csproj
```

No additional NuGet packages are needed; ASP.NET Core framework libraries come with the SDK.

## Demonstrate the output

1. Open `/` in the browser.
2. Enter **Amit**, contact **9876543210**, location **Thane**, and select **Male**.
3. Select **SSC**, **HSC**, and **Graduate**; click **Submit**.
4. Output: a page showing all five submitted values, including the selected education items.
5. Click **Enter another record**. Submit with no name/contact: the form requests the required fields.

This is the ASP.NET Core equivalent of the document's `.aspx` example. It demonstrates the same inputs/output using MVC. Radio buttons share one property, so only one gender is selected.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [MVC project creation](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0).
