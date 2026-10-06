using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
public class IndexModel : PageModel
{
    [BindProperty] public Student Student { get; set; } = new();
    public bool Submitted { get; private set; }
    public void OnGet() { }
    public void OnPost()
    {
        if (Student.Id < 1) ModelState.AddModelError("Student.Id", "Roll number must be positive.");
        if (!ModelState.IsValid) return;
        Submitted = true;
    }
}
