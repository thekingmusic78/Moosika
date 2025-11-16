import yt_dlp
import os
import traceback

def downAudio(url, destino='downs'):
    try:
        # Crear carpeta "downs" si no existe
        carpeta_salida = 'downs'
        os.makedirs(carpeta_salida, exist_ok=True)
    
        opciones = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(carpeta_salida, '%(title)s.%(ext)s'),  # Guarda con el título del video
            'ffmpeg_location': r'C:\ffmpeg\bin',
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'ios', 'web'],
                    'skip': ['hls', 'dash']
                }
            },
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
            },
            'postprocessors': [
                {   # Extrae el audio
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',  # Calidad en kbps
                }
            ],
            'quiet': False  # Puedes poner True si no quieres ver detalles
            'nocheckcertificate': True,
            'no_warnings': False,
        }
        
        
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
            
    except Exception as e:
        # print(f"Error: {e}")
        traceback.print_exc()

# Ejemplo de uso
if __name__ == '__main__':
    enlace = input("Inserte el enlace de YouTube: ")
    print(enlace)
    downAudio(enlace)

