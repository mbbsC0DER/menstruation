using System.ComponentModel.DataAnnotations;
public class Student
{
    public int Id { get; set; }
    [Required, StringLength(80)] public string Name { get; set; } = "";
    [Required, EmailAddress] public string Email { get; set; } = "";
    [Required] public string Course { get; set; } = "";
    [Range(0, 100)] public int Marks { get; set; }
}
