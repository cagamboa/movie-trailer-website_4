import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_video_info(self):
        print("Title = " + self.title)
        print("Duration = " + str(self.duration))
        
class Movie(Video):
    """This class provides a way to store movie related information."""
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, title, duration, movie_storyline, post_image,
                 trailer_youtube, rotten_tomatoes, genre):
        Video.__init__(self, title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = post_image
        self.trailer_youtube_url = trailer_youtube
        self.rotten_tomatoes = rotten_tomatoes
        self.genre = genre
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_video_info(self):
        print("Title = " + self.title)
        print("Duration = " + str(self.duration))
        print("Storyline = " + self.storyline)
        

class TvShow(Video):
    """This class provides a way to store tv series information."""

    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        print("Title = " + self.title)
        print("TV Station = " +self.tv_station)

    def show_video_info(self):
        print("Title = " + self.title)
        print("Duration = " + str(self.duration))
        print("Season = " + str(self.season))
        




