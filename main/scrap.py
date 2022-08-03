from requests_html import HTMLSession
from newspaper import Article
import nest_asyncio
import os.path
nest_asyncio.apply()


def obtener_noticias():

    session = HTMLSession()
    categoria = input("Ingrese la categoria que desea realizar scrapping, (Deje en blanco si quiere traer noticias aleatorias): ")
    url = 'https://www.lanacion.com.ar/'+categoria
    r = session.get(url)

    if categoria == "":
        location = 'test'
    else:
        location = 'train_'+categoria


    ## Busco todos los articulos existentes
    articles = r.html.find('article')

    #Creo una lista en donde luego voy a guardar los links de todas las noticias
    lista_links = []


    #Recorro todos los articulos y busco las etiquetas h2 las cuales contienen el link de cada noticia y los extraigo en la lista --> "lista_links" (Use try and except para evitar errores)

    try:
        for item in articles:

            newsitem = item.find('h2', first=True)

            newsarticle = {
                'link' : newsitem.absolute_links
            }

            for i in newsarticle['link']:
                lista_links.append(i)

    except AttributeError:
        pass

    
    # Generador de Noticias

    c = 0
    for i in lista_links:
        
        c += 1
        url_n = i
        my_article = Article(url_n, language = "es")
        my_article.download()
        my_article.parse()
        my_article.nlp()
        
        path = f'C:\\Users\\fabri\\Clasificador_PLN\\main\\{location}\\'


        archivo = open(f"{path}noticia_"+str(categoria)+"_"+str(c)+".txt", "w", encoding="UTF-8")
        #Extraer el titulo
        archivo.write(my_article.title+"\n\n")
        #Escribo el contenido
        archivo.write(my_article.text)
        #Cierro Archivo
        archivo.close()  



obtener_noticias()