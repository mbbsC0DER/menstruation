# Practical 6: URL routing and dependency injection

Source: `ASP_NET_Core_URL_Routing_and_Dependency_Injection_Practical.docx`. Working project: `routes_6/RoutingDemo.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `routes_6` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `routes_6/RoutingDemo.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **RoutingDemo → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **RoutingDemo** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5206** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web API**, choose the C# template, and click **Next**.
2. Name it **RoutingDemo** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `routes_6` into the project directory, replacing **RoutingDemo.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Controllers/StudentsController.cs`
- `Program.cs`
- `Properties/launchSettings.json`
- `RoutingDemo.csproj`
- `Services/StudentService.cs`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project RoutingDemo.csproj
```

No additional NuGet packages are needed; ASP.NET Core framework libraries come with the SDK.

## Demonstrate the output

Open these browser URLs after starting:

| Path | Expected output |
|---|---|
| `/api/students` | Student Management System is running. |
| `/api/students/101` | Student ID: 101 |
| `/api/students/101/details` | JSON with id 101, name Rahul Sharma, course BCA |
| `/api/students/101/name` | Rahul Sharma |
| `/api/students/110/details` | HTTP 404, Student not found |

`IStudentService` is registered with `AddScoped` in Program.cs. ASP.NET Core injects its implementation into the controller's constructor. All route examples are retained in the final controller.

The source document says practical 5; the supplied index assigns this topic to **6**, which is used here.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [MVC project creation](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0).
