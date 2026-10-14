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
        pass

    def handleTrovaGruppo(self, e):
        pass
