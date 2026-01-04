from django.shortcuts import render

def home(request):
    datos = {
        'perfil': {
            'nombre': 'Elkin Joshua Delgado Lopez',
            'titulo': 'Estudiante de Tecnología de la Información',
            'universidad': 'ULEAM',
            'descripcion': 'Apasionado por el desarrollo web y bases de datos.',
        },

        'contacto': {
            'email': 'elkin@email.com',
            'telefono': '+593 999 999 999',
            'direccion': 'Manta, Ecuador',
        },

        'formacion': [
            {
                'nivel': 'Educación Superior',
                'institucion': 'Universidad Laica Eloy Alfaro de Manabí',
                'detalle': 'Tecnología de la Información',
            },
            {
                'nivel': 'Educación Secundaria',
                'institucion': 'Unidad Educativa X',
                'detalle': 'Bachillerato',
            },
        ],

        'habilidades': [
            'HTML', 'CSS', 'JavaScript',
            'Python', 'Django',
            'PostgreSQL', 'Git'
        ],

        'experiencia': [
            {
                'puesto': 'Practicante TI',
                'empresa': 'Empresa X',
                'descripcion': 'Soporte técnico y desarrollo básico.',
            }
        ],

        'cursos': [
            {
                'nombre': 'Python Básico',
                'institucion': 'Microsoft',
            },
            {
                'nombre': 'Bases de Datos',
                'institucion': 'Cisco',
            }
        ]
    }

    return render(request, 'hoja-de-vida.html', {'datos': datos})

