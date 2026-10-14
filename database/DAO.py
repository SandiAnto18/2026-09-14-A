from database.DB_connect import DBConnect
from model.Actor import Actor
from model.Movie import Movie


class DAO():

    # RECUPERA TUTTI I RATING DISPONIBILI
    @staticmethod
    def getAllRatings(min,max):
        conn = DBConnect.get_connection()

        results = []

        # USO dictionary=True PER ACCEDERE AI DATI CON IL NOME DELLA COLONNA
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT DISTINCT avg_rating
        FROM ratings r
        where r.avg_rating >= %s and r.avg_rating <= %s
        ORDER BY avg_rating
        """

        cursor.execute(query,(min,max))

        # SCORRO LE RIGHE RESTITUITE DAL DATABASE
        for row in cursor:
            results.append(row["avg_rating"])

        cursor.close()
        conn.close()

        return results

#interpreti/registi NAMES
    @staticmethod
    def getActors(min,max):
        conn = DBConnect.get_connection()

        results = []

        # USO dictionary=True PER ACCEDERE AI DATI CON IL NOME DELLA COLONNA
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT n.*
        FROM names n,role_mapping rm ,movie m ,ratings r 
        where r.avg_rating >= %s and r.avg_rating <= %s
        and n.id=rm.name_id 
        and (rm.category = "actor" or rm.category ="actress")
        and rm.movie_id =m.id 
        and m.id=r.movie_id 
        
        """

        cursor.execute(query,(min,max))

        # SCORRO LE RIGHE RESTITUITE DAL DATABASE
        for row in cursor:
            results.append(Actor(**row))

        cursor.close()
        conn.close()

        return results

    def getFilmsByActor(id):
        conn = DBConnect.get_connection()

        results = []

        # USO dictionary=True PER ACCEDERE AI DATI CON IL NOME DELLA COLONNA
        cursor = conn.cursor(dictionary=True)

        query = """
        select m.*
from movie m,role_mapping rm ,names n
where m.id =rm.movie_id 
and n.id=rm.name_id 
and n.id=%s

        """

        cursor.execute(query, (id,))

        # SCORRO LE RIGHE RESTITUITE DAL DATABASE
        for row in cursor:
            results.append(Movie(**row))

        cursor.close()
        conn.close()

        return results

    @staticmethod
    def getA1A2Peso(min, max):
        conn = DBConnect.get_connection()

        results = []

        # USO dictionary=True PER ACCEDERE AI DATI CON IL NOME DELLA COLONNA
        cursor = conn.cursor(dictionary=True)

        query = """
        select distinct n.id as actor1,n2.id as actor2,count(m.id) as peso
from movie m,role_mapping rm ,names n,names n2,movie m2,role_mapping rm2,ratings r 
where m.id =rm.movie_id 
and n.id=rm.name_id 
and m2.id =rm2.movie_id 
and n2.id =rm2.name_id 
and m.id =m2.id
and m.id=r.movie_id 
and r.avg_rating >=%s
and r.avg_rating <= %s
and n.id < n2.id
and (rm.category ="actor" or rm.category="actress")
and (rm2.category ="actor" or rm2.category="actress")
group by actor1 ,actor2 


        """

        cursor.execute(query, (min, max))

        # SCORRO LE RIGHE RESTITUITE DAL DATABASE
        for row in cursor:
            results.append((row["actor1"],row["actor2"],row["peso"]))

        cursor.close()
        conn.close()

        return results










