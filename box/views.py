from django.shortcuts import render

def BoxPage(request, imdb_no):

    return render(request, 'box_page.html', {
        'imdb_no': imdb_no
    })

def PosterBoxPage(request, imdb_no):

    return render(request, 'poster_box_page.html', {
        'imdb_no': imdb_no
    })

def ActorOfTheFilmBoxPage(request, imdb_no):

    return render(request, 'actors_of_the_film_box_page.html', {
        'imdb_no': imdb_no,

    })

def IndexPage(request):
    return render(request, 'index.html', {
        'host': request.get_host()
    })
