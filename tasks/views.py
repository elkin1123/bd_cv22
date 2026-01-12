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

        # 🔹 FORMACIÓN (bien acomodada)
        'formacion': [
    {
        'nivel': 'Educación Secundaria',
        'institucion': 'Unidad Educativa Fiscal Juan León Mera',
        'detalle': 'Bachillerato en Ciencias',
        'descripcion': 'Formación secundaria completa que fortaleció bases académicas, responsabilidad y trabajo en equipo.'
    }
],
        # 🔹 EXPERIENCIA (más viva pero breve)
        'experiencia': [
            {
                'puesto': 'Practicante TI',
                'empresa': 'Proyectos Académicos',
                'descripcion': (
                    'Participación en proyectos académicos aplicando conocimientos de desarrollo web, '
                    'programación en Python y uso de herramientas modernas para el despliegue de aplicaciones.'
                ),
            }
        ],

        # 🔹 PROYECTOS (más interesantes)
        'proyectos': [
            {
                'titulo': 'Práctica de Render',
                'descripcion': (
                    'Aplicación web desarrollada como parte de un bootcamp, '
                    'desplegada en la nube utilizando Render, enfocada en buenas prácticas de desarrollo.'
                ),
                'url': 'https://proyecto2025-4v99.onrender.com'
            },
            {
                'titulo': 'Página Web Navideña',
                'descripcion': (
                    'Página web estática con diseño creativo y temática navideña, '
                    'publicada en GitHub Pages como práctica de maquetación y estilos.'
                ),
                'url': 'https://joshua391125.github.io/josu-391125.github.io/'
            }
        ],

        # 🔹 CERTIFICADOS (con más vida)
        'cursos': [
            {
                'nombre': 'Certificado de Python',
                'institucion': 'Curso de Python',
                'descripcion': 'Capacitación en fundamentos de programación, lógica, estructuras de control y manejo de datos.',
                'url': 'https://drive.google.com/file/d/1tZPwiW_oej5h-0QWprymZMOkrUFMGDwi/view?usp=drive_link'
            },
            {
                'nombre': 'Certificado de HTML y CSS',
                'institucion': 'Formación Complementaria',
                'descripcion': 'Curso enfocado en diseño web, estructura de páginas y estilos responsivos.',
                'url': 'https://drive.google.com/file/d/1wDTdsVZ7IkBFLETni0egMw_g2_q-Oj4a/view?usp=drive_link'
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
