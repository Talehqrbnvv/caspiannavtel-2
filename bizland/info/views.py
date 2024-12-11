from django.shortcuts import render,redirect,get_object_or_404
from .models import TeamMember,Service,FAQ,ContactMessage,Client,PortfolioItem,MenuItem
from .forms import ContactForm
from django.contrib import messages






# Create your views here.
def index(request):
    team_members = TeamMember.objects.all()
    services = Service.objects.all()
    portfolio_items = PortfolioItem.objects.all()  # Tüm portföy öğelerini al
    faqs = FAQ.objects.filter(is_active=True)
    clients = Client.objects.all()
    menu_items = MenuItem.objects.all()


    
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()  
            messages.success(request, 'Mesajınız uğurla gondərildi!')
            form = ContactForm()
        else:
            messages.error(request, 'Problem baş verdi,Xahiş olunur təkrar cəhd edin!')

    return render(request, 'index.html', {
        'form': form,
        'team_members': team_members,
        'services': services,
        'faqs': faqs,
        'clients': clients,
        'portfolio_items': portfolio_items,
        'menu_items': menu_items,
        
    })


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    service_details = service.details.all()  # Ters ilişkiyi kullanarak ServiceDetail'ları alıyoruz
    return render(request, 'service-detail.html', {'service': service, 'service_details': service_details})

