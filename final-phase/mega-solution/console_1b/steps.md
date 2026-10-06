# Practical 1b: Console application and manual testing

Source: `TYIT_ASP_Practs.docx`. Working project: `console_1b/SquareDemo.csproj`.

## Visual Studio 2026 setup (once)

1. On Windows, open **Visual Studio Installer**.
2. Find **Visual Studio 2026 → Modify → Workloads**.
3. Select **ASP.NET and web development**. For the console practical, also select **.NET desktop development** if the Console App template is absent.
4. In **Individual components**, ensure the **.NET 10 SDK** is installed. Click **Modify** and wait for installation.
5. Open Visual Studio 2026. These projects target **.NET 10.0**. [Microsoft's VS 2026 compatibility list](https://learn.microsoft.com/en-us/visualstudio/releases/2026/compatibility) confirms .NET 10 support.

## Run the provided project (recommended)

1. Keep every file inside `console_1b` together.
2. In Visual Studio select **File → Open → Project/Solution**.
3. Browse to `console_1b/SquareDemo.csproj` and click **Open**.
4. Wait for NuGet restore. If needed, right-click the solution → **Restore NuGet Packages**.
5. If your solution contains other projects, right-click **SquareDemo → Set as Startup Project**.
6. Select **Build → Build Solution** (Ctrl+Shift+B). Fix any restore failure before running.
7. Press **Ctrl+F5**. A console window opens.
8. Close the console when finished.

This is a .NET Console App, not a Console App (.NET Framework).

## If creating the project yourself

1. **File → New → Project**. Search for **Console App**, choose the C# template, and click **Next**.
2. Name it **SquareDemo** and choose a new empty location. Click **Next**.
3. Select **.NET 10.0** and leave top-level statements enabled.
4. Click **Create**. Close the project before replacing files.
5. Remove starter **Program.cs**, **Controllers**, **Models**, **Views**, **Pages**, **Properties**, **Data**, **Areas**, and **wwwroot** folders when present; these practicals include their complete replacements. Keep only project files outside those folders that you still need.
6. Copy all the supplied files from `console_1b` into the project directory, replacing **SquareDemo.csproj** too. Reopen that `.csproj`, restore NuGet packages, build, and run as above.

## Files and code

Every code file is provided separately. Open it directly; no code is hidden in the document.

- `Program.cs`
- `SquareDemo.csproj`

## Terminal alternative

Open **View → Terminal**, change to the folder containing the `.csproj`, and run:

```powershell
dotnet restore
dotnet run --project SquareDemo.csproj
```

No additional NuGet packages are needed; ASP.NET Core framework libraries come with the SDK.

## Demonstrate the output

1. Enter **Amit** at the name prompt: output includes `Hello, Amit!`.
2. Enter **5**: output `The square of 5 is 25.`
3. Enter **-3**: output `The square of -3 is 9.`
4. Enter **abc**: output asks for an integer.
5. Enter **quit**: output `Testing complete.` and the program exits.

A `long` result prevents overflow when squaring a valid 32-bit integer. End-of-input also exits cleanly.

## If something fails

- **net10.0 not supported:** update VS 2026 and install the .NET 10 SDK; check `dotnet --list-sdks`.
- **NuGet restore failed:** connect to the internet and restore again.

Reference: [MVC project creation](https://learn.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-10.0).
