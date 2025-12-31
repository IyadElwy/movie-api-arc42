import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database.connection import SessionLocal, init_db
from app.business.services import MovieService, ActorService, RatingService


def populate_database():
    init_db()
    db = SessionLocal()

    try:
        actor_service = ActorService(db)
        rating_service = RatingService(db)
        movie_service = MovieService(db)

        print("Creating actors...")

        actors_data = [
            ("Tim", "Robbins", date(1958, 10, 16), "American"),
            ("Morgan", "Freeman", date(1937, 6, 1), "American"),
            ("Marlon", "Brando", date(1924, 4, 3), "American"),
            ("Al", "Pacino", date(1940, 4, 25), "American"),
            ("Christian", "Bale", date(1974, 1, 30), "British"),
            ("Heath", "Ledger", date(1979, 4, 4), "Australian"),
            ("Leonardo", "DiCaprio", date(1974, 11, 11), "American"),
            ("Kate", "Winslet", date(1975, 10, 5), "British"),
            ("Tom", "Hanks", date(1956, 7, 9), "American"),
            ("Matthew", "McConaughey", date(1969, 11, 4), "American"),
            ("Anne", "Hathaway", date(1982, 11, 12), "American"),
            ("Keanu", "Reeves", date(1964, 9, 2), "Canadian"),
            ("Laurence", "Fishburne", date(1961, 7, 30), "American"),
            ("Brad", "Pitt", date(1963, 12, 18), "American"),
            ("Edward", "Norton", date(1969, 8, 18), "American"),
            ("Robert", "De Niro", date(1943, 8, 17), "American"),
            ("Jodie", "Foster", date(1962, 11, 19), "American"),
            ("Samuel L.", "Jackson", date(1948, 12, 21), "American"),
            ("John", "Travolta", date(1954, 2, 18), "American"),
            ("Uma", "Thurman", date(1970, 4, 29), "American"),
            ("Harrison", "Ford", date(1942, 7, 13), "American"),
            ("Mark", "Hamill", date(1951, 9, 25), "American"),
            ("Carrie", "Fisher", date(1956, 10, 21), "American"),
            ("Russell", "Crowe", date(1964, 4, 7), "New Zealander"),
            ("Joaquin", "Phoenix", date(1974, 10, 28), "American"),
            ("Scarlett", "Johansson", date(1984, 11, 22), "American"),
            ("Robert", "Downey Jr.", date(1965, 4, 4), "American"),
            ("Chris", "Evans", date(1981, 6, 13), "American"),
            ("Chris", "Hemsworth", date(1983, 8, 11), "Australian"),
            ("Natalie", "Portman", date(1981, 6, 9), "Israeli-American"),
            ("Elijah", "Wood", date(1981, 1, 28), "American"),
            ("Ian", "McKellen", date(1939, 5, 25), "British"),
            ("Viggo", "Mortensen", date(1958, 10, 20), "American"),
            ("Cate", "Blanchett", date(1969, 5, 14), "Australian"),
            ("Daniel", "Radcliffe", date(1989, 7, 23), "British"),
            ("Emma", "Watson", date(1990, 4, 15), "British"),
            ("Rupert", "Grint", date(1988, 8, 24), "British"),
            ("Will", "Smith", date(1968, 9, 25), "American"),
            ("Denzel", "Washington", date(1954, 12, 28), "American"),
            ("Meryl", "Streep", date(1949, 6, 22), "American"),
            ("Jack", "Nicholson", date(1937, 4, 22), "American"),
            ("Jennifer", "Lawrence", date(1990, 8, 15), "American"),
            ("Ryan", "Gosling", date(1980, 11, 12), "Canadian"),
            ("Emma", "Stone", date(1988, 11, 6), "American"),
            ("Matt", "Damon", date(1970, 10, 8), "American"),
            ("Ben", "Affleck", date(1972, 8, 15), "American"),
            ("Robin", "Williams", date(1951, 7, 21), "American"),
            ("Johnny", "Depp", date(1963, 6, 9), "American"),
            ("Orlando", "Bloom", date(1977, 1, 13), "British"),
            ("Keira", "Knightley", date(1985, 3, 26), "British"),
            ("Anthony", "Hopkins", date(1937, 12, 31), "Welsh"),
            ("Sigourney", "Weaver", date(1949, 10, 8), "American"),
            ("Arnold", "Schwarzenegger", date(1947, 7, 30), "Austrian-American"),
            ("Sylvester", "Stallone", date(1946, 7, 6), "American"),
            ("Bruce", "Willis", date(1955, 3, 19), "American"),
            ("Tom", "Cruise", date(1962, 7, 3), "American"),
            ("Nicole", "Kidman", date(1967, 6, 20), "Australian-American"),
            ("George", "Clooney", date(1961, 5, 6), "American"),
            ("Julia", "Roberts", date(1967, 10, 28), "American"),
            ("Sandra", "Bullock", date(1964, 7, 26), "American"),
        ]

        actors = []
        for first_name, last_name, birth_date, nationality in actors_data:
            actor = actor_service.create_actor(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                nationality=nationality
            )
            actors.append(actor)

        print(f"Created {len(actors)} actors")

        print("Creating movies...")

        movies_data = [
            # Movie data: (title, release_date, runtime, synopsis, poster_url, language, genres, budget, revenue, actor_indices)
            ("The Shawshank Redemption", date(1994, 9, 23), 142,
             "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
             "https://example.com/posters/shawshank.jpg", "English", ["Drama", "Crime"], 25000000, 28341469, [0, 1]),

            ("The Godfather", date(1972, 3, 24), 175,
             "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
             "https://example.com/posters/godfather.jpg", "English", ["Crime", "Drama"], 6000000, 246120974, [2, 3]),

            ("The Dark Knight", date(2008, 7, 18), 152,
             "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
             "https://example.com/posters/darkknight.jpg", "English", ["Action", "Crime", "Drama"], 185000000, 1004558444, [4, 5]),

            ("Titanic", date(1997, 12, 19), 195,
             "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
             "https://example.com/posters/titanic.jpg", "English", ["Drama", "Romance"], 200000000, 2187463944, [6, 7]),

            ("Forrest Gump", date(1994, 7, 6), 142,
             "The presidencies of Kennedy and Johnson, the Vietnam War, and other historical events unfold from the perspective of an Alabama man.",
             "https://example.com/posters/forrestgump.jpg", "English", ["Drama", "Romance"], 55000000, 678226465, [8]),

            ("Interstellar", date(2014, 11, 7), 169,
             "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
             "https://example.com/posters/interstellar.jpg", "English", ["Adventure", "Drama", "Sci-Fi"], 165000000, 677471339, [9, 10, 4]),

            ("The Matrix", date(1999, 3, 31), 136,
             "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
             "https://example.com/posters/matrix.jpg", "English", ["Action", "Sci-Fi"], 63000000, 463517383, [11, 12]),

            ("Fight Club", date(1999, 10, 15), 139,
             "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
             "https://example.com/posters/fightclub.jpg", "English", ["Drama"], 63000000, 101218804, [13, 14]),

            ("Taxi Driver", date(1976, 2, 8), 114,
             "A mentally unstable veteran works as a nighttime taxi driver in New York City, where the perceived decadence and sleaze fuels his urge for violent action.",
             "https://example.com/posters/taxidriver.jpg", "English", ["Crime", "Drama"], 1300000, 28262574, [15, 16]),

            ("Pulp Fiction", date(1994, 10, 14), 154,
             "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.",
             "https://example.com/posters/pulpfiction.jpg", "English", ["Crime", "Drama"], 8000000, 213928762, [17, 18, 19]),

            ("Star Wars: A New Hope", date(1977, 5, 25), 121,
             "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy.",
             "https://example.com/posters/starwars.jpg", "English", ["Action", "Adventure", "Fantasy"], 11000000, 775398007, [20, 21, 22]),

            ("Gladiator", date(2000, 5, 5), 155,
             "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
             "https://example.com/posters/gladiator.jpg", "English", ["Action", "Adventure", "Drama"], 103000000, 460583960, [23, 24]),

            ("The Avengers", date(2012, 5, 4), 143,
             "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army.",
             "https://example.com/posters/avengers.jpg", "English", ["Action", "Adventure", "Sci-Fi"], 220000000, 1518815515, [26, 27, 25, 17]),

            ("The Lord of the Rings: The Fellowship of the Ring", date(2001, 12, 19), 178,
             "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring.",
             "https://example.com/posters/lotr1.jpg", "English", ["Adventure", "Drama", "Fantasy"], 93000000, 871368364, [30, 31, 32]),

            ("The Lord of the Rings: The Return of the King", date(2003, 12, 17), 201,
             "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom.",
             "https://example.com/posters/lotr3.jpg", "English", ["Adventure", "Drama", "Fantasy"], 94000000, 1119929521, [30, 31, 32, 33]),

            ("Harry Potter and the Sorcerer's Stone", date(2001, 11, 16), 152,
             "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil.",
             "https://example.com/posters/hp1.jpg", "English", ["Adventure", "Family", "Fantasy"], 125000000, 1007935896, [34, 35, 36]),

            ("Inception", date(2010, 7, 16), 148,
             "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea.",
             "https://example.com/posters/inception.jpg", "English", ["Action", "Adventure", "Sci-Fi"], 160000000, 829895144, [6, 9]),

            ("The Departed", date(2006, 10, 6), 151,
             "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
             "https://example.com/posters/departed.jpg", "English", ["Crime", "Drama", "Thriller"], 90000000, 291465034, [6, 44, 40]),

            ("The Silence of the Lambs", date(1991, 2, 14), 118,
             "A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer.",
             "https://example.com/posters/silenceofthelambs.jpg", "English", ["Crime", "Drama", "Thriller"], 19000000, 272742922, [16, 50]),

            ("Saving Private Ryan", date(1998, 7, 24), 169,
             "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper.",
             "https://example.com/posters/savingprivateryan.jpg", "English", ["Drama", "War"], 70000000, 481840909, [8, 44]),

            ("Good Will Hunting", date(1997, 12, 5), 126,
             "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
             "https://example.com/posters/goodwillhunting.jpg", "English", ["Drama", "Romance"], 10000000, 225933435, [44, 45, 46]),

            ("La La Land", date(2016, 12, 9), 128,
             "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations.",
             "https://example.com/posters/lalaland.jpg", "English", ["Comedy", "Drama", "Music"], 30000000, 446094432, [42, 43]),

            ("Pirates of the Caribbean: The Curse of the Black Pearl", date(2003, 7, 9), 143,
             "Blacksmith Will Turner teams up with eccentric pirate Captain Jack Sparrow to save his love from Jack's former pirate allies.",
             "https://example.com/posters/pirates1.jpg", "English", ["Action", "Adventure", "Fantasy"], 140000000, 654264015, [47, 48, 49]),

            ("Alien", date(1979, 5, 25), 117,
             "After a space merchant vessel receives an unknown transmission, they investigate a nearby planetoid, discovering a deadly organism.",
             "https://example.com/posters/alien.jpg", "English", ["Horror", "Sci-Fi"], 11000000, 104931801, [51]),

            ("The Terminator", date(1984, 10, 26), 107,
             "A human soldier is sent from 2029 to 1984 to stop an almost indestructible cyborg killing machine.",
             "https://example.com/posters/terminator.jpg", "English", ["Action", "Sci-Fi"], 6400000, 78371200, [52]),

            ("Rocky", date(1976, 11, 21), 120,
             "A small-time Philadelphia boxer gets a supremely rare chance to fight the world heavyweight champion in a bout.",
             "https://example.com/posters/rocky.jpg", "English", ["Drama", "Sport"], 1000000, 225000000, [53]),

            ("Die Hard", date(1988, 7, 15), 132,
             "An NYPD officer tries to save his wife and several others taken hostage by German terrorists during a Christmas party.",
             "https://example.com/posters/diehard.jpg", "English", ["Action", "Thriller"], 28000000, 141603197, [54]),

            ("Top Gun", date(1986, 5, 16), 110,
             "As students at the United States Navy's elite fighter weapons school compete to be best in the class, one daring young pilot learns a few things.",
             "https://example.com/posters/topgun.jpg", "English", ["Action", "Drama"], 15000000, 357288178, [55]),

            ("Ocean's Eleven", date(2001, 12, 7), 116,
             "Danny Ocean and his ten accomplices plan to rob three Las Vegas casinos simultaneously.",
             "https://example.com/posters/oceans11.jpg", "English", ["Crime", "Thriller"], 85000000, 450717150, [57, 13, 44]),

            ("The Proposal", date(2009, 6, 19), 108,
             "A pushy boss forces her young assistant to marry her in order to keep her visa status in the U.S. and avoid deportation to Canada.",
             "https://example.com/posters/proposal.jpg", "English", ["Comedy", "Drama", "Romance"], 40000000, 317375031, [59, 42]),

            ("Inception", date(2010, 7, 16), 148,
             "A thief who enters the dreams of others to steal secrets from their subconscious.",
             "https://example.com/posters/inception2.jpg", "English", ["Action", "Sci-Fi", "Thriller"], 160000000, 836836967, [6, 10]),

            ("The Grand Budapest Hotel", date(2014, 3, 28), 99,
             "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka.",
             "https://example.com/posters/budapest.jpg", "English", ["Adventure", "Comedy", "Crime"], 25000000, 174600318, [58]),

            ("Joker", date(2019, 10, 4), 122,
             "In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society.",
             "https://example.com/posters/joker.jpg", "English", ["Crime", "Drama", "Thriller"], 55000000, 1074251311, [24]),

            ("The Lion King", date(1994, 6, 24), 88,
             "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
             "https://example.com/posters/lionking.jpg", "English", ["Animation", "Adventure", "Drama"], 45000000, 968483777, [44]),

            ("Avatar", date(2009, 12, 18), 162,
             "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world.",
             "https://example.com/posters/avatar.jpg", "English", ["Action", "Adventure", "Fantasy"], 237000000, 2787965087, [17, 51]),

            ("Black Panther", date(2018, 2, 16), 134,
             "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future.",
             "https://example.com/posters/blackpanther.jpg", "English", ["Action", "Adventure", "Sci-Fi"], 200000000, 1347280838, [17]),

            ("Spider-Man: No Way Home", date(2021, 12, 17), 148,
             "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help. When a spell goes wrong, dangerous foes from other worlds start to appear.",
             "https://example.com/posters/spiderman.jpg", "English", ["Action", "Adventure", "Fantasy"], 200000000, 1921847111, [11]),

            ("Jurassic Park", date(1993, 6, 11), 127,
             "A pragmatic paleontologist touring an almost complete theme park on an island in Central America is tasked with protecting a couple of kids.",
             "https://example.com/posters/jurassicpark.jpg", "English", ["Action", "Adventure", "Sci-Fi"], 63000000, 1029939903, [17]),

            ("The Social Network", date(2010, 10, 1), 120,
             "As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook.",
             "https://example.com/posters/socialnetwork.jpg", "English", ["Biography", "Drama"], 40000000, 224920315, [11]),

            ("Parasite", date(2019, 5, 30), 132,
             "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
             "https://example.com/posters/parasite.jpg", "Korean", ["Comedy", "Drama", "Thriller"], 11400000, 258870309, []),

            ("1917", date(2019, 12, 25), 119,
             "Two British soldiers are given an impossible mission during World War I to deliver a message deep in enemy territory.",
             "https://example.com/posters/1917.jpg", "English", ["Drama", "War"], 95000000, 384891446, [45]),

            ("Dunkirk", date(2017, 7, 21), 106,
             "Allied soldiers from Belgium, the British Commonwealth and Empire, and France are surrounded by the German Army and evacuated during WWII.",
             "https://example.com/posters/dunkirk.jpg", "English", ["Action", "Drama", "History"], 100000000, 530432122, [8, 55]),

            ("The Prestige", date(2006, 10, 20), 130,
             "After a tragic accident, two stage magicians engage in a battle to create the ultimate illusion while sacrificing everything they have.",
             "https://example.com/posters/prestige.jpg", "English", ["Drama", "Mystery", "Sci-Fi"], 40000000, 109676311, [4, 11]),

            ("Memento", date(2000, 10, 11), 113,
             "A man with short-term memory loss attempts to track down his wife's murderer.",
             "https://example.com/posters/memento.jpg", "English", ["Mystery", "Thriller"], 9000000, 39723096, []),

            ("The Wolf of Wall Street", date(2013, 12, 25), 180,
             "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall.",
             "https://example.com/posters/wolfofwallstreet.jpg", "English", ["Biography", "Crime", "Drama"], 100000000, 392000694, [6]),

            ("Catch Me If You Can", date(2002, 12, 25), 141,
             "A seasoned FBI agent pursues Frank Abagnale Jr. who successfully forged millions of dollars worth of checks.",
             "https://example.com/posters/catchmeifyoucan.jpg", "English", ["Biography", "Crime", "Drama"], 52000000, 352114312, [6, 8]),

            ("The Green Mile", date(1999, 12, 10), 189,
             "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder who has a mysterious gift.",
             "https://example.com/posters/greenmile.jpg", "English", ["Crime", "Drama", "Fantasy"], 60000000, 286801374, [8]),

            ("Cast Away", date(2000, 12, 22), 143,
             "A FedEx executive undergoes a physical and emotional transformation after crash landing on a deserted island.",
             "https://example.com/posters/castaway.jpg", "English", ["Adventure", "Drama", "Romance"], 90000000, 429632142, [8]),

            ("The Truman Show", date(1998, 6, 5), 103,
             "An insurance salesman discovers his whole life is actually a reality TV show.",
             "https://example.com/posters/trumanshow.jpg", "English", ["Comedy", "Drama", "Sci-Fi"], 60000000, 264118201, []),

            ("Whiplash", date(2014, 10, 10), 106,
             "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor.",
             "https://example.com/posters/whiplash.jpg", "English", ["Drama", "Music"], 3300000, 49398953, []),
        ]

        movies = []
        for title, release_date, runtime, synopsis, poster_url, language, genres, budget, revenue, actor_indices in movies_data:
            actor_ids = [actors[i].id for i in actor_indices if i < len(actors)]
            movie = movie_service.create_movie(
                title=title,
                release_date=release_date,
                runtime=runtime,
                synopsis=synopsis,
                poster_url=poster_url,
                language=language,
                genres=genres,
                budget=budget,
                revenue=revenue,
                actor_ids=actor_ids if actor_ids else None
            )
            movies.append(movie)

        print(f"Created {len(movies)} movies")

        print("Creating ratings...")

        # Create multiple ratings for each movie
        import random
        rating_count = 0

        review_templates = [
            "An absolute masterpiece!",
            "One of the best films ever made.",
            "Incredible performances all around.",
            "A cinematic triumph.",
            "Flawless execution from start to finish.",
            "Unforgettable and powerful.",
            "A must-watch classic.",
            "Stunning visuals and compelling story.",
            "Brilliantly directed and acted.",
            "A timeless piece of cinema.",
            "Exceeded all expectations.",
            "Emotionally gripping and beautifully crafted.",
            "A true work of art.",
            "Outstanding in every way.",
            "Simply phenomenal.",
            "Captivating from beginning to end.",
            "A remarkable achievement.",
            "Perfectly executed.",
            "Extraordinary filmmaking.",
            "A cinematic experience like no other."
        ]

        for movie in movies:
            # Create 2-5 ratings per movie
            num_ratings = random.randint(2, 5)
            for i in range(num_ratings):
                score = round(random.uniform(7.0, 10.0), 1)
                review_text = random.choice(review_templates)
                reviewer_email = f"reviewer{rating_count}@example.com"

                rating_service.create_rating(
                    score=score,
                    movie_id=movie.id,
                    review_text=review_text,
                    reviewer_email=reviewer_email
                )
                rating_count += 1

        print(f"Created {rating_count} ratings")

        print("\nDatabase populated successfully!")
        print(f"Total actors: {len(actor_service.get_all_actors())}")
        print(f"Total movies: {len(movie_service.get_all_movies())}")
        print(f"Total ratings: {len(rating_service.get_all_ratings())}")

    except Exception as e:
        print(f"Error populating database: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    populate_database()
