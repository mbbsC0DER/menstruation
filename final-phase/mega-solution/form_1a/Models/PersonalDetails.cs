using System.ComponentModel.DataAnnotations;
public class PersonalDetails
{
    [Required] public string Name { get; set; } = "";
    [Required, Phone] public string Contact { get; set; } = "";
    [Required] public string Location { get; set; } = "Thane";
    [Required] public string Gender { get; set; } = "";
    public string[] Education { get; set; } = [];
}
