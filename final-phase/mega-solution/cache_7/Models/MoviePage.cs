public record MovieData(string[] Movies, DateTimeOffset CreatedAt);
public record MoviePage(string Theatre, MovieData Data, bool FromCache);
