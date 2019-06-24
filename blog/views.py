from django.shortcuts import render

# Create your views here.

from blog.models import Blogpost, Blogger, Topic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogpost = Blogpost.objects.all().count()
     
    # The 'all()' is implied by default.    
    num_blogger = Blogger.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_blogpost,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        'num_authors': num_bloggers,
        'num_visits': num_visits,
    }




    
   

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BlogListView(generic.ListView):
    model = Blogpost
    paginate_by = 10

class BlogpostDetailView(generic.DetailView):
    model = Blogpost

