# Practical 8: RESTful student service with Swagger

Source: `Creating RESTFul services.docx`. Working project: `rest_8/StudentRest.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `rest_8` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `rest_8/StudentRest.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **StudentRest → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **StudentRest** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5208** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web API**, choose the C# template, and click **Next**.
2. Name it **StudentRest** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `rest_8` into the project directory, replacing **StudentRest.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Controllers/StudentsController.cs`
- `Data/StudentStore.cs`
- `Models/Student.cs`
- `Program.cs`
- `Properties/launchSettings.json`
- `StudentRest.csproj`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project StudentRest.csproj
```

The `.csproj` already includes the required packages. For manual recreation only:

```powershell
dotnet add package Swashbuckle.AspNetCore --version 10.2.3
```

## Demonstrate the output

1. Open `/swagger`: Swagger UI lists GET, POST, PUT, and DELETE under Students.
2. Expand **GET /api/students**, click **Try it out → Execute**: HTTP 200 returns the seeded student list.
3. Expand **POST /api/students**, click **Try it out**, and use:

   ```json
   { "name": "Priya", "email": "priya@example.com", "course": "BCA", "marks": 88 }
   ```

4. Execute: HTTP **201** returns the created record, generated `id`, and a Location header. Copy the `id`.
5. Execute **GET /api/students/{id}** with that id: HTTP 200 returns the record.
6. Execute **PUT /api/students/{id}** with the same fields and `marks` changed to **95**: HTTP **204** (success with no body).
7. GET the record again: marks are **95**.
8. Execute **DELETE /api/students/{id}**: HTTP **204**.
9. GET that id again: HTTP **404**.
10. POST with an empty name or marks **101**: HTTP **400** validation response.

The service uses an in-memory repository for the simplest working REST demo. Its data resets on restart. Practical 3 is the persistent database example. IDs are assigned by the server and cannot be overwritten by submitted input.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [MVC project creation](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0).
