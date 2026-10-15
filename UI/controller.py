import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handleCreaGrafo(self, e):
        # Leggo i valori inseriti nei campi di testo
        # uso float perchè rating è numerico: 7.0
        min_rating= float(self._view._txtRatingMin.value)
        max_rating= float(self._view._txtRatingMax.value)

        #passo i 2 valori al MODEL
        risultati= self._model.getAllRatings(min_rating,max_rating)
        #VERIFICA CHE PRENDI I VALORI NEL RATING
        print (risultati)
        # ATTENZIONE ARRIVA UNA LISTA DA MODEL.PY
        # e per il numero di nodi devo stampare un numero quindi uso len
        self._model.buildGraph(min_rating,max_rating)
        # devo costruire il grafo
        self._view._txt_result.controls.clear()
        # comando per aggiungere righe testuali/numero in output
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi:{self._model.getNodes()}"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di archi:{self._model.getEdges()}"))

        self._view.update_page()

    def handleStampaInfo(self, e):
        # PULISCO L'AREA DEI RISULTATI
        self._view._txt_result.controls.clear()

        # ARTISTA CON GRADO MAGGIORE
        artistDegree, grado = self._model.getArtistMaxDegree()
        self._view._txt_result.controls.append(
            ft.Text(f"ATTORE CON GRADO MAGGIORE: {artistDegree} (grado: {grado})")

        )

        # ARTISTA CON SOMMA DEI PESI INCIDENTI MASSIMA
        artistWeight, somma = self._model.getArtistMaxWeight()

        self._view._txt_result.controls.append(
            ft.Text(f"ATTORE CON SOMMA DEI PESI INCIDENTI MASSIMA: {artistWeight}(somma:{somma})")
        )
        self._view.update_page()

        # TOP 5 ARCHI DI PESO MAGGIORE
        topEdges = self._model.getTop5Edges()
        self._view._txt_result.controls.append(
            ft.Text("TOP 5 ARCHI DI PESO MAGGIORE:")
        )

        # STAMPO I 5 ARCHI con numerazione
        for i, (artist1, artist2, data) in enumerate(topEdges, start=1):
            self._view._txt_result.controls.append(
                ft.Text(f"{i}. {artist1} -- {artist2}: (peso = {data['weight']})")
            )

        # Recupero dal Model l'attore più giovane e quello più anziano
        youngest = self._model.getYoungestActor()
        oldest = self._model.getOldestActor()

        # Controllo che entrambi gli attori siano stati trovati
        if youngest is not None and oldest is not None:

            # Stampo il nome dell'attore più giovane e la sua data di nascita
            self._view._txt_result.controls.append(
                ft.Text(f"Attore più giovane: {youngest} (nato il {youngest.date_of_birth})")
            )

            # Stampo il nome dell'attore più anziano e la sua data di nascita
            self._view._txt_result.controls.append(
                ft.Text(f"Attore più anziano: {oldest} (nato il {oldest.date_of_birth})")
            )

        # Se non è possibile trovare entrambi gli attori con una data valida
        else:
            # Mostro un messaggio informativo, senza generare errori
            self._view._txt_result.controls.append(
                ft.Text("Data di nascita non disponibile per gli attori nel grafo.")
            )
        self._view.update_page()
    def handleTrovaGruppo(self, e):
        pass
