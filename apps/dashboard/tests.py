from apps.dashboard.models import Categoria

# Create your tests here.

if __name__ == '__main__':
    categoria = ['Gastronomía', 'Alojamiento', 'Transporte', 'Comercio']

    for c in categoria:
        try:
            Categoria.objects.create(nombre=c)
        except Exception as e:
            print(e)
    print(Categoria.objects.all())