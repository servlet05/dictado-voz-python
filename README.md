# 🎤 Dictado por Voz - Aplicación Web

Aplicación web que permite dictar texto usando el micrófono y convertirlo a audio, con opción de descargar como TXT o Word.

## 🚀 Características

- Grabación de audio en tiempo real
- Transcripción automática usando Google Speech Recognition
- Edición manual del texto transcrito
- Descarga en formatos TXT y DOCX
- Interfaz responsive
- Copiar al portapapeles

## 📋 Requisitos

- Python 3.7+
- Navegador moderno con soporte para WebRTC

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/servlet05/dictado-voz-python.git
cd dictado-voz-python
```
```
    Crear entorno virtual:

bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
```
    Instalar dependencias:

bash

pip install -r requirements.txt
```
```
    Ejecutar la aplicación:

bash

python app.py
```
```
    Abrir navegador en http://localhost:5000
```
```
📦 Estructura del Proyecto
text

dictado-voz/
├── app.py              # Backend Flask
├── requirements.txt    # Dependencias
├── README.md          # Documentación
├── .gitignore         # Archivos ignorados
├── templates/         # Plantillas HTML
│   └── index.html    # Frontend
└── static/           # Archivos estáticos
    └── style.css     # Estilos CSS

⚙️ Cómo usar

    Haz clic en "Iniciar Grabación"

    Permite el acceso al micrófono

    Habla claramente

    Haz clic en "Detener"

    Espera la transcripción

    Edita el texto si es necesario

    Descarga en el formato que prefieras

🛠️ Tecnologías

    Backend: Flask (Python)

    Frontend: HTML5, CSS3, JavaScript

    Reconocimiento de voz: SpeechRecognition + Google API

    Procesamiento de audio: WebRTC, PyAudio

    Documentos: python-docx

📄 Licencia

MIT License
```
