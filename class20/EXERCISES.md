## Exercise 1 -- Add Validation

make the following requirements:

- title cannot be empty
- year must be a positive number

## Exercise 2 -- Add a details page

Create a new route:

dedicate a page to an individual detailed page of the movie.

## Exercise 3 -- Add genre filtering

_this could be a route, it also could be only through query parameters_
_`/movies?genre=Sci-Fi`_

You query only movies that contain a specific genre

```
Movie.query.filter_by(genre=genre).all()
```

## Exercise 4 -- Add a confirmation message

A message appears after create/update/delete on the page.
