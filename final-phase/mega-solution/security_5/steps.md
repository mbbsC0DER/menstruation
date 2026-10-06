# Practical 5: Identity authentication and role authorization

Source: `Practical 5_ Implementing Security to an Application.docx`. Working project: `security_5/SecurityDemo.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `security_5` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `security_5/SecurityDemo.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **SecurityDemo → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. In the run dropdown select **SecurityDemo** (the project profile), then press **Ctrl+F5**. Open **http://localhost:5205** if the browser does not open automatically.
8. Stop the server with **Shift+F5** when debugging, or close its console window / press Ctrl+C when running without the debugger.

The supplied launch profile uses HTTP on a fixed localhost port, so no development-certificate setup is required. Select the project profile rather than IIS Express to use the URL above.

## If creating the project yourself

1. **File → New → Project**. Search for **ASP.NET Core Web App (Model-View-Controller)**, choose the C# template, and click **Next**.
2. Name it **SecurityDemo** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0**, **Authentication: None**, disable container support, and uncheck **Configure for HTTPS** if shown. For Web API, enable **Use controllers** and disable the template OpenAPI option; the supplied Program.cs controls API setup.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `security_5` into the project directory, replacing **SecurityDemo.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

For practical 5, choose Authentication **None** when following these files: the included code configures ASP.NET Core Identity itself. Selecting Individual Accounts would add a second set of starter authentication files.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Controllers/AccountController.cs`
- `Controllers/HomeController.cs`
- `Data/AuthDb.cs`
- `Models/AccountForm.cs`
- `Program.cs`
- `Properties/launchSettings.json`
- `SecurityDemo.csproj`
- `Views/Account/Denied.cshtml`
- `Views/Account/Login.cshtml`
- `Views/Account/Register.cshtml`
- `Views/Home/Admin.cshtml`
- `Views/Home/Dashboard.cshtml`
- `Views/Home/Index.cshtml`
- `Views/Shared/_Layout.cshtml`
- `Views/_ViewImports.cshtml`
- `Views/_ViewStart.cshtml`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project SecurityDemo.csproj
```

The `.csproj` already includes the required packages. For manual recreation only:

```powershell
dotnet add package Microsoft.EntityFrameworkCore.Sqlite --version 10.0.12
dotnet add package Microsoft.AspNetCore.Identity.EntityFrameworkCore --version 10.0.12
```

## Demonstrate the output

1. Open `/`: the **Public Page** is visible without login.
2. Click **Dashboard** while logged out: the app redirects to Login.
3. Click **Public page**, then **Register**. Use **student@example.com** and password **Student123!**.
4. Registration signs in the new user and assigns the **User** role. The dashboard displays the email.
5. Click **Admin page**: output **Access denied** with HTTP 403 after the authorization redirect.
6. Return to Dashboard and click **Logout**. Dashboard now requires login again.
7. Click **Login** and use the seeded local demo account:
   - Email: **admin@example.com**
   - Password: **Admin123!**
8. Click **Admin page**: output **Admin Panel**.
9. Log out. Enter an incorrect password on Login: the page shows `Invalid email or password.`

`accounts.db` is created automatically. ASP.NET Core Identity stores password hashes, signs in users with a cookie, and checks roles. The code creates Admin/User roles and a demo admin so role authorization can actually be shown. New registrations always receive User, not Admin. This small demo does not require an email-confirmation service or SQL Server. Identity's standard password requirements apply; the example passwords above meet them.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.
- **Port already in use:** stop the older copy of this practical. If changing the port in `Properties/launchSettings.json`, use that new URL.

Reference: [ASP.NET Core Identity](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0).
