from django.shortcuts import render

def home(request):
    datos = {
        'perfil': {
            'nombre': 'Elkin Joshua Delgado Lopez',
            'titulo': 'Estudiante de Tecnología de la Información',
            'universidad': 'ULEAM',
            'descripcion': 'Apasionado por el desarrollo web, Python y despliegue de aplicaciones en la nube.',
        },

        'contacto': {
            'email': 'elkinjoshuadelgadolopez@email.com',
            'telefono': '+593 98 350 6478',
            'direccion': 'Manta, Ecuador',
        },

        'habilidades': [
            'HTML', 'CSS', 'JavaScript',
            'Python', 'Django',
            'PostgreSQL', 'Git'
        ],

        'formacion': [
            {
                'nivel': 'Educación Superior',
                'institucion': 'Universidad Laica Eloy Alfaro de Manabí',
                'detalle': 'Tecnología de la Información',
            }
        ],

        'experiencia': [
            {
                'puesto': 'Practicante TI',
                'empresa': 'Proyectos Académicos',
                'descripcion': 'Desarrollo de páginas web, prácticas con Python y despliegue en Render y GitHub Pages.',
            }
        ],

        'proyectos': [
            {
                'titulo': 'Práctica de Render',
                'descripcion': 'Página web navideña desplegada en la plataforma Render.',
                'url': 'https://proyecto2025-4v99.onrender.com'
            },
            {
                'titulo': 'Página Web Navideña',
                'descripcion': 'Página estática con temática navideña publicada en GitHub Pages.',
                'url': 'https://joshua391125.github.io/josu-391125.github.io/'
            }
        ],

        'cursos': [
            {
                'nombre': 'Certificado de Python',
                'institucion': 'Curso de Python',
                'url': 'https://drive.google.com/file/d/1tZPwiW_oej5h-0QWprymZMOkrUFMGDwi/view?usp=drive_link'
            },
            {
                'nombre': 'Certificado Académico',
                'institucion': 'Formación Complementaria',
                'url': 'https://drive.google.com/file/d/1tZPwiW_oej5h-0QWprymZMOkrUFMGDwi/view?usp=drive_link'
            }
        ],

        'referencias': [
            {
                'nombre': 'Ing. Marcos Alvarado',
                'telefono': '0992807826'
            },
            {
                'nombre': 'Lic. Jamileth Delgado',
                'telefono': '0987835167'
            }
        ]
    }

    return render(request, 'hoja-de-vida.html', {'datos': datos})
