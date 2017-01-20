import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        movies =("Rainman", "Mermaids", "All Dogs Go To Heaven", "Batman", "The Witches of Eastwick", "Labyrinth")
        index = random.randint(0, len(movies)-1)
        return (movies[index])
        # TODO: randomly choose one of the movies, and return it

        return "The Big Lebowski"

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        next_movie = self.getRandomMovie()
        content += "<h1>Tomorrow's Movie</h1>"
        content += "<p>" + next_movie + "</p>"

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
