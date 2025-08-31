#!/usr/bin/env python3
"""
Script de prueba para la API directa de MiniMax
"""

import sys
import json
from pathlib import Path

# Agregar el directorio del proyecto al path
sys.path.append('C:/Users/Fabian/Documents/Github/vidgenie')

from utils.minimax_api import MiniMaxAPI

def test_text_to_speech():
    """Prueba la generación de texto a voz"""
    
    print("=== Prueba de API MiniMax ===\n")
    
    # Inicializar API
    api = MiniMaxAPI()
    
    # Prueba 1: Voz de María
    print("1. Generando audio con voz de María...")
    result_maria = api.text_to_speech(
        text="Hola, soy María. Esta es una prueba de la API directa de MiniMax. Bienvenidos a Historias de América.",
        voice_id='maria',
        output_path='test_maria.mp3'
    )
    
    if result_maria['success']:
        print(f"   ✓ Audio generado: {result_maria['output_path']}")
        print(f"   ✓ Tamaño: {result_maria['audio_size']} bytes")
    else:
        print(f"   ✗ Error: {result_maria['error']}")
    
    # Prueba 2: Voz de Carlos
    print("\n2. Generando audio con voz de Carlos...")
    result_carlos = api.text_to_speech(
        text="Hola, soy Carlos. Es increíble pensar cómo estos eventos del pasado siguen influyendo en nuestro presente.",
        voice_id='carlos',
        output_path='test_carlos.mp3'
    )
    
    if result_carlos['success']:
        print(f"   ✓ Audio generado: {result_carlos['output_path']}")
        print(f"   ✓ Tamaño: {result_carlos['audio_size']} bytes")
    else:
        print(f"   ✗ Error: {result_carlos['error']}")
    
    # Prueba 3: Generación de múltiples segmentos
    print("\n3. Generando múltiples segmentos...")
    segments = [
        {
            'id': '001',
            'speaker': 'María',
            'text': '¿Qué sucede cuando tu mayor enemigo se convierte también en tu maestro?'
        },
        {
            'id': '002',
            'speaker': 'Carlos',
            'text': 'Esa es una pregunta que realmente me intriga, María.'
        },
        {
            'id': '003',
            'speaker': 'María',
            'text': 'Hoy exploraremos la fascinante historia de Lautaro, el joven mapuche que cambió el curso de la historia.'
        }
    ]
    
    results = api.generate_audio_segments(segments, 'test_segments')
    
    for result in results:
        if result['status'] == 'success':
            print(f"   ✓ Segmento {result['id']} - {result['speaker']}: Generado")
        else:
            print(f"   ✗ Segmento {result['id']} - {result['speaker']}: {result.get('error', 'Error desconocido')}")
    
    print("\n=== Prueba completada ===")
    
    # Guardar resultados
    with open('test_results.json', 'w', encoding='utf-8') as f:
        json.dump({
            'test_maria': result_maria,
            'test_carlos': result_carlos,
            'segments': results
        }, f, indent=2, ensure_ascii=False)
    
    print("Resultados guardados en test_results.json")

if __name__ == "__main__":
    test_text_to_speech()