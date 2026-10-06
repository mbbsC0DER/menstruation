using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Caching.Memory;
public class MoviesController(IMemoryCache cache) : Controller
{
    private static readonly string[] theatres = ["IMAX", "PVR", "MOVIEMAX"];
    public IActionResult Index(string theatre = "IMAX")
    {
        if (!theatres.Contains(theatre)) return BadRequest("Select IMAX, PVR or MOVIEMAX.");
        string key = "movies:" + theatre;
        bool fromCache = cache.TryGetValue<MovieData>(key, out var data);
        if (!fromCache || data is null)
        {
            data = new MovieData(["Interstellar", "Inception", "Dune"], DateTimeOffset.UtcNow);
            cache.Set(key, data, TimeSpan.FromSeconds(30));
        }
        return View(new MoviePage(theatre, data, fromCache));
    }
}
