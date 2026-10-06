# Practical 7: Movie listings with caching

Source: `pract7 Caching.docx`. Working project: `cache_7/CacheDemo.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `cache_7` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `cache_7/CacheDemo.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **CacheDemo → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **CacheDemo** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5207** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web App (Model-View-Controller)**, choose the C# template, and click **Next**.
2. Name it **CacheDemo** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `cache_7` into the project directory, replacing **CacheDemo.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `CacheDemo.csproj`
- `Controllers/MoviesController.cs`
- `Models/MoviePage.cs`
- `Program.cs`
- `Properties/launchSettings.json`
- `Views/Movies/Index.cshtml`
- `Views/Shared/_Layout.cshtml`
- `Views/_ViewImports.cshtml`
- `Views/_ViewStart.cshtml`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project CacheDemo.csproj
```

No additional NuGet packages are needed; ASP.NET Core framework libraries come with the SDK.

## Demonstrate the output

1. Open `/`: select **IMAX** and click **Show movies**.
2. On the first request for a theatre, Source shows **Fresh data** with a creation timestamp.
3. Refresh immediately: Source shows **Reading from cache** and the creation timestamp stays identical.
4. Select **PVR**: it gets its own cache entry. Return to IMAX within its 30-second lifetime: the original entry is reused.
5. Wait at least **31 seconds** from the entry's creation, then refresh: Source is **Fresh data** and the timestamp changes.

The first browser page load may already populate IMAX. If it already says cached, select an unused theatre or restart the app. This version caches data with ASP.NET Core `IMemoryCache`, rather than a Web Forms UI control. Expiry is absolute: refreshing does not extend its 30-second life.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [In-memory caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/memory?view=aspnetcore-10.0).
